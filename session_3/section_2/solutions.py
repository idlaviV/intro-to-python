import pandas as pd

#------------------------------------------------------------------------------#
# (1)
# Read the credit card data

df = pd.read_csv("data/cc_data.csv")
print(df)

# convert the price colum to a float, last4ccnum to an int
df.price = df.price.astype(float)
df.last4ccnum = df.last4ccnum.astype(int)


# split the timestamp into date and time
df[['date', "time"]] = df.timestamp.str.split(" ", expand=True)
print(df)

# round the price in every row (however you like)
df.price = df.price.apply(lambda x: round(x))
print(df)

#------------------------------------------------------------------------------#
# (2)
# Determine where the most money got spent (at which location)
# use groupby

print(df.groupby("location").sum("price"))


# Determine the mean money spent at every location
# the mean of the last 4 ccnums obv. doesn't make sense:D
print(df.groupby("location").mean("price"))