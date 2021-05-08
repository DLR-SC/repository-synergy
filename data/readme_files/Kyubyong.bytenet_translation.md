# Bytenet Translation

A TensorFlow Implementation of Machine Translation In [Neural Machine Translation in Linear Time](https://arxiv.org/abs/1610.10099)

## Requirements
  * numpy >= 1.11.1
  * TensorFlow >= 1.1 (Probably 1.0 should work as well.)
  * nltk >= 3.2.2 (only for calculating the bleu score)

## Notes
  * This implementation is different from the paper in the following aspects.
    * I used the IWSLT 2016 de-en dataset, not the wmt 2014 de-en dataset, which is much bigger.
    * I applied a greedy decoder at the inference phase, not the beam search decoder.
    * I didn't implement `Dynamic Unfolding`.

## Steps
  * STEP 1. Download [IWSLT 2016 German–English parallel corpus](https://wit3.fbk.eu/download.php?release=2016-01&type=texts&slang=de&tlang=en) and extract it to `corpora/` folder.
  * STEP 2. Run `train.py`.
  * STEP 3. Run `eval.py` to get test results

Or if you'd like to use the pretrained model,

  * Download and extract [the pre-trained model files](https://www.dropbox.com/s/c6b833wxvfkst97/log.tar.gz?dl=0), and then run `eval.py`.

## Results
After 15 epochs, I obtained the Bleu score 7.38, which is far from good. Maybe some part in the implementation is incorrect. Or maybe we need more data or a bigger model. Details are available in the `results` folder.
