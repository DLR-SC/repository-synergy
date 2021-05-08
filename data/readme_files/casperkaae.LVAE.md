# Probabilistic Ladder
Code to run experiments in

*Sønderby, C.K., Raiko, T., Maaløe, L., Sønderby, S.K. and Winther, O., 2016.*  
*How to Train Deep Variational Autoencoders and Probabilistic Ladder Networks.*  
*arXiv preprint [arXiv:1602.02282](http://arxiv.org/abs/1602.02282).*  

The code is not well documented at the moment, please feel free to ask questions by writing me an email or creating a github-issue.

### Example
To run a VAE model with 3 layers of stochastic units, each connected by a two-layer MLP:

*VAE: X->MLP->Z1->MLP->Z2->MLP->Z3->MLP->Z2->MLP->Z1->MLP->Xrecon*

```
python run_models.py \
	-lr 0.00020 \
	-modeltype VAE \
	-batch_size 256 \
	-dataset mnistresample \
	-mlp_layers 2 \
	-latent_sizes 64,32,16 \
	-hidden_sizes 512,256,128 \
	-nonlin_dec leaky_rectify \
	-nonlin_enc leaky_rectify \
	-only_mu_up True \
	-eq_samples 1 \
	-iw_samples 1 \
	-ramp_n_samples True \
	-batch_norm True \
	-batch_norm_output False \
	-temp_start 0.00 -temp_epochs 200 \
	-num_epochs 2000 -eval_epochs 100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000 \
	-ladder_share_params False \
	-only_mu_up True \
	-lv_eps_z 1e-5 \
	-lv_eps_out 1e-5 \
	-outfolder results/mnistresample_VAE
```

Corresponding ladderVAE model

```
python run_models.py \
	-lr 0.00020 \
	-modeltype ladderVAE \
	-batch_size 256 \
	-dataset mnistresample \
	-mlp_layers 2 \
	-latent_sizes 64,32,16 \
	-hidden_sizes 512,256,128 \
	-nonlin_dec leaky_rectify \
	-nonlin_enc leaky_rectify \
	-only_mu_up True \
	-eq_samples 1 \
	-iw_samples 1 \
	-ramp_n_samples True \
	-batch_norm True \
	-batch_norm_output False \
	-temp_start 0.00 -temp_epochs 200 \
	-num_epochs 2000 -eval_epochs 100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000 \
	-ladder_share_params False \
	-only_mu_up True \
	-lv_eps_z 1e-5 \
	-lv_eps_out 1e-5 \
	-outfolder results/mnistresample_ladderVAE
```
