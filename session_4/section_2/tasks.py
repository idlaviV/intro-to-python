#------------------------------------------------------------------------------#
# (1)
# Apply UMAP or PCA to the cc_data - the location is encoded as an int
# index of the following list:
import pandas
locs = ['Carlyle Chemical Inc.', 'Nationwide Refinery', 'Daily Dealz', 'General Grocer', 'Roberts and Sons', "Frank's Fuel", "Shoppers' Delight", 'Ouzeri Elian', "Albert's Fine Clothing", 'Bean There Done That', 'Hallowed Grounds', "Katerina's Cafe", 'Ahaggo Museum', 'Kronos Pipe and Irrigation', 'Coffee Cameleon', "Guy's Gyros", 'U-Pump', 'Abila Scrapyard', 'Maximum Iron and Steel', 'Abila Zacharo', 'Chostus Hotel', 'Gelatogalore', 'Coffee Shack', 'Brewed Awakenings', "Brew've Been Served", 'Kronos Mart', 'Abila Airport', 'Kalami Kafenion', "Frydos Autosupply n' More", 'Desafio Golf Course', "Octavio's Office Supplies", "Jack's Magical Beans", 'Stewart and Sons Fabrication', 'Hippokampos']

df = pandas.read_csv("data/cc_data_2.csv")


# I transformed it with this line:
#df.location = df.location.apply(lambda x: locs.index(x))

# There is a further field "hour" and minute 
df[['hour', "minute"]] = df.time.str.split(":", expand=True)
# Include location, price, last4ccnum and maybe hour
print(df)

df['minutes'] = df['hour'].astype(int).apply(lambda x: x*60) \
                + df['minute'].astype(int)

print(df)
