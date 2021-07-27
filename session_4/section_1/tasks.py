#------------------------------------------------------------------------------#
# (1)
# Write min. 2 functions which handle the reading, processing and visualization 
# of a time series of transactions for one location (dependet on an argument) 
# (you can use the sum, mean or median) for the transactions on one day.


import pandas as pd
import matplotlib.pyplot as plt


def load_data(loc):
    df = pd.read_csv("data/cc_data.csv")
    df = df.query(f"location == \"{loc}\"")
    df = df.reset_index(drop = True)
    df = df.groupby("date").sum("price")
    return df[["price"]]


def plot(loc):
    df = load_data(loc)    
    df.plot()
    plt.show()


# test your function(s) for <Coffee Cameleon> and <Brew've Been Served>
# plot("Coffee Cameleon")
# plot("Brew've Been Served")


# (2) - optional
# Create a heatmap (https://seaborn.pydata.org/generated/seaborn.heatmap.html)
# using seaborn for every location (y) and every date (x) and the 
# sum of the price on the specific day (z).
# Hints: 1 - first build a list of dictionaires and convert it then to 
# a df to visualize
# 2 - use iterrows in this way to iterate through a df:
#   for index, row in df.iterrows:
#       row.location

import numpy as np
import seaborn as sns

cc_df = pd.read_csv("data/cc_data.csv")

def get_hm_data(df):
    locs = [*set(df.location)]
    dates = [*set(df.date)]
    print(dates)
    data = {}
    for loc in locs:
        loc_df = df.query(f"location == \"{loc}\"")
        loc_df = loc_df.groupby("date").sum("price")        
        del loc_df["last4ccnum"]
        for date in dates:            
            if date in loc_df.index:
                z_value = loc_df.loc[date].price
            else:
                z_value = 0
            if not loc in data:
                data[loc] = []
            data[loc].append(z_value)
    
    result_df = pd.DataFrame()
    for loc_key in data:
        result_df[loc_key] = data[loc_key]
    result_df.index = result_df.index
    return result_df
        

heatmap_df = get_hm_data(cc_df)
print(heatmap_df)

ax = sns.heatmap(heatmap_df)
plt.show()
        
        
        
        
        
