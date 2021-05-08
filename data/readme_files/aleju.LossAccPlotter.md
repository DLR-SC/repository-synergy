# About

The LossAccPlotter is a small class to generate plots during the training of machine learning algorithms (specifically neural networks) showing the following values over time/epochs:
* The result of the _loss_ function, when applied to the _training_ dataset.
* The result of the _loss_ function, when applied to the _validation_ dataset.
* The _accuracy_ of the current model, when applied to the _training_ dataset.
* The _accuracy_ of the current model, when applied to the _validation_ dataset.

Some Features:
* Automatic regression on your values to predict future values over the next N epochs.
* Automatic generation of averages to get a better estimate of your true performance (i.e. to get rid of variance).
* Option to save the plot automatically to a file (at every update).
* The plot is non-blocking, so your program can train in the background while the plot gets continuously updated.

# Requirements

* matplotlib
* numpy
* python 2.7 (only tested in that version - may or may not work in other versions)
    * [python 3 fork of the library](https://github.com/JamesLuoau/LossAccPlotter)

# Example images

![Example plot with loss and accuracy](images/example_plot.png?raw=true "Example plot with loss and accuracy")

![Example plot, only loss function](images/example_plot_loss.png?raw=true "Example plot, only loss function")

![Example plot, different update intervals](images/example_plot_update_intervals.png?raw=true "Example plot, different update intervals")

![Example plot, only training set results](images/example_plot_only_training.png?raw=true "Example plot, only training set results")

# Example code

In order to use the `LossAccPlotter`, simply copy `laplotter.py` into your project's directory, import `LossAccPlotter` from the file and then add some values to the plotted lines, as shown in the following examples.

Example loop over 100 epochs:

```python
from laplotter import LossAccPlotter

plotter = LossAccPlotter()

for epoch in range(100):
    # somehow generate loss and accuracy with your model
    loss_train, acc_train = your_model.train()
    loss_val, acc_val = your_model.validate()
    
    # plot the last values
    plotter.add_values(epoch,
                       loss_train=loss_train, acc_train=acc_train,
                       loss_val=loss_val, acc_val=acc_val)

# As the plot is non-blocking, we should call plotter.block() at the end, to
# change it to the blocking-mode. Otherwise the program would instantly end
# and thereby close the plot.
plotter.block()
```

All available settings for the `LossAccPlotter`:

```python
from laplotter import LossAccPlotter

# What these settings do:
# - title: A title shown at the top of the plot.
# - save_to_filepath: File to save the plot to at every update.
# - show_regressions: Whether to predict future values with regression.
# - show_averages: Whether to show moving averages for all lines.
# - show_loss_plot: Whether to show the plot of the loss function (on the left).
# - show_acc_plot: Whether to show the plot of the accuracy (on the right).
# - show_plot_window: Whether to show the plot as a window (on e.g. clusters you might want to deactivate that and only save to a file).
# - x_label: Label of the x-axes (e.g. "Epoch", "Batch", "Example").
plotter = LossAccPlotter(title="This is an example plot",
                         save_to_filepath="/tmp/my_plot.png",
                         show_regressions=True,
                         show_averages=True,
                         show_loss_plot=True,
                         show_acc_plot=True,
                         show_plot_window=True,
                         x_label="Epoch")

# ...
```

You don't have to provide values for all lines at every epoch:

```python
from laplotter import LossAccPlotter

plotter = LossAccPlotter()
for epoch in range(100):
    loss_train, acc_train = your_model.train()

    # Validate only every 25th epoch
    # both validation lines will be less smooth than the lines of the training dataset
    if epoch % 25 == 0:
        loss_val, acc_val = your_model.validate()
    else:
        loss_val, acc_val = None, None

    plotter.add_values(epoch,
                       loss_train=loss_train, acc_train=acc_train,
                       loss_val=loss_val, acc_val=acc_val)
plotter.block()
```


When adding many values in a row (e.g. when loading a history from a file), you should add `redraw=False` to the `add_values()` call, otherwise the plotter will spend a lot of time rebuilding the chart many times:

```python
from laplotter import LossAccPlotter
import numpy as np

plotter = LossAccPlotter()

# generate some example values for the loss training line
example_values = np.linspace(0.8, 0.1, num=100)

# add them all
for epoch, value in enumerate(example_values):
    # deactivate redrawing after each update
    plotter.add_values(epoch, loss_train=value, redraw=False)

# redraw once at the end
plotter.redraw()

plotter.block()
```


# Tests

There are no automated tests, as it's rather hard to measure the quality of a plot automatically.
You can however run a couple of checks on the library, which show various example plots.
These plots should all look plausible and "beautiful".
Run the checks via:

```python
python check_laplotter.py
```

# License

MIT
