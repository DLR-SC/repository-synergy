# superresolution_gan

Chainer implementation of [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)

### Try

```
wget https://www.dropbox.com/s/l4s5a6v4licks62/generator_model_3008000.npz
python superresolution.py --modelpath generator_model_3008000.npz --imagepath input.png --outputpath sr.png
```

### Training

```
python train.py \
  --gpu=2  \
  --use_discriminator \
  --pretrained_generator generator_model_3008000.npz \
  --dataset "/mnt/dataset/ilsvrc/ILSVRC2012_img_train/*.JPEG" \
  --batchsize=16 \
  --k_mse=0.0001 \
  --k_adversarial=0.00001 \
  --outdirname output/srgan
```
