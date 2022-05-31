import numpy as np
import pytest


def test_random_number_seed():
    np.random.seed(1)
    a = np.random.normal()
    assert np.isclose(a, 1.6243453636632417)
