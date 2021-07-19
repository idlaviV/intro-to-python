## Packages
# CSV files can also be read the way we discussed in section 1 - 
# the easiest way however is using the pandas package.
# To install a package type: `pip install <package-name>`:
# > pip install pandas
# for notebooks use: !pip install pandas
# if you still/as well have python2 installed you might have to type pip3
# your output for `pip --version` should look something like this:
# > pip 21.1.2 from /home/linuxbrew/.linuxbrew/Cellar/python@3.9/3.9.1_1/lib/python3.9/site-packages/pip (python 3.9)
# you can find packages for every purpose - some are better documented than others

# pyhton comes with a few built-in packages: e.g.:
import time
print(time.time())

import random
print(random.randint(0, 100))

# when working with csv files (or json) one package is very prominent and 
# comes with a lot of functionality:
# pandas

#!pip install pandas

# it's common to abbr. pandas as pd
import pandas as pd


# reading a csv_file (credit card data from the VAST Mini Challange 2021)
cc_df = pd.read_csv("data/cc_data.csv")

# csv files may have different seperators:
# df = pd.read_csv("data/cc_data.csv", sep=";")

# everything in pandas is a dataframe (df) - basically a table
print(cc_df)

# show / return the first n lines
print(cc_df.head(5)) 

# show / return the last n lines
print(cc_df.tail(5)) 

# we can also create our own dataframe:
df_data = [
    {"name": "Tilman", "age": 22, "blob": 123},
    {"name": "Vincent", "age": 26, "blob": "413"},
    {"name": "Lavia", "age": 19, "blob": "eq3e"},
    {"name": "Sven", "age": "34", "blob": ""},
    {"name": "Jens", "age": 34, "blob": 18321412},
]

df = pd.DataFrame(df_data)
print(df)

# print out column names:

# we can delete columns:
del df["blob"]

# Alternatively we can select only the ones we need/want:

df = df[["name", "age"]]



# accessing columns:
print(df.name)

# accessing rows:
print(df.iloc[0])
print(df.iloc[2])

# accessing cells:
print(df.iloc[0]["name"])
print(df.name.iloc[0])
print(df.loc[0, "name"])

# We can slice rows similar to list slicing:
print(df[2:4])


# extending/appending data:
df2 = pd.DataFrame([
    {"name": "Marie", "age": 13, "blob": ""},
    {"name": "Roxanne", "age": 22, "blob": "lights"}
])
df = df.append(df2)

# drop an entire row:
df.drop(0)

# df.drop(-1) does not work

# convert types

df.age = df.age.astype(int)
print(df)


# pandas built in methods for easy stats / exploration:
print(df.age.sum())
print(df.age.mean())

# more methods are:
# .count()      Number of non-null observations
# .sum()        Sum of values
# .mean() 	    Mean of Values
# .median() 	Median of Values
# .mode() 	    Mode of values
# .std() 	    Standard Deviation of the Values
# .min()        Minimum Value
# .max()        Maximum Value
# .abs()        Absolute Value
# .prod()       Product of Values
# .cumsum()     Cumulative Sum
# .cumprod()    Cumulative Product


# pandas has some methods which help to get a first idea of the data:
cc_df.describe()
print(cc_df.T)


# many more functionality .... 
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html
# Simply search for what you want to do and read doc/reference
# -> e.g. sort dataframe


