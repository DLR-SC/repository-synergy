# topbox
A small Python 3 wrapper around the Stanford Topic Modeling Toolbox (STMT) that makes working with L-LDA a bit easier; no need to leave the Python environment. More information on its workings can be found on [my blog](https://cmry.github.io/notes/topbox).

# Setting up

Just [download](http://nlp.stanford.edu/software/tmt/tmt-0.4/tmt-0.4.0.jar) STMT and put it in the `box` directory. After, import `topbox` from wherever you left it.

On Linux, this would look something like this:

``` shell
$ cd ~
$ git clone https://github.com/cmry/topbox
$ cd ~/topbox/box
$ wget http://nlp.stanford.edu/software/tmt/tmt-0.4/tmt-0.4.0.jar
$ cd ~
$ vi some_topbox_script.py
```

You can paste the code below in the script file to test if it's working.

# Example

``` python
import topbox

stmt = topbox.STMT('bit_of_testing', epochs=10, mem=15000)


space = ['text text more text', 'things to do with text']
labels = ['label1 label2', 'label1 label3']

stmt.train(space, labels)


infer = ['this is a text', 'things with more text']
gs = ['label1 label2', 'label1 label3']

stmt.test(infer, gs)


from sklearn.metrics import average_precision_score

# array requires numpy and scipy
y_true, y_score = stmt.results(gs, array=True)

print(average_precision_score(y_true, y_score))
```
