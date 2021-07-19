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

# we can sort

