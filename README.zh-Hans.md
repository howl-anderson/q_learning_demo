[README written in English](README.md)
------------------------------

# Q-Learning-Demo

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/howl-anderson/q_learning_demo/master?filepath=jupyter_notebooks%2Fproof-of-concept.ipynb)

从零开始演示 Q-learning 如何工作

## 博客

[基于 OpenAI Gym 的 Q-Learning 算法演示](http://blog.xiaoquankong.ai/%E5%9F%BA%E4%BA%8E-OpenAI-Gym-%E7%9A%84-Q-Learning-%E7%AE%97%E6%B3%95%E6%BC%94%E7%A4%BA/)

## 开始使用

下载或者 clone 这个代码仓库

## 概念验证
**在线演示**

提供了一个 Jupyter notebook 用于在线演示. 地址在 [这里](https://mybinder.org/v2/gh/howl-anderson/q_learning_demo/master?filepath=jupyter_notebooks%2Fproof-of-concept.ipynb).

### 基础依赖

Python 3.5+

检查你的 python 版本
```
python --version
```

### 安装

Git clone 代码

```
git clone https://github.com/howl-anderson/q_learning_demo.git
```

然后

```
cd q_learning_demo
```

## 运行训练脚本

你可以从零开始训练模型或者使用预先训练好的模型（见下文）

```
python -m q_learning_demo.train
```

### 运行预先训练好的模型

使用预先训练好的模型去测试

```
python -m q_learning_demo.load
```

## 所使用的组件

* [OpenAI Gym](https://github.com/openai/gym) - 增强学习框架

## 如何贡献

请仔细阅读 [CONTRIBUTING.md](CONTRIBUTING.md), 然后发送 pull requests 给我们

## 版本

我们使用 [SemVer](http://semver.org/) 的版本规则. 访问 [tags on this repository](https://github.com/howl-anderson/q_learning_demo/tags) 可以查看所有的已发布版本

## 作者

* **Xiaoquan Kong** - *创建者* - [howl-anderson](https://github.com/howl-anderson)

贡献者名单，请访问 [contributors](https://github.com/howl-anderson/q_learning_demo/contributors)

## 协议

本项目使用 MIT License - 详情见 [LICENSE.md](LICENSE.md)

## 致谢

* [Billie Thompson](https://github.com/PurpleBooth) - 感谢其提供 README.md & CONTRIBUTING.md 模板
