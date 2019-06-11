"""
Use this python file as for interactive jupyter notebook data analysis.
This isn't an .ipynb file format, but you can export output cells into a 
notebook after analysis.
Using a regular python file as my workflow, I have a clearler view
of the defined variables.
Also, you can better commit code and have full vscode tools at your disposal.
"""

#%%
# import all the modules needed for data analysis
import sys
import logging

import numpy as np

# import scipy as sp
# import sklearn
# import statsmodels.api as sm
# from statsmodels.formula.api import ols

# import pandas as pd
import pandas as pd

pd.set_option("display.max_rows", 120)
pd.set_option("display.max_columns", 120)

# %load_ext autoreload
# %autoreload 2

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

# import seaborn as sns
# sns.set_context("poster")
# sns.set(rc={'figure.figsize': (16, 9.)})
# sns.set_style("whitegrid")


#%%
frame_data = np.random.randint(0, 100, size=(2 ** 10, 2 ** 8))
df = pd.DataFrame(frame_data)
df.head()

#%%
frame_data

#%%
