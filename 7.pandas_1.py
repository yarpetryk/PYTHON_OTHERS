import pandas as pd
import numpy as np
left=pd.read_csv('../../left.csv')
right=pd.read_csv('../../right.csv')
left.set_index(['name'],inplace=True)
right.set_index(['name'],inplace=True)

print(left)
print(right)
#CONCAT-----------------------------------------------------------------
pieces=[left[:3],left[3:6]]
my_concat=pd.concat(pieces)
print(my_concat)
my_union=pd.concat([left, right])
print(my_union)
#MERGE-----------------------------------------------------------------
my_merge=pd.merge(left,right,on='id', how='left')
print(my_merge)
left.reset_index(inplace=True)
right.reset_index(inplace=True)
my_merge_1=pd.merge(left,right,on='id', how='left')
print(my_merge_1)
#GROUP BY--------------------------------------------------------------
my_group=left.groupby('sex').sum()
print(my_group)
my_group_1=left.groupby(['sex','region']).sum()
print(my_group_1)
#PIVOT TABLE--------------------------------------------------------------
my_pivot_table=pd.pivot_table(left, values='salary', index=['region'],columns=['sex'], aggfunc=np.sum)
print(my_pivot_table)
