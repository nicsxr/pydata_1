import pandas as pd

df = pd.read_csv('survey_results_public.csv')

# 1.1 - გამოვიტანოთ მონაცემები სადაც YearsCode>10 && == Developer, back-end && country == United States of America
res_1 = df[(pd.to_numeric(df['YearsCode'], errors='coerce') > 10) & (df['DevType'] == 'Developer, back-end') & (df['Country'] == 'United States of America')]
print(res_1)


# 1.2 - ინდექსირება ResponseId-ზე
df.index = df['ResponseId'] # შევქმნათ ინდექსი
df.drop(['ResponseId'], axis=1) # წწავშალოთ დუბლიკატი იდ
df.set_index('ResponseId', inplace=True) # დავუნიშნოთ ინდექსი
print(df)


# 1.3 - მონაცემების გაფილტვრა ConvertedCompYearly და AIDevWantToWorkWith
condition1 = pd.to_numeric(df['ConvertedCompYearly']) >= 285000
condition2 = df['AIDevWantToWorkWith'] == 'GitHub Copilot'
filtered_df = df[condition1 & condition2]
print(filtered_df)


# 1.4 - mean, standard deviation, median, min, max
mean = df['CompTotal'].mean()
print("Mean:", mean)

std_dev = df['CompTotal'].std()
print("Standard Deviation:", std_dev)

median = df['CompTotal'].median()
print("Median:", median)

minimum = df['CompTotal'].min()
print("Minimum:", minimum)

maximum = df['CompTotal'].max()
print("Maximum:", maximum)