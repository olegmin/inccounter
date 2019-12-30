# Libraries
import numpy as np
import pandas as pd


# Configuration
M = 2
N = 10


# Data Frame
df = pd.DataFrame({
    'feature1': np.random.randint(M, size=(N,)),
    'feature2': np.random.randint(M, size=(N,)),
    'time': np.random.rand(N)
})


# Save data to CSV-file
df.to_csv('/data/incedents.csv', index_label='id')
