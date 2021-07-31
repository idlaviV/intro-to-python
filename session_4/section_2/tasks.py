#------------------------------------------------------------------------------#
# (1)
# Apply UMAP or PCA to the cc_data - the location is encoded as an int
# index of the following list:

['Carlyle Chemical Inc.', 'Nationwide Refinery', 'Daily Dealz', 'General Grocer', 'Roberts and Sons', "Frank's Fuel", "Shoppers' Delight", 'Ouzeri Elian', "Albert's Fine Clothing", 'Bean There Done That', 'Hallowed Grounds', "Katerina's Cafe", 'Ahaggo Museum', 'Kronos Pipe and Irrigation', 'Coffee Cameleon', "Guy's Gyros", 'U-Pump', 'Abila Scrapyard', 'Maximum Iron and Steel', 'Abila Zacharo', 'Chostus Hotel', 'Gelatogalore', 'Coffee Shack', 'Brewed Awakenings', "Brew've Been Served", 'Kronos Mart', 'Abila Airport', 'Kalami Kafenion', "Frydos Autosupply n' More", 'Desafio Golf Course', "Octavio's Office Supplies", "Jack's Magical Beans", 'Stewart and Sons Fabrication', 'Hippokampos']

# I transformed it with this line:
# df.location = df.location.apply(lambda x: locs.index(x))

# There is a further field "hour" and minute 
# df[['hour', "minute"]] = df.time.str.split(":", expand=True)
# Include location, price, last4ccnum and maybe hour

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import umap

reducer = umap.UMAP()

df = pd.read_csv("data/cc_data_2.csv")
print(df)

data = df[
    [
        "hour",
        "price",
        "last4ccnum",
    ]
].values
scaled_data = StandardScaler().fit_transform(data)


embedding = reducer.fit_transform(scaled_data)
embedding.shape


plt.scatter(
    embedding[:, 0],
    embedding[:, 1])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the CC dataset', fontsize=24)
plt.show()
