# RocAlphaGo.data

Version controlled data for the [Rochester-NRT/AlphaGo](https://github.com/Rochester-NRT/AlphaGo) repository.

## Where is the data?

Still working on it. Follow progress in the [main repository](https://github.com/Rochester-NRT/AlphaGo). There is enough here to load and run a few partially-trained policy networks as standalone players.

## Directory structure

`scripts/` contains short code snippets that we've found useful

`expert_play/` contains datasets of SGF files. We do not have permission to release all datasets that we are using, hence some models are trained on datasets not present in this directory

`models/` contains `json` model specifications. For example

* `models/CNNPolicy/12plane_default.json` specifies a `CNNPolicy` object with the features `['board', 'ones', 'turns_since']`
* `models/CNNPolicy/20plane_default.json` is likewise, with the features `['board', 'ones', 'turns_since', 'liberties']`
* `models/CNNPolicy/46plane_default.json` is likewise with all features except ladders

`training_results/` contains trained models and epoch checkpoints.