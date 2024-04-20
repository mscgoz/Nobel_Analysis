import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the dataset and find the most common gender and birth country

df = pd.read_csv("nobel.csv")

def check_df(dataframe):
    print("########################################################## HEAD #################################################################")
    print(df.head())
    print("########################################################## TAIL #################################################################")
    print(df.tail())
    print("########################################################## DESCRIBE #################################################################")
    print(df.describe().T)
    print("########################################################## INFO #################################################################")
    print(df.info())
    print("########################################################## NAs #################################################################")
    print(df.isnull().sum())
    print("########################################################## Variable Types #################################################################")
    print(df.dtypes)

# print(check_df(df))


top_gender = df["sex"].value_counts().idxmax()
# print(f"The most commonly awarded gender is {top_gender}")

top_country = df["birth_country"].value_counts().idxmax()
# print(f"The most commonly awarded country is {top_country}")


# Step 2: Identify the decade with the highest ratio of US-born winners

"""
Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
Store this as an integer called max_decade_usa.
"""

df["us_born_winners"] = df["birth_country"] == "United States of America"
df["decade_years"] = (np.floor(df["year"]/10) * 10).astype(int)
usa_winners_proportion = df.groupby("decade_years", as_index = False)["us_born_winners"].mean()


max_decade_usa = usa_winners_proportion[usa_winners_proportion["us_born_winners"] == usa_winners_proportion["us_born_winners"].max()]["decade_years"].values[0]
print(max_decade_usa)

sns.relplot(x = "decade_years", y = "us_born_winners", data = usa_winners_proportion, kind = "line")
plt.show()