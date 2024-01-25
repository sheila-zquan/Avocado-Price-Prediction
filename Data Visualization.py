#Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime as dt
import seaborn as sns


# load data
avocado = pd.read_csv('/Users/sheila/Desktop/Spring2023/CS105/project/data/New_Avocado_Price.csv')

av1 = avocado.copy(deep = True)
av1['Date'] = pd.to_datetime(av1['Date'])
av1.set_index('Date',inplace = True)
av1.head()

#
sns.distplot(avocado['AveragePrice']);
plt.title('Average Price Distribution')

#
fig, ax = plt.subplots()
sns.lineplot(x = 'Date' ,y = 'Total Volume',data = av1);
plt.title('Change of Total Volume Over Time')

#
fig, ax = plt.subplots()
sns.lineplot(x = 'Date' ,y = 'AveragePrice',data = av1);
plt.title('Change of Average Price Over Time')

#combine
fig, ax1 = plt.subplots(figsize=(10, 5))
# plot Total Volume
sns.lineplot(x='Date', y='Total Volume', data=av1, ax=ax1, color='green')
ax1.set_ylabel('Total Volume (green)')

# create second axis
ax2 = ax1.twinx()

# plot Average Price
sns.lineplot(x='Date', y='AveragePrice', data=av1, ax=ax2, color='red')
ax2.set_ylabel('Average Price (red)', rotation=-90, labelpad=15)

plt.title('Change of Total Volume and Average Price Over Time')


plt.show()


def do_regression(df, independent, dependent):
    '''
    perform an OLS regression of the column identified by dependent 
    as a function of the column identified by independent.
    '''
        
    #define the variable for linear equation:
    X = df[independent]
    Y = df[dependent]
    
    #conduct a model summary:
    model = sm.OLS(Y,X).fit()
    print(model.summary())
    
    #create the scatter plot and show:
    plt.scatter(X, Y)
    
    #label the X and Y:
    plt.xlabel(independent, fontsize = 15)
    plt.ylabel(dependent, fontsize = 15)
        
    #show the scatter plot as result:
    plt.show()


if __name__ == '__main__':
    
    
    filename = 'avocado_organic.csv'

    # read the data, set up index
    df = pd.read_csv(filename)
    df.index = df["region"]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date']=df['Date'].map(dt.datetime.toordinal)
   


    # do_regression(df.loc["LasVegas"], 'AveragePrice', 'Total Volume')
    do_regression(df.loc["Boston"], 'AveragePrice', 'Total Volume')