import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns

df = pd.read_csv('axisdata.csv')

print("\n*** Structure ***")
print(df.info())


lNSigTerms = ['id', 'name', 'desc']
lsRet = []
vColList = df.columns.to_list()
for vCol in vColList:
    bIsNotSig = False
    for vTerm in lNSigTerms:
        if vCol.lower().startswith(vTerm) or vCol.lower().endswith(vTerm): 
            bIsNotSig = True
    if bIsNotSig == False:
        lsRet.append(vCol) 
# store for future use
lSigCols = lsRet       
dfSigCols = df[lSigCols]
print("\n*** Significant Columns ***")
for vCol in lSigCols:
    print(vCol)



print("\n*** Histogram Plot ***")
for vCol in lSigCols:
    if (df[vCol].dtypes == 'object'): #and df[vCol].dtypes != 'float64' ):
        continue
    #print("Col",vCol)
    colValues = df[vCol].values
    plt.figure(figsize=(10,5))
    sns.distplot(colValues, bins=7, kde=False, color='b')
    plt.title('Column %s' % vCol)
    plt.ylabel(vCol)
    plt.xlabel('Bins')
    plt.show()
