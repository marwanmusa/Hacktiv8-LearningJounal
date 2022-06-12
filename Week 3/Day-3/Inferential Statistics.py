# -*- coding: utf-8 -*-
# Day 3 AM - Inferential Statistics
"""

import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)

"""## Resampling

Resampling in statistics means to repeatedly sample values from observed data, with a general goal of assessing random variability in a statistic. To understand what resampling is, let we look at the housing price in Amsterdam data distribution (histogram) below.
"""

house_price = pd.read_csv('https://raw.githubusercontent.com/fahmimnalfrzki/Additional-Materials/main/HousingPrices-Amsterdam-August-2021.csv')
house_price.head()

sns.displot(house_price.Price, kde=True, label='Housing Price in Amsterdam')

fig,ax = plt.subplots(ncols=4, figsize = (18,4))
for i in range(4):
  house_price.Price.sample(400).plot(kind='hist',bins=20,ax=ax[i])
  ax[i].set_title('Sample #{}'.format(i+1))

"""We take 100 samples randomly from the housing price data and we did it 4 times. The visualization show that their distribution look the same. It happend simply because of randomness.

## Implementation to Marketing Campaign Analysis

In this lesson, we will learn about hypothesis testing and how to implement it to a daily business case such as online retail. We will use the data from ML UCI dataset https://archive.ics.uci.edu/ml/datasets/online+retail.
"""

data = pd.read_excel('https://github.com/fahmimnalfrzki/Additional-Materials/blob/main/online_retail_data.xlsx?raw=true').drop(columns='Unnamed: 0').sort_values('InvoiceDate',ascending=True).reset_index(drop=True)
data

data['StockCode'].value_counts()

"""### Single Sample Hypothesis Testing

Let we play a role. Suppose that during the last five years, our daily income is \$500 on average and during the last a year, we reach \$580 a day on average. Is it means that we're improved significantly?
"""

data['income'] = data['Quantity']*data['UnitPrice']
data['date'] = data['InvoiceDate'].dt.date
daily_income = data[['date','income']].groupby('date').sum()
print('Average Income a Day for the last a year: ${}'.format(np.round(daily_income['income'].mean())))

"""To check whether our sales is significantly increase or not, we will perform the single sample one sided and set the significance level of 0.05. We use this method since we only test a variable and compare the sample (last a year data) and the population (we assume it is the last five years data).

Our hypothesis on this case:

**H0: μ <= \$500**

**H1: μ > \$500**
"""

daily_income

t_stat,p_val = stats.ttest_1samp(daily_income.income, 500)
print('P-value:',p_val/2) #The p-value divided by 2 since the output is two-sided p-value
print('t-statistics:',t_stat)

daily_income_pop = np.random.normal(daily_income.income.mean(), daily_income.income.std(), 10000)

ci = stats.norm.interval(0.90, daily_income.income.mean(), daily_income.income.std())

plt.figure(figsize=(16,5))
sns.distplot(daily_income_pop, label='Daily Income (Population)', color='blue')
plt.axvline(daily_income.income.mean(), color='red', linewidth=2, label='Daily Income (Mean)')
plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(daily_income_pop.mean() + t_stat*daily_income_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.legend()

"""**Since our p-value is less than `0.05`, so we reject the null hypothesis** and we can conclude that, our sales for the last a year is improved than the last five years. 

*Note: Variable `t-statistics` refers to how far the alternative hypothesis from null hypothesis away.*

### One Sample Two Tailed

Our hypothesis on this case:

**H0: μ =\$500**

**H1: μ != \$500**
"""

t_stat,p_val = stats.ttest_1samp(daily_income.income, 500)
print('P-value:',p_val)
print('t-statistics:',t_stat)

daily_income_pop = np.random.normal(daily_income.income.mean(), daily_income.income.std(), 10000)

ci = stats.norm.interval(0.95, daily_income.income.mean(), daily_income.income.std())

plt.figure(figsize=(16,5))
sns.distplot(daily_income_pop, label='Daily Income (Population)', color='blue')
plt.axvline(daily_income.income.mean(), color='red', linewidth=2, label='Daily Income (Mean)')

plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')

plt.axvline(daily_income_pop.mean() + t_stat*daily_income_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.axvline(daily_income_pop.mean() - t_stat*daily_income_pop.std(), color='black', linestyle='dashed', linewidth=2)
plt.legend()

"""### Two Samples Independent Two Tailed Hypothesis Testing

Now, we want to check, whether daily average of sales of two countries are significantly different or not using two samples independent two tailed test. We will pick sample of France and Germany.
"""

daily_france = data[data['Country']=='France'][['date','income']].groupby('date').sum()
daily_germany = data[data['Country']=='Germany'][['date','income']].groupby('date').sum()

print('Average sales of France a day: ${}'.format(np.round(daily_france.income.mean())))
print('Average sales of Germany a day: ${}'.format(np.round(daily_germany.income.mean())))

"""Our hypothesis on this case:

**H0: μ_france = μ_germany**

**H1: μ_france != μ_germany**
"""

t_stat, p_val = stats.ttest_ind(daily_france,daily_germany)
print('P-value:',p_val[0]) #the p-value isn't divided by 2 since the output is two-sided p-value
print('t-statistics:',t_stat[0])

france_pop = np.random.normal(daily_france.income.mean(),daily_france.income.std(),10000)
germany_pop = np.random.normal(daily_germany.income.mean(),daily_germany.income.std(),10000)

ci = stats.norm.interval(0.95, daily_france.income.mean(), daily_france.income.std())
plt.figure(figsize=(16,5))
sns.distplot(france_pop, label='France Average Sales a Day *Pop',color='blue')
sns.distplot(germany_pop, label='Germany Average Sales a Day *Pop',color='red')

plt.axvline(daily_france.income.mean(), color='blue', linewidth=2, label='France mean')
plt.axvline(daily_germany.income.mean(), color='red',  linewidth=2, label='Germany mean')

plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

plt.axvline(france_pop.mean()+t_stat[0]*france_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
plt.axvline(france_pop.mean()-t_stat[0]*france_pop.std(), color='black', linestyle='dashed', linewidth=2)

plt.legend()

"""Based on the result above, we can conclude that **we fail to reject the null hypothesis** which between the france and germany are not significantly different in terms of average sales per day.

## ANOVA

ANOVA is similar to the t-test. It used for testing whether more than two variables are significantly different or not. So, we will test whether the mean of daily sales of IEV,N8U, and U5F are significantly different or not.
"""

scanner_data = pd.read_csv('https://raw.githubusercontent.com/fahmimnalfrzki/Additional-Materials/main/scanner_data.csv')
scanner_data

scanner_data.groupby('Date').sum()

IEV_quantity = scanner_data[scanner_data.SKU_Category == 'IEV'].groupby('Date').sum()['Quantity']
N8U_quantity = scanner_data[scanner_data.SKU_Category == 'N8U'].groupby('Date').sum()['Quantity']
U5F_quantity = scanner_data[scanner_data.SKU_Category == 'U5F'].groupby('Date').sum()['Quantity']

print("Daily Average of IEV",IEV_quantity.mean())
print("Daily Average of N8U",N8U_quantity.mean())
print("Daily Average of U5F",U5F_quantity.mean())

"""It seems that they are significantly different since `N8U` average is `33` and the rest is `22."""

f_stat,p_value = stats.f_oneway(IEV_quantity, N8U_quantity, U5F_quantity)
print('P-value:',p_value)

"""**Since the p-value is below 0.05, then we reject the Null Hypothesis.** We conclude that the difference of IEV, N8U, and U5F is statistically significant.

## Paired Test
**Implementation on A/B Testing**

We're dealing with the marketing division of game developer company to analyze which game version that tend to give more retention rate? Is it correct that we upgrade our game from gate 30 to gate 40 version? (Data from https://www.kaggle.com/yufengsui/mobile-games-ab-testing) We will use retention_1 data which capture the information that did the player come back and play 1 day after installing.
"""

cookie_cats = pd.read_csv('https://raw.githubusercontent.com/fahmimnalfrzki/Additional-Materials/main/cookie_cats.csv')
cookie_cats

gate_30 = cookie_cats[cookie_cats['version']=='gate_30']['retention_1'].replace({True:1,False:0})
gate_40 = cookie_cats[cookie_cats['version']=='gate_40']['retention_1'].replace({True:1,False:0})

print('Retention rate of gate 30 version:',gate_30.sum()/gate_30.count())
print('Retention rate of gate 40 version:',gate_40.sum()/gate_40.count())

gate_30

gate_40

"""The retention rate between those versions is slightly different. Is the difference truly the same or because of chance?

To make sure of our result, we will check using paired test two sided.

Our hypothesis on this case:

**H0: μ_gate30 = μ_gate40**

**H1: μ_gate30 != μ_gate40**
"""

t_stat,p_val = stats.ttest_rel(gate_30.sample(40000),gate_40.sample(40000)) #we take 40000 sample of each data to make the size the same.
print('P-value:',p_val)

"""**Since the p-value is more than 0.05, we conclude that we fail to reject the Null Hypothesis** which means between gate 30 and 40 version is the same. We safely upgrade our game into gate 40 version.

## Chi-Square Test

Chi-square test is used for testing of independence between two categorical data. Since statistics handling the numerical data, we need to calculate the frequency of each variable and presented by a contingency table.
"""

chi_df=pd.read_csv('https://raw.githubusercontent.com/yug95/MachineLearning/master/Hypothesis%20testing/chi-test.csv')
chi_df

contingency_table=pd.crosstab(chi_df["Gender"],chi_df["Like Shopping?"])
contingency_table

stat, p, dof, expected = stats.chi2_contingency(contingency_table)
print('p=%.3f' % (p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')