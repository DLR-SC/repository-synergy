# Tensorpeers
P2P peer-to-peer training of deep learning [tensorflow](https://github.com/tensorflow/tensorflow) models

Not to be confused with [locally distributed training](https://www.tensorflow.org/how_tos/distributed/),
However presumably a lot can be learned from tf.train.Supervisor etc

## Community Power
In the Golden age of deep learning, baidu and others have shown that training time can scale almost linearly with the number of GPUs.
This gives large corporations an advantage over startups in the run for the best A.I. systems ... until now.

Tensorpeers will empower the community to combine their efforts and GPU time into quickly converging wonderful models.

## Architecture
The architecture has to be slightly different from existing 'parameter server' schemes, because of relatively slow Internet connections. However our optimistic guess is that this won't hinder the success of this project: as long as we find any  merging scheme, which successfully combines the *gained knowledge* of two separate runs, we should be fine.

To speed things up, we base this project on python-libtorrent.

## Install dependency:
MAC:
`brew install libtorrent-rasterbar --with-python`
LINUX:
`apt-get install python-libtorrent` or
`apt-get install python3-libtorrent`

## Open questions
This is a wildly wide open research area, so if you want to make the world a better place (and or need a PhD thesis):
Herewith you have full leverage.


<!--
This is a wildly wide open research area, so if you want to make the world a better place (and or need a PhD thesis):
Herewith you have full leverage.

Not to be confused with [exxact p2p deep-learning](https://exxactcorp.com/deep-learning-p2p.php)-->
