## Session 4 - Section 1
## First visualizations using pandas
# We have already introduced pandas in session 3, section 2.
# Besides data manipulation and cleaning we can also visualize data using
# pandas dataframes:
import pandas as pd

# for simple random value handling
import numpy as np
# we need a further import - mathplotlib the mother of all vis libs in python
import matplotlib.pyplot as plt

plt.close("all")

# random series data
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
print(ts)

ts = ts.cumsum()

ts.plot()

# if you are not in a yupiter notebook you have to explicitly show the plot via:
plt.show()


# let's look again at the example from last session:
cc_df = pd.read_csv("data/cc_data.csv")
print(cc_df)

# price by location is:
df = cc_df.groupby("location").sum("price")

# the sum of the last 4 ccnum doesn't make sense -> remove
del df["last4ccnum"]

# plot
df.plot()
plt.show()

# use barchart plot -> makes more sense for this case:
df.plot.bar()
plt.show()


## Seaborn
# Seaborn is a Python data visualization library based on matplotlib

# also needs pandas, and mathplotlib (maybe numpy)
import seaborn as sns

# only look at Katerina's Cafe
cc_df = cc_df.query("location == \"Katerina's Cafe\"")
sns.relplot(x=cc_df.date, y=cc_df.price, data=cc_df)
# again we need to tell pyhton to explicitly show the vis
plt.show()

sns.relplot(x=cc_df.timestamp, y=cc_df.price, data=cc_df, kind="line")
plt.show()


## Plotly
# supports dash - package for easy dashboard creation + easy rendering to svg, ..

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'svg' Renderer"
)
fig.show(renderer="svg")


