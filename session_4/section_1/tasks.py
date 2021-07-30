# ------------------------------------------------------------------------------#
# (1)
# Write min. 2 functions which handle the reading, processing and visualization 
# of a time series of transactions for one location (dependant on an argument)
# (you can use the sum, mean or median) for the transactions on one day.
import pandas as pd
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt


def visualize_mean_transactions_at_location_over_time(df, location):
    grouped_df = df.query(f'location == \"{location}\"')
    mean_price = grouped_df.groupby('date')['price'].mean()
    mean_price.plot()
    plt.show()


def visualize_sum_of_transactions_at_location_over_time(df, location):
    grouped_df = df.query(f'location == \"{location}\"')
    summed_price = grouped_df.groupby('date')['price'].sum()
    summed_price.plot()
    plt.show()


# reading a csv_file (credit card data from the VAST Mini Challange 2021)


# test your function(s) for <Coffee Cameleon> and <Brew've Been Served>
# plot("Coffee Cameleon")
# plot("Brew've Been Served")
def test_visualize_above():
    cc_df = pd.read_csv("data/cc_data_1.csv")
    visualize_mean_transactions_at_location_over_time(cc_df, 'Coffee Cameleon')
    visualize_sum_of_transactions_at_location_over_time(cc_df, 'Coffee Cameleon')
    visualize_mean_transactions_at_location_over_time(cc_df, 'Brew\'ve Been Served')
    visualize_sum_of_transactions_at_location_over_time(cc_df, 'Brew\'ve Been Served')


# test_visualize_above()

# (2) - optional
# Create a heatmap (https://seaborn.pydata.org/generated/seaborn.heatmap.html)
# using seaborn for every location (y) and every date (x) and the 
# sum of the price on the specific day (z).
# Hints: 1 - first build a list of dictionaries and convert it then to
# a df to visualize
# 2 - use iterrows in this way to iterate through a df:
#   for index, row in df.iterrows:
#       row.location


def heatmap_location_date(df):
    data_by_location = {}
    locs = df['location'].tolist()
    for loc in locs:
        ta_in_loc = df.query(f'location == \"{loc}\"')
        data_by_location[loc] = ta_in_loc.groupby('date').size()
    df_by_location = pd.DataFrame(data_by_location).fillna(0)
    sns.heatmap(df_by_location.transpose())
    pl.show()


def test_heatmap():
    cc_df = pd.read_csv("data/cc_data_1.csv")
    heatmap_location_date(cc_df)


test_heatmap()
