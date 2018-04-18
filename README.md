[中文版本的 README](README.zh-Hans.md)
------------------------------

# Q-Learning-Demo

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/howl-anderson/q_learning_demo/master?filepath=jupyter_notebooks%2Fproof-of-concept.ipynb)

A project show how Q-learning works from scratch

## Blog

[基于 OpenAI Gym 的 Q-Learning 算法演示](http://blog.xiaoquankong.ai/%E5%9F%BA%E4%BA%8E-OpenAI-Gym-%E7%9A%84-Q-Learning-%E7%AE%97%E6%B3%95%E6%BC%94%E7%A4%BA/)

## Getting Started

Download or git clone this repository.

## Proof of concept
**Online demo**

A Jupyter notebook is provided to demo online. Link is [here](https://mybinder.org/v2/gh/howl-anderson/q_learning_demo/master?filepath=jupyter_notebooks%2Fproof-of-concept.ipynb).

### Prerequisites

Python 3.5+

Check you python version with this
```
python --version
```

### Installing

Git clone the code

```
git clone https://github.com/howl-anderson/q_learning_demo.git
```

then

```
cd q_learning_demo
```

## Running the training

You can train your model or skip this to used pre-trained model

```
python -m q_learning_demo.train
```

### Running the pre-trained model

Use built-in pre-trained model to test model

```
python -m q_learning_demo.load
```

## Built With

* [OpenAI Gym](https://github.com/openai/gym) - The reinforcement framework used

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/howl-anderson/q_learning_demo/tags).

## Authors

* **Xiaoquan Kong** - *Initial work* - [howl-anderson](https://github.com/howl-anderson)

See also the list of [contributors](https://github.com/howl-anderson/q_learning_demo/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Billie Thompson](https://github.com/PurpleBooth) - For README.md & CONTRIBUTING.md template
