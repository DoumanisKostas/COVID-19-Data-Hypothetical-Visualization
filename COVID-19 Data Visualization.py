import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create hypothetical data
dates = pd.date_range(start="2019-12-01", end="2022-12-31")
num_days = len(dates)
countries = ['Greece', 'Italy', 'Spain', 'Germany', 'France', 'China']

data = {
    'date': np.tile(dates, len(countries)),
    'country': np.repeat(countries, num_days),
    'confirmed': np.random.randint(0, 1000000, num_days * len(countries)),
    'deaths': np.random.randint(0, 50000, num_days * len(countries)),
    'recovered': np.random.randint(0, 900000, num_days * len(countries))
}

df = pd.DataFrame(data)

# Group data by month
df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
df_monthly = df.groupby(['month', 'country']).agg({'confirmed': 'sum'}).reset_index()

# Create two subplots
fig, axes = plt.subplots(2, 1, figsize=(14, 16), sharex=True)

# First plot: Confirmed cases for 'Greece', 'Italy', 'Spain'
countries_group1 = ['Greece', 'Italy', 'Spain']
sns.barplot(data=df_monthly[df_monthly['country'].isin(countries_group1)], x='month', y='confirmed', hue='country', palette='tab10', ax=axes[0])
axes[0].set_title('Monthly COVID-19 Confirmed Cases for Greece, Italy, Spain')
axes[0].set_ylabel('Confirmed Cases')
axes[0].legend(title='Country')
axes[0].tick_params(axis='x', rotation=45, labelsize=10)

# Second plot: Confirmed cases for 'Germany', 'France', 'China'
countries_group2 = ['Germany', 'France', 'China']
sns.barplot(data=df_monthly[df_monthly['country'].isin(countries_group2)], x='month', y='confirmed', hue='country', palette='tab10', ax=axes[1])
axes[1].set_title('Monthly COVID-19 Confirmed Cases for Germany, France, China')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Confirmed Cases')
axes[1].tick_params(axis='x', rotation=45, labelsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()




