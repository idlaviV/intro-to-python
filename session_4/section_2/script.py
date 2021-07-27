## Session 4 - Section 2
## Dimension-Reduction: Umap and PCA

# For UMAP we can use the umap-learn package:
# https://umap-learn.readthedocs.io/en/latest/


import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# pandas can also read from urls
penguins = pd.read_csv("https://github.com/allisonhorst/palmerpenguins/raw/5b5891f01b52ae26ad8cb9755ec93672f49328a8/data/penguins_size.csv")

# drop na values
penguins = penguins.dropna()
print(penguins)

# sns pair-plot:
sns.pairplot(penguins, hue='species_short')
plt.show()

import umap

# reducer = umap.UMAP()
# 
# penguin_data = penguins[
#     [
#         "culmen_length_mm",
#         "culmen_depth_mm",
#         "flipper_length_mm",
#         "body_mass_g",
#     ]
# ].values
# scaled_penguin_data = StandardScaler().fit_transform(penguin_data)
# 
# 
# embedding = reducer.fit_transform(scaled_penguin_data)
# embedding.shape
# 
# 
# plt.scatter(
#     embedding[:, 0],
#     embedding[:, 1],
#     c=[sns.color_palette()[x] for x in penguins.species_short.map({"Adelie":0, "Chinstrap":1, "Gentoo":2})])
# plt.gca().set_aspect('equal', 'datalim')
# plt.title('UMAP projection of the Penguin dataset', fontsize=24)
# plt.show()

# in comparison to PCA:
from sklearn.decomposition import PCA
	
sex = penguins.sex.tolist()
species = penguins.species_short.tolist()

pca = PCA(n_components=4)
penguins_pca = pca.fit_transform(penguin_data)


pc_df = pd.DataFrame(data = penguins_pca , 
        columns = ['PC1', 'PC2','PC3', 'PC4'])

pc_df['sex'] = sex
pc_df['species'] = species


plt.figure(figsize=(12,10))
sns.scatterplot(x="PC1", y="PC2",
                    data=pc_df, 
                    hue="species",
                    style="sex",
                    s=100)
plt.show()