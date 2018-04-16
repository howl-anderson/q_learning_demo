import random


def set_global_seeds(i):
    try:
        import tensorflow as tf
    except ImportError:
        pass
    else:
        tf.set_random_seed(i)

    try:
        import numpy as np
    except ImportError:
        pass
    else:
        np.random.seed(i)

    random.seed(i)
