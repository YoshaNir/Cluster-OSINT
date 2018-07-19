# open raw data source file (IPs)
import numpy as np
import pandas as pd
import numpy as np
import csv

data = pd.read_csv('MaliciousIPs.csv')
print(data.shape)
data.head()
data.desctibe()
data[['octet1','octet2','octet3','octet4']] = data['IP'].str.split('.',expand=True)
data[‘octet1’].value_counts()



reader = csv.reader(open('assignedIPv4blocks.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v


data[‘owner'] = data['octet1'].map(d)

data['owner'].value_counts(normalize=True)

data[['octet1','octet2']] = data[['octet1','octet2']].apply(pd.to_numeric)

data['decimal'] = data['octet1']*256+data['octet2']


reader2 = csv.reader(open('countryIPv4blocks.csv', 'r'))
c = {}
for row in reader2:
   k, v = row
   c[k] = v


data['decimal'] = data['decimal'].apply(str)

data['country'] = data['decimal'].map(c)

data['country'].value_counts()



