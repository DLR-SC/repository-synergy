# tensorlm

Generate Shakespeare poems with 4 lines of code.

<a href="https://theblog.github.io/post/character-language-model-lstm-tensorflow/" target="_blank">[![showcase of the package](http://i.cubeupload.com/8Cm5RQ.gif)](http://theblog.github.io/post/character-language-model-lstm-tensorflow/)</a>

## Installation

`tensorlm` is written in / for Python 3.4+ and TensorFlow 1.1+

    pip3 install tensorlm
    
## Basic Usage

Use the `CharLM` or `WordLM` class:
```python
import tensorflow as tf
from tensorlm import CharLM
    
with tf.Session() as session:
    
    # Create a new model. You can also use WordLM
    model = CharLM(session, "datasets/sherlock/tinytrain.txt", max_vocab_size=96,
                   neurons_per_layer=100, num_layers=3, num_timesteps=15)
    
    # Train it 
    model.train(session, max_epochs=10, max_steps=500)
    
    # Let it generate a text
    generated = model.sample(session, "The ", num_steps=100)
    print("The " + generated)
```

This should output something like:

    The  ee e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 
  
## Command Line Usage

**Train:** 
`python3 -m tensorlm.cli --train=True --level=char --train_text_path=datasets/sherlock/tinytrain.txt --max_vocab_size=96 --neurons_per_layer=100 --num_layers=2 --batch_size=10 --num_timesteps=15 --save_dir=out/model --max_epochs=300 --save_interval_hours=0.5`

**Sample:**
`python3 -m tensorlm.cli --sample=True --level=char --neurons_per_layer=400 --num_layers=3 --num_timesteps=160 --save_dir=out/model`

**Evaluate:**
`python3 -m tensorlm.cli --evaluate=True --level=char --evaluate_text_path=datasets/sherlock/tinyvalid.txt --neurons_per_layer=400 --num_layers=3 --batch_size=10 --num_timesteps=160 --save_dir=out/model`


See `python3 -m tensorlm.cli --help` for all options.

## Advanced Usage

### Custom Input Data

The inputs and targets don't have to be text. `GeneratingLSTM` only expects token ids, so you can use any data type for the sequences, as long as you can encode the data to integer ids.
```python
# We use integer ids from 0 to 19, so the vocab size is 20. The range of ids must always start
# at zero.
batch_inputs = np.array([[1, 2, 3, 4], [15, 16, 17, 18]])  # 2 batches, 4 time steps each
batch_targets = np.array([[2, 3, 4, 5], [16, 17, 18, 19]])

# Create the model in a TensorFlow graph
model = GeneratingLSTM(vocab_size=20, neurons_per_layer=10, num_layers=2, max_batch_size=2)

# Initialize all defined TF Variables
session.run(tf.global_variables_initializer())

for _ in range(5000):
    model.train_step(session, batch_inputs, batch_targets)

sampled = model.sample_ids(session, [15], num_steps=3)
print("Sampled: " + str(sampled))
```

This should output something like:

    Sampled: [16, 18, 19]

### Custom Training, Dropout etc.

Use the `GeneratingLSTM` class directly. This class is agnostic to the dataset type. It expects integer ids and returns integer ids.

```python
import tensorflow as tf
from tensorlm import Vocabulary, Dataset, GeneratingLSTM

BATCH_SIZE = 20
NUM_TIMESTEPS = 15

with tf.Session() as session:
    # Generate a token -> id vocabulary based on the text
    vocab = Vocabulary.create_from_text("datasets/sherlock/tinytrain.txt", max_vocab_size=96,
                                        level="char")

    # Obtain input and target batches from the text file
    dataset = Dataset("datasets/sherlock/tinytrain.txt", vocab, BATCH_SIZE, NUM_TIMESTEPS)

    # Create the model in a TensorFlow graph
    model = GeneratingLSTM(vocab_size=vocab.get_size(), neurons_per_layer=100, num_layers=2,
                           max_batch_size=BATCH_SIZE, output_keep_prob=0.5)

    # Initialize all defined TF Variables
    session.run(tf.global_variables_initializer())

    # Do the training
    epoch = 1
    step = 1
    for epoch in range(20):
        for inputs, targets in dataset:
            loss = model.train_step(session, inputs, targets)

            if step % 100 == 0:
                # Evaluate from time to time
                dev_dataset = Dataset("datasets/sherlock/tinyvalid.txt", vocab,
                                      batch_size=BATCH_SIZE, num_timesteps=NUM_TIMESTEPS)
                dev_loss = model.evaluate(session, dev_dataset)
                print("Epoch: %d, Step: %d, Train Loss: %f, Dev Loss: %f" % (
                    epoch, step, loss, dev_loss))

                # Sample from the model from time to time
                print("Sampled: \"The " + model.sample_text(session, vocab, "The ") + "\"")

            step += 1

```

This should output something like:

    Epoch: 3, Step: 100, Train Loss: 3.824941, Dev Loss: 3.778008
    Sampled: "The                                                                                                     "
    Epoch: 7, Step: 200, Train Loss: 2.832825, Dev Loss: 2.896187
    Sampled: "The                                                                                                     "
    Epoch: 11, Step: 300, Train Loss: 2.778579, Dev Loss: 2.830176
    Sampled: "The         eee                                                                                         "
    Epoch: 15, Step: 400, Train Loss: 2.655153, Dev Loss: 2.684828
    Sampled: "The        ee    e  e   e  e  e  e  e  e  e   e  e  e   e  e  e   e  e  e   e  e  e   e  e  e   e  e  e "
    Epoch: 19, Step: 500, Train Loss: 2.444502, Dev Loss: 2.479753
    Sampled: "The    an  an  an  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  on  o"
