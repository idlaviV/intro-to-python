#------------------------------------------------------------------------------#
# (1)
# Apply UMAP or PCA to the cc_data - the location is encoded as an int
# index of the following list:
import pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
locs = ['Carlyle Chemical Inc.', 'Nationwide Refinery', 'Daily Dealz', 'General Grocer', 'Roberts and Sons', "Frank's Fuel", "Shoppers' Delight", 'Ouzeri Elian', "Albert's Fine Clothing", 'Bean There Done That', 'Hallowed Grounds', "Katerina's Cafe", 'Ahaggo Museum', 'Kronos Pipe and Irrigation', 'Coffee Cameleon', "Guy's Gyros", 'U-Pump', 'Abila Scrapyard', 'Maximum Iron and Steel', 'Abila Zacharo', 'Chostus Hotel', 'Gelatogalore', 'Coffee Shack', 'Brewed Awakenings', "Brew've Been Served", 'Kronos Mart', 'Abila Airport', 'Kalami Kafenion', "Frydos Autosupply n' More", 'Desafio Golf Course', "Octavio's Office Supplies", "Jack's Magical Beans", 'Stewart and Sons Fabrication', 'Hippokampos']

df = pandas.read_csv("data/cc_data_2.csv")


# I transformed it with this line:
#df.location = df.location.apply(lambda x: locs.index(x))

# There is a further field "hour" and minute 
df[['hour', "minute"]] = df.time.str.split(":", expand=True)
# Include location, price, last4ccnum and maybe hour
df[['day', 'month', 'year']] = df.date.str.split("/", expand=True)
df['agg_day'] = df['month'].astype(int).apply(lambda x: x*31) + df['day'].astype(int)

df['minutes'] = df['hour'].astype(int).apply(lambda x: x*60) \
                + df['minute'].astype(int)
df = df.drop(labels=['timestamp', 'location', 'time', 'hour', 'minute', 'day', 'month', 'year', 'date'], axis=1)
print(df)
pca = PCA(n_components=4)
cc_pca = pca.fit_transform(df)
pc_df = pandas.DataFrame(data=cc_pca, columns=['PC1', 'PC2', 'PC3', 'PC4'])
plt.figure(figsize=(12, 10))
print(cc_pca)
sns.scatterplot(x="PC1", y="PC2", data=pc_df, s=100)
plt.show()
