

# FFTNet

a TensorFlow implementation of the [FFTNet](http://gfx.cs.princeton.edu/pubs/Jin_2018_FAR/)

## Quick Start
1. install requirements
```
pip install -r requirements.txt
```

2. Download data [click here](http://festvox.org/cmu_arctic/cmu_arctic/packed/cmu_us_slt_arctic-0.95-release.tar.bz2)

3. Extract Features
```
python preprocess.py \
    --name cmu_arctic \
    --in_dir your_data_dir \
    --out_dir the_feature_dir \
    --hparams "input_type=mulaw-quantize"  # mulaw_quantize is better in my test
```

4. Training Process

**you can split your `train.txt` into two parts in you data_dir**
```
python train.py \
    --train_file "your_data_dir/train.txt" \
    --val_file "your_data_dir/val.txt" \
    --name "upsample_slt"
```

5. Synthesis Process

```
python synthesis.py \
    --checkpoint_path "your_checkpoint_dir" \
    --output "your_output_dir" \
    --local_path "local_condtion_path"
```