import scipy.stats as stats

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import numpy as np
import pandas as pd
import math
import warnings
import itertools

def cohend(d1, d2):
	# calculate the size of samples
	n1, n2 = len(d1), len(d2)
	# calculate the variance of the samples
	s1, s2 = math.var(d1, ddof=1), math.var(d2, ddof=1)
	# calculate the pooled standard deviation
	s = math.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
	# calculate the means of the samples
	u1, u2 = math.mean(d1), math.mean(d2)
	# calculate the effect size
    
	return (u1 - u2) / s

def effect_size_r(p_val, N):
    z = stats.norm.ppf(1-((1-p_val)))
    sqrt_n = math.sqrt(N)
    return z/sqrt_n


def anova_table(aov):
    aov['mean_sq'] = aov[:]['sum_sq']/aov[:]['df']
    
    aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])
    
    aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*aov['mean_sq'][-1]))/(sum(aov['sum_sq'])+aov['mean_sq'][-1])
    #eta squared (η2), and omega squared (ω2)
    cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq']
    aov = aov[cols]
    return aov


def significance(original_df, features = None, save = False, desc='', independent_var='cluster'):
    result = []
    warnings.filterwarnings('ignore')
    print('data has {} instances'.format(str(len(original_df))))

    # to save the data
    row = "sep=;\nfeature;is_normal (shapiro);is_homogeneous (levene);p_value;is_significant;effect;result"
    # all pairs
    pairs = list(itertools.combinations(original_df[independent_var].unique(), 2))
    
    for pair in pairs:
        row += ';' + str(pair) + ';' + str(pair) 
    row += '\n'
    
    
    # thresholds
    p_value_threshold = 0.05
    bonforrini_threshold = p_value_threshold / len(pairs)
    print('bonforrini_threshold: ', bonforrini_threshold)
    
    # conduct sig. test for each characteristic
    if features is None:
        features = list(original_df.columns)
        features.remove(independent_var)

    for feature in features:

        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                

                df = original_df[[independent_var, feature ]]
                # Get feature values for each group
                groups = {}
                for g, g_df in original_df.groupby([independent_var]):
                    groups[g] = g_df[feature]
                
                # SHAPIRO FOR NORMALITY
                is_all_normal= True
                try:
                    for v in groups.values():
                        if (stats.shapiro(v)[1] < 0.05): # not normal
                            is_all_normal= False
                            break
                except Warning as w:
                    is_all_normal= False
                    
                # LEVENE FOR HOMOGENEITY
                is_homogeneous = False
                if is_all_normal:
                    is_homogeneous = stats.levene(*groups.values())[1] >= 0.05


                # DEFAULTS
                stat = -1
                p_val = np.nan
                str_res = ''
                effect_interpretation = ''

                # sig TESTS FOR EACH FEATURE
                if is_all_normal and is_homogeneous:
                    #stat, p_val = stats.f_oneway(no_effect_feat, empowering_feat, challenging_feat, na_feat)
                    anova_result = ols(feature+' ~ C('+independent_var+')', data=df).fit()
                    aov_table = anova_lm(anova_result, typ=2)

                    aov = anova_table(aov_table).loc['C('+independent_var+')']

                    stat = aov['F']
                    p_val = aov['PR(>F)']
                    effect_omega = aov['omega_sq']

                    #low (0.01 – 0.059), medium (0.06 – 0.139), and large (0.14+) 


                    if p_val < p_value_threshold:

                        effect_interpretation = 'high'
                        if effect_omega < 0.06:
                            effect_interpretation = 'low'
                        elif effect_omega < 0.14:
                            effect_interpretation = 'medium'

                    str_res = "F({0},{1})= {2:.2f}, p = {3:.7f}, ω2 = {4:.2f}".format(int(anova_result.df_model), int(anova_result.df_resid), stat, p_val, effect_omega)

                else:
                    stat, p_val = stats.kruskal(*groups.values()) #, na_feat)

                pairs_results = ''
                result_row = {}
                result_row['feature'] = feature
                for pair in pairs:
                    try:
                        sample1 = list((df[feature][df[independent_var] == pair[0]]).values)
                        sample2 = list((df[feature][df[independent_var] == pair[1]]).values)

                        pair_stat, pair_p_val = stats.ttest_ind(sample1, sample2) if ( is_all_normal and is_homogeneous) else stats.mannwhitneyu(sample1, sample2, alternative = 'two-sided')

                        pair_effect_size =''
                        pair_effect_size_num = float('nan')
                        if pair_p_val < bonforrini_threshold:
                            N = len(sample1) + len(sample2)
                            if is_all_normal and is_homogeneous:
                                z = stats.norm.ppf(1-(1-pair_p_val))
                                pair_effect_size_num = round((z)/(np.sqrt(N)), 2)
                                pair_effect_size = str(pair_effect_size_num)
                            else:
                                m_u = len(sample1)*len(sample2)/2
                                sigma_u = np.sqrt(len(sample1)*len(sample2)*(len(sample1)+len(sample2)+1)/12)
                                z = (pair_stat - m_u)/sigma_u
                                pair_effect_size_num = round((z)/(np.sqrt(N)), 2)
                                pair_effect_size = str(pair_effect_size_num)
                        #if pair_stat < bonforrini_threshold:
                        result_row[pair[0]+ ' '+pair[1]] = pair_effect_size_num

                        pair_res = "{0}".format((pair_p_val < bonforrini_threshold))
                        pairs_results += ';' + str(pair_res) + ';' + pair_effect_size

                    
                    except Exception as e:
                        print(feature)
                        pairs_results += ';same values;same values'
                        print('INNER EXCEPTION', e)
                        
                        #logging.error(traceback.format_exc())



                row += "{};{};{};{};{};{};{}".format( feature, 
                                                    is_all_normal, is_homogeneous, p_val, (p_val<0.05),
                                                           effect_interpretation,str_res)
                row +=  pairs_results
                row += '\n'
                if not np.isnan(p_val) and  p_val < p_value_threshold:
                    result.append(result_row)  
            
            except Exception as e:
                print('exception for feature ', e)
                
    # Saving 
    if save:

        filename = '{}.csv'.format( desc)
        with open(filename, 'w', encoding="utf-8") as w:
            w.write(row)
    result_df = pd.DataFrame(result)
    result_df.set_index(['feature'], inplace=True)
    return result_df