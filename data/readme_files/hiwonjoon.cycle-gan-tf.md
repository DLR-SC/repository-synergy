# Cycle-GAN-TF

Reimplementation of [cycle-gan](https://arxiv.org/pdf/1703.10593.pdf) with [improved w-gan](https://arxiv.org/abs/1704.00028) loss in tensorflow.

## Prerequisites

- Tensorflow v1.0

## Training Result

- Training is done with nVidia Titan X Pascal GPU.
- aerial maps <-> maps
![loss graph](/assets/training_loss.png)
    - A(aerial map) -> B(map) -> A
![result of **training** examples(a->b->a)](/assets/a_to_b_to_a.png)
    - B -> A -> B
![result of **training** examples(b->a->b)](/assets/b_to_a_to_b.png)

## Result on test sets

- Each model trained 20000 steps(20000*8/1000 ~= about 160 epochs).

- aerial maps <-> maps
![](/assets/map2airview.jpg)
![](/assets/airview2map.jpg)
- horse <-> zebra
![](/assets/horse2zebra.jpg)
![](/assets/zebra2horse.jpg)
- apple <-> orange
![](/assets/apple2orange.jpg)
![](/assets/orange2apple.jpg)

## Training

### Download dataset

```
./download_dataset.sh [specify a dataset you want]
```

### Run code

Before running the code, change the paths and hyper-parameters as desired in the code.
```
python main.py
```

## Using pretrained model & inference

Before running the code, change the paths as desired in the code.
```
python inference.py
```

## Notes & Acknowledgement

0. The code for download dataset was copied from [here](https://github.com/junyanz/CycleGAN/blob/master/datasets/download_dataset.sh).
1. Network architecture might slightly different from the original paper's one.
    - For instance, different D network (actually, C network in the Wasserstein gan) is used.
2. Tensorflow does not support reflection padding for conv(and decov) layer, so some artifacts can be seen.
