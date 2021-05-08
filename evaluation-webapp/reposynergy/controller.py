import pandas as pd
import csv

from django.http import HttpResponse
from .models import RepositoryPair, Annotation, User

################# Helpers #################

def qs_to_df(qs):
    if qs is not None:
        return pd.DataFrame(list(qs.values()))
    return None

def get_repo_readme(url):
    folder = "data/readme_files" # "data/readme_files"
    path = '{}/{}.md'.format(folder, '.'.join(url.split('/')[-2:]))
    data = None#

    with open(path, 'r', encoding="utf8") as file:
        data = file.read()

    return data

################# DF Helpers #################

def _set_synergy_label(row):
    synergy_map= {1:'None', 2:'Weak', 3:'Somewhat', 4:'Strong'}
    direction_map = {0: 'None', 12: 'repo1 can benefit from repo2', 21: 'repo2 can benefit from repo1',
                     2: 'both can benefit from each others'}
    row['synergy'] = synergy_map[int(row['synergy'])] if row['synergy'] != '' else ''
    row['direction'] = direction_map[int(row['direction'])] if row['direction'] != '' else ''
    return row

################# Controller methods #################

def get_annotations_info(user_id, batch):
    print('batch: ', batch)
    repo_pair_df = qs_to_df(RepositoryPair().getBatchRepoPairs(batch))
    repo_pair_df.sort_values(['id'], inplace=True)
    repo_pair_df.set_index('id', inplace=True)

    annotation_df = qs_to_df(Annotation.getUserAnnotations(user_id)) # annotation_date,synergy, explanation
    if annotation_df is not None and len(annotation_df) > 0:
        annotation_df.set_index('repository_pair_id', inplace=True)
        repo_pair_df = repo_pair_df.join(annotation_df, how='left', rsuffix='_annotator' )
        repo_pair_df['synergy'].fillna('', inplace=True)
        repo_pair_df['explanation'].fillna('', inplace=True)
        repo_pair_df['direction'].fillna('', inplace=True)
    else:
        repo_pair_df['synergy'] = ''
        repo_pair_df['explanation'] = ''
        repo_pair_df['direction'] = ''
        repo_pair_df['annotation_date'] = None

    repo_pair_df = repo_pair_df.apply(_set_synergy_label, axis=1)
    repo_pair_df.reset_index(inplace=True)

    total = len(repo_pair_df)
    annotated = len(annotation_df) if annotation_df is not None else 0

    return repo_pair_df, total, annotated

def _add_annotations_info(row, annotations):
    synergy_map = {1: 'None', 2: 'Weak', 3: 'Somewhat', 4: 'Strong'}
    direction_map = {0: 'None', 12: 'repo1 can benefit from repo2', 21: 'repo2 can benefit from repo1',
                     2: 'both can benefit from each others'}

    repo_id = row['id']
    repo_annotations = annotations[annotations['repository_pair_id'] == repo_id].copy() if (annotations is not None and len(annotations) >0) else None

    if (repo_annotations) is not None :
        row['annotations_num'] = len(repo_annotations)
        row['labels'] = ','.join([synergy_map[x] for x in   list(repo_annotations['synergy'].values)])
        row['directions'] = ','.join([direction_map[x] for x in list(repo_annotations['direction'].values)])
        row['users'] = ', '.join([str(x) for x in list(repo_annotations['user_id'].values)])
    return row

def get_all_annotations(batch):
    repo_pair_df = qs_to_df(RepositoryPair().getBatchRepoPairs(batch))
    annotations_df = qs_to_df(Annotation().get_batch_annotations(batch))


    repo_pair_df['annotations_num'] = 0
    repo_pair_df['labels'] = ''
    repo_pair_df['directions'] = ''
    repo_pair_df['users'] = ''

    repo_pair_df = repo_pair_df.apply(_add_annotations_info, axis=1, args=(annotations_df,))
    annotated_count = len(repo_pair_df[repo_pair_df['annotations_num'] >= 3])
    total = len(annotations_df)
    return repo_pair_df, annotated_count, total

def get_unnotated(user_id, batch):
    all_annotations, total, annotated = get_annotations_info(user_id, batch)
    unnotated_df = (all_annotations[all_annotations['synergy'] == '']).copy()
    return unnotated_df

def get_next_unnotated_pair(user_id, batch):
    unnotated_df = get_unnotated(user_id, batch)
    return unnotated_df.id.values[0] if (len(unnotated_df) > 0) else None

def get_repo_pair_info(pair_id):
    repo_pair =  RepositoryPair.objects.get(pk=pair_id)

    repo1_readme =get_repo_readme(repo_pair.repo_url1)
    repo2_readme =get_repo_readme(repo_pair.repo_url2)

    return repo1_readme, repo2_readme

#### Export
def export_to_csv(model_class= None, df=None, name=''):

    data = qs_to_df(model_class.objects.all()) if (model_class is not None) else df.copy()
    response = None

    if data is not None:
        meta = model_class._meta if (model_class is not None) else name
        field_names = list(data.columns.values)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for _, row in data.iterrows():
            row = writer.writerow([row[field] for field in field_names])

    return response

def deactivate_user(user_id):
    User().re_deactivate(user_id, activate=False)

def activate_user(user_id):
    User().re_deactivate(user_id)