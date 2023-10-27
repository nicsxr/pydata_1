import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('survey_results_public.csv')

# თითოეული ასაკის ჯგუფის YearsCode საშუალო.
# ვაჯგუფებთ Age და YearsCode და numpy-ით ვიღებთ საშუალოს თითოეულ ასაკის ჯგუფზე
age_groups = df.groupby('Age')['YearsCode'].apply(lambda x: np.mean(pd.to_numeric(x, errors='coerce')))

ages = age_groups.index
average_years_code = age_groups.values

# line chart
plt.figure(figsize=(10, 6))
plt.plot(ages, average_years_code, marker='o', linestyle='-')
plt.title('Average YearsCode by Age')
plt.xlabel('Age')
plt.ylabel('Average YearsCode')
# plt.xticks(rotation=45)  

# Display the chart
plt.tight_layout()
plt.grid(True)
plt.show()