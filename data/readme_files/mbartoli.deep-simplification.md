# deep-simplification
Text simplification using RNNs. Our deep-simplification model achieves a BLEU score of 61.14

## Training
Navigate to the simplify directory and run
```
THEANO_FLAGS=device=gpu,floatX=float32 python train_nmt.py 
```

## Sampling
Navigate to the simplify directory and run
```
THEANO_FLAGS=device=cpu,floatX=float32 python translate.py -n -p 1 model_hal.npz \
    ../data/dictionaries/simple.wiki.tok.pkl \
    ../data/dictionaries/simple.wiki.tok.pkl \
    ../data/testing/testing.normal.aligned.tok \
    ../data/testing/testing.simple.aligned.out.tok
```

## Testing
Navigate to the simplify directory and run 
```
perl multi-bleu.perl ../data/testing/testing.simple.tok < \
    ../data/testing/testing.simple.aligned.out.tok 
```
