
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]]()
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/justinglibert/bezos">
    <img src="https://raw.githubusercontent.com/justinglibert/bezos/master/github/icon.gif" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Bezos :godmode:: Build your own Reinforcement Learning framework</h3>

  <p align="center">
    Bezos is a light Deep RL framework that you can fork and extend.
    <br />
    <br />
    <br />
    <a href="https://github.com/justinglibert/bezos/issues">Report Bug</a>
    ·
    <a href="https://github.com/justinglibert/bezos/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Features](#features)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
  - [Train a model (params in the config file)](#train-a-model-params-in-the-config-file)
  - [Evaluate a model](#evaluate-a-model)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <img src="https://raw.githubusercontent.com/justinglibert/bezos/master/github/cover.gif"/>
</p>



There are many great reinforcement learning frameworks on GitHub, however, I didn't find one that was light and small enough to let me fork it and add my own algorithms while still feeling in control. I thus created Bezos, a very light RL framework which implements all the boring things so that you don't have to. 

## Features
- Rollout class (supports GAE, reward to go, and recurrent neural network)
- Runner class: loads a Gym env and runs one or multiple agents on the environment to generate rollouts
- A simple Actor Critic Network
- RL Algorithm: PPO [Paper on Arxiv](https://arxiv.org/abs/1707.06347)
- RL Algorithm: A2C [OpenAI blog post](https://openai.com/blog/baselines-acktr-a2c/)
- Supports all the OpenAI Gym env
- I added all the Vizdoom envs as well (look into kits/)
- Supports the marLo env [Github](https://github.com/crowdAI/marLo) (look into kits/)
- A bunch of useful OpenAI Gym wrappers. Includes frame skipping, RGB→Grayscale, cropping, and many more. (look into envs.py)

### Built With
The framework uses Pytorch to do all the deep learning stuff, numpy, and OpenAI Gym
* [Pytorch](https://github.com/pytorch/pytorch)
* [OpenAI Gym](https://github.com/openai/gym)
* [Numpy](https://github.com/numpy/numpy)



<!-- GETTING STARTED -->
## Getting Started

Bezos has been designed to be configured before each run with a YAML file. Some examples of those YAML config files can be found in the configs folder. If you want to know what a parameter does (they are all self explanatory) check the source :)

### Installation

- Create a new conda env (yo don't use python 2 ok)
- ```pip install -r requirements.txt ```




<!-- USAGE EXAMPLES -->
## Usage
### Train a model (params in the config file) 
```bash
python bezos.py --config ./configs/ppo-minecraft.yaml train
```
### Evaluate a model
```bash
python bezos.py --config ./configs/ppo-minecraft.yaml evaluate --det
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/justin-glibert-108272133/
[product-screenshot]: https://raw.githubusercontent.com/justinglibert/bezos/master/github/bezos.gif
