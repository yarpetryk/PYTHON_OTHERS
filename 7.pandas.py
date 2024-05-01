
import pandas as pd
my_pandas=pd.read_csv('../../country_full_1.csv')
my_pandas.set_index(['name'],inplace=True)
print(my_pandas.head())
print(my_pandas.tail())
print(my_pandas.info())
print(my_pandas.shape)
print(my_pandas.isnull())
print(my_pandas.isnull().sum())
my_pandas.fillna('---',inplace=True)
print(my_pandas.head())
print(my_pandas.describe())
print(my_pandas['region'].value_counts())
#-------------------------------------------------------------------------------------------
print(my_pandas.iloc[2:5])
print(my_pandas.loc['Afghanistan':'Albania'])
#-----------------------------------------------------------------------------------------
print(my_pandas['country-code'].head())
print((my_pandas['country-code']==4).head())
print((my_pandas[my_pandas['country-code']==8]).head())
print((my_pandas[my_pandas['country-code'].isin([4,8])]).head())
print((my_pandas[my_pandas['country-code'].between(3,10)]).head())
#-------------------------------------------------------------------------------------------
def code(x):
    if x>5:
        return 'good'
    else:
        return 'bad'

my_pandas['new_row']=my_pandas['country-code'].apply(code)
print(my_pandas.head())

my_pandas['new_row_1']=my_pandas['country-code'].apply(lambda x: 'very good' if x>7 else 'very bad')
print(my_pandas.head())
#---------------------------------------------------------------------------------------------------
print(my_pandas.sort_values(by='region').head())
my_pandas_1=my_pandas.copy()
my_pandas_1.drop_duplicates(inplace=True, keep=False)
print(my_pandas.shape)
print(my_pandas_1.shape)

my_pandas_2=my_pandas.append(my_pandas)
print(my_pandas_2.shape)
my_pandas_2.drop_duplicates(inplace=True, keep=False)
print(my_pandas.shape)
print(my_pandas_2.shape)
