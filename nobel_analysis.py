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

print(check_df(df))

top_gender = df["sex"].value_counts().idxmax()
print(f"The most commonly awarded gender is {top_gender}")

top_country = df["birth_country"].value_counts().idxmax()
print(f"The most commonly awarded country is {top_country}")

# Step 2: Identify the decade with the highest ratio of US-born winners

df["us_born_winners"] = df["birth_country"] == "United States of America"
df["decade_years"] = (np.floor(df["year"]/10) * 10).astype(int)
usa_winners_proportion = df.groupby("decade_years", as_index = False)["us_born_winners"].mean()
max_decade_usa = usa_winners_proportion[usa_winners_proportion["us_born_winners"] == usa_winners_proportion["us_born_winners"].max()]["decade_years"].values[0]

sns.relplot(x = "decade_years", y = "us_born_winners", data = usa_winners_proportion, kind = "line")
#plt.show()

# Step 3: Find the decade and category with the highest proportion of female laureates

df["Female"] = df["sex"] == "Female"
female_proportions = df.groupby(["decade_years", "category"], as_index = False)["Female"].mean()
max_female_category = female_proportions[female_proportions["Female"] == female_proportions["Female"].max()][["decade_years", "category"]]
my_dict = {max_female_category["decade_years"].values[0] : max_female_category["category"].values[0]}

# Step 4: Find first woman to win a Nobel Prize

women_nobel = df[df["Female"] == True]
min_year_women = women_nobel[women_nobel["year"] == women_nobel["year"].min()]
print(f"{women_nobel["full_name"].values[0]} won the first Nobel in {min_year_women["year"].values[0]} in the {min_year_women["category"].values[0]} category")

# Step 5: Determine repeat winners

counts = df["full_name"].value_counts()
repeat_lists = list(counts[counts >= 2].index)
print(f"The repeat winners are {repeat_lists}")

# Bonus 1: On which century did the US Nobel winners have more trophys?

us_borns = df[df["birth_country"] == "United States of America"]
twentieth_century_us = df[(df["year"] >= 1901) & (df["year"] <= 2000) & (df["birth_country"] == "United States of America")]
ratio_twentieth = len(twentieth_century_us) / len(df)
twentyfirst_century_us = df[(df["year"] >= 2001) & (df["birth_country"] == "United States of America")]
ratio_twentyfirst = len(twentyfirst_century_us) / len(df)

if ratio_twentieth > ratio_twentyfirst:
    print("The century with the highest ratio is 20th Century with a ratio of:", ratio_twentieth)
else:
    print("The century with the highest ratio is 21st Century with a ratio of:", ratio_twentyfirst)

"""
Comments, Findings:

 1.Big Picture (df_check):
    * DF shows the nobel prize winner's information ranging from 1901 to 2023
    * DF consists of 18 columns and the most importants are: year, category, birth_country, sex.

 2. The most common gender is: Male

 3. The most common birth country is: USA

 4. The decade with the highest ratio of US-born winners is: 2000

 5. The decade with the highest proportion of female laureates is: 2020

 6. The category with the highest proportion of female laureates is: Literature

 7. The first woman to win a Nobel Prize is: Marie Cury in Physics

 8. The repeat winners are: 'Comité international de la Croix Rouge (International Committee of the Red Cross)', 'Linus Carl Pauling', 'John Bardeen', 'Frederick Sanger', 'Marie Curie, née Sklodowska', 'Office of the United Nations High Commissioner for Refugees (UNHCR)'

"""
