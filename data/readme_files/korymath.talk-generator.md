# Talk Powerpoint Generator
[![CircleCI](https://circleci.com/gh/korymath/talk-generator.svg?style=svg&circle-token=dcba7d5a9ff7953cff0526e201990c0b811b3aae)](https://circleci.com/gh/korymath/talk-generator)
[![codecov](https://codecov.io/gh/korymath/talk-generator/branch/master/graph/badge.svg?token=gqkCyuXop0)](https://codecov.io/gh/korymath/talk-generator)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/korymath/britbot/blob/master/LICENSE.md)

## Description

Software to automatically generate talks, presentations for PowerPoint and/or Keynote. Their main purpose is for the improvisational comedy format *"Improvised TED talk"* or *"Powerpoint Karaoke"*, where the actors have to present an unseen presentation slide deck, but pretend to be an expert and explain their slide show choices.

## Demo

For a demo of this generator, please visit [talkgenerator.com](http://talkgenerator.com/), a platform created by [Shaun Farrugia](https://github.com/h0h0h0) to give easier access to this talk generator.

### Example

![Automatically Generated](https://media.giphy.com/media/MXXe522nIAA9JZjExI/giphy.gif)

## Easy Install and Run

Our program relies on certain APIs that require authentication in order to use it.
Create a file named `.env` (don't forget the period) in your project directory, and fill this with the correct API keys as described on our [wiki page about this](https://github.com/korymath/talk-generator/wiki/Setting-Up-API-Keys).

```sh
# Make a new Python 3 virtual environment 
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and install  requirements
pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Download NLTK dependencies
python3 -m nltk.downloader punkt averaged_perceptron_tagger

# Install the Talk Generator 
pip install -e .

# Generate a 10 slide talk with topic peanuts
talkgenerator --topic "peanuts" --num_slides 10
```

### Run arguments

| Argument               | Description               |
| ---------------------- | ------------------------- |
| `topic` | The topic of the generator. This works best if it is a common, well-known noun. Use comma-separated words to generate a slide deck about multiple topics |
| `slides` | The number of slides in the generated presentation (*default: 10*) |
| `schema` | The presentation schema to use when generating the presentation. Currently, only two modes are implemented, being `default` and `test` (for testing during development) |
| `title` | Title of the presentation. Either `topic` or this one should to be set in order to generate a slide deck (just setting `topic` is usually more fun though)  |
| `presenter` | The name that will be present on the first slide. Leave blank for an automatically generated name |
| `output_folder` | The folder to output the generated presentations (*default: `./output/`*) |
| `save_ppt` | If this flag is true(*default*), the generated powerpoint will be saved on the computer in the `output_folder`|
| `open_ppt` | If this flag is true (*default*), the generated powerpoint will automatically open after generating|
| `parallel` | If this flag is true (*default*), the generator will generate all slides in parallel |

## Program structure

See the [wiki](https://github.com/korymath/talk-generator/wiki/Program-structure) to know more about the inner implementation.

## Tests
Test files are `tests/*.py`, prefixed with `test_`. Test files use the `unittest` module.
They can easily be run all together when using PyCharm by right clicking on `talk-generator` and pressing *Run 'Unittests in talk-generator'*

```sh
. venv/bin/activate
pytest --cov=talkgenerator tests/
```

Test coverage is automatically handled by `codecov`. Tests are automatically run with CircleCI based on the `.yml` file in the `.circleci` directory.

## Credits

This ``Talk Generator`` is made by [Kory Mathewson](https://github.com/korymath)
and [Thomas Winters](https://github.com/TWinters),
with help from [Shaun Farrugia](https://github.com/h0h0h0), [Piotr Mirowski](https://github.com/piotrmirowski) and [Julian Faid](https://github.com/jfaid).

If you would like to refer to this project in academic work, please cite the following paper:

Winters T., Mathewson K.W. (2019) **Automatically Generating Engaging Presentation Slide Decks**. In: Ekárt A., Liapis A., Castro Pena M. (eds) Computational Intelligence in Music, Sound, Art and Design. EvoMUSART 2019. Lecture Notes in Computer Science, vol 11453. Springer, Cham

```
@InProceedings{winters2019tedric,
    author="Winters, Thomas
    and Mathewson, Kory W.",
    editor="Ek{\'a}rt, Anik{\'o}
    and Liapis, Antonios
    and Castro Pena, Mar{\'i}a Luz",
    title="Automatically Generating Engaging Presentation Slide Decks",
    booktitle="Computational Intelligence in Music, Sound, Art and Design",
    year="2019",
    publisher="Springer International Publishing",
    address="Cham",
    pages="127--141",
    isbn="978-3-030-16667-0"
}
```

## License

MIT License. Copyright (c) 2018 [Kory Mathewson](https://github.com/korymath), [Thomas Winters](https://github.com/TWinters), and [Shaun Farrugia](https://github.com/h0h0h0).
