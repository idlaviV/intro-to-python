#------------------------------------------------------------------------------#
# (1)
# Read the credit card data
import pandas as pd
data = pd.read_csv("data/cc_data.csv")


# convert the price column to a float, last4ccnum to an int
data.price = data.price.astype(float)
data.last4ccnum = data.last4ccnum.astype(int)

# split the timestamp into date and time
data['date'] = data.timestamp.apply(lambda x: x.split()[0])
data['time'] = data.timestamp.apply(lambda x: x.split()[1])

# round the price in every row (however you like)
data['price'] = data['price'].apply(float.__round__)

#------------------------------------------------------------------------------#
# (2)
# Determine where the most money got spent (at which location)
# use groupby
gp_sum = data.groupby('location').sum('price')
maximum = gp_sum.sort_values('price', ascending=False).iloc[0]
print(f"Most money got spent at {maximum.name}: {maximum['price']}")


# Determine the mean money spent at every location
print("Mean money spent at:")
print(data.groupby('location')['price'].mean())