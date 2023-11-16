import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

claim_data = pd.read_csv('claims.csv')
cust_data = pd.read_csv('cust_demographics.csv')
claim_cust = pd.merge(left = claim_data,right = cust_data,left_on = 'customer_id',right_on = 'CUST_ID',how = 'inner',indicator=True)
a=claim_cust = claim_cust.drop(columns='_merge')
print(cust_data)
#claim_cust.dropna(inplace=True)



from pandas import DataFrame
#Data Audit

d=claim_cust.dtypes[claim_cust.dtypes!='object'].index.values
claim_cust[d]=claim_cust[d].astype('float64')
mean=DataFrame({'mean':claim_cust[d].mean()})
std_dev=DataFrame({'std_dev':claim_cust[d].std()})
missing= DataFrame({'missing':claim_cust[d].isnull().sum()})
minimum=DataFrame({'min':claim_cust[d].min()})
maximum=DataFrame({'max':claim_cust[d].max()})
DA=pd.concat([mean,std_dev,missing,minimum,maximum],axis=1,sort = False)


c=claim_cust.dtypes[claim_cust.dtypes=='object'].index.values
Mean=DataFrame({'mean':np.repeat('Not Applicable',len(c))},index=c)
Std_Dev=DataFrame({'std_dev':np.repeat('Not Applicable',len(c))},index=c)
Missing=DataFrame({'missing':claim_cust[c].isnull().sum()})
Minimum=DataFrame({'min':np.repeat('Not Applicable',len(c))},index=c)
Maximum=DataFrame({'max':np.repeat('Not Applicable',len(c))},index=c)
Da=pd.concat([Mean,Std_Dev,Missing,Minimum,Maximum],axis =1,sort = False)
Dq = pd.concat([DA,Da])
print(Dq)'''

'''Dq = pd.concat([DA],[Da])
Dq.to_csv('DataAudit.csv')
dq = pd.read_csv("DataAudit.csv")
dq.rename(columns = {'Unnamed: 0':''})
print(Dq,dq)


'''#3
claim_cust['claim_amount'] = claim_cust['claim_amount'].astype(str)
claim_cust['claim_amount'] = claim_cust['claim_amount'].str.replace('$','')
claim_cust['claim_amount'] = pd.to_numeric(claim_cust['claim_amount'],errors="coerce")
print(claim_cust.iloc[::,7])'''


'''#4
claim_cust['Flag'] = np.where(claim_cust.police_report == 'Unknown',0,1)
print(claim_cust.head())'''


'''#5
recent_obs = claim_cust.drop_duplicates(subset = 'CUST_ID',keep = 'last')
print(recent_obs.head())'''
 
'''#6
claim_cust["claim_amount"]=claim_cust["claim_amount"].str.replace('$','')
claim_cust['claim_amount'].fillna(0 , inplace=True)
claim_cust['claim_amount']=pd.to_numeric(claim_cust['claim_amount'], errors='coerce')

mean=claim_cust["claim_amount"].mean()
print("mean is:" ,mean)
claim_cust['claim_amount']= claim_cust['claim_amount'].replace(0,mean)
print(claim_cust.loc[24,"claim_amount"])
print(claim_cust.head(20))'''


#7
year_today = pd.to_datetime('today').year
year_dob = pd.DatetimeIndex(claim_cust['DateOfBirth']).year          
year1 = year_dob-100                                               
year2 = year_today - year1
year_final = year_today - year_dob
claim_cust['age'] = (np.where(year_dob > year_today,year2,year_final))
claim_cust.loc[(claim_cust.age < 18),'AgeGroup'] = 'Children'
claim_cust.loc[(claim_cust.age >=18) & (claim_cust.age <30),'AgeGroup'] = 'Youth'
claim_cust.loc[(claim_cust.age >=30) & (claim_cust.age <60),'AgeGroup'] = 'Adult'
claim_cust.loc[(claim_cust.age >=60),'AgeGroup'] = 'Senior'
print(claim_cust.head(30))


#8
print(claim_cust.groupby(['Segment'])['claim_amount'].mean())


#9
print(claim_cust.groupby(['incident_cause'])['claim_amount'].sum())

#10
count_adults = claim_cust.loc[((claim_cust.State == 'TX') | (claim_cust.State == 'DE') | (claim_cust.State == 'AK')) & (claim_cust.incident_cause == 'Driver error') & (claim_cust.AgeGroup == 'Adult'),['AgeGroup']].count()
print(count_adults)

#11
claim = pd.pivot_table(claim_cust, index =['Segment'],columns ='gender',values ='claim_amount')
print(claim)

gf=claim.loc['Gold','Female']
gm=claim.loc['Gold','Male']
pf=claim.loc['Platinum','Female']
pm=claim.loc['Platinum','Male']
sf=claim.loc['Silver','Female']
sm=claim.loc['Silver','Male']

plt.pie([gf,pf,sf],labels=['Gold','Platinum','Silver'])
plt.title('Female')
plt.show()

plt.pie([gm,pm,sm],labels=['Gold','Platinum','Silver'])
plt.title('Male')
plt.show()


'''#12
driver_issue = claim_cust.loc[claim_cust['incident_cause'].isin(['Driver error','Other driver error'])]
gender_group = driver_issue.groupby(['gender'])['claim_amount'].sum()
gender_group.nlargest(1)
gender_group.plot(kind = 'bar',title='driver error')
plt.show()

issue1 = claim_cust.loc[claim_cust['fraudulent'] == 'Yes']
group_age = issue1.groupby(['AgeGroup'])['Total policy claims'].sum()
group_age.plot(kind = 'bar',title='Fraudulent policy claims')
plt.show()


#14
claim_cust['claim_date'] = pd.to_datetime(claim_cust['claim_date'])
claim_cust['Claim_date'] = claim_cust['claim_date'].dt.month
sns.set()
pd.pivot_table(claim_cust, index ='claim_type',columns = pd.DatetimeIndex(claim_cust['claim_date']).month,
               values="claim_amount").plot(kind='bar')
plt.ylabel('Total amount spent')
plt.show()'''