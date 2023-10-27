import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey_results_public.csv')

# რამდენჯერ მეორდება თითო მნიშვნელობა
value_counts = df['YearsCodePro'].value_counts()

# sort
value_counts = value_counts.sort_index()

# bar chart
plt.figure(figsize=(12, 6))
value_counts.plot(kind='bar', color='skyblue')
plt.title(f'Frequency of Values in the {'YearsCodePro'} Column')
plt.xlabel('YearsCodePro')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()