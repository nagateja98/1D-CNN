# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D3c_YqqHWvFRH3iq7qdL0brq67MHwrjG
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
dataset = pd.read_csv('/content/housing.csv')
dataset.head(18).plot.line(subplots=True)

