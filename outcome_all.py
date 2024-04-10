# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:27:55 2023

@author: hgathuri
"""

####Outcome at discharge per hospital – Alive, dead, referred.

s=synd_df2.groupby('hospital')['date_of_entry'].count().reset_index()
s=s.rename(columns={'hospital': 'Hospital','date_of_entry':'Patients Discharged'})

outcome = synd_df2['outcome'].value_counts(dropna=False)
#outcome.to_csv('outcome.csv')

status_at_discharge = synd_df2['status_at_discharge'].value_counts(dropna=False)	
#status_at_discharge.to_csv('status_at_discharge.csv')


######### Create a bar graph with these columns for each hospital.
### Alive, Dead, Referred

a_df = synd_df2[(synd_df2['outcome'] == 'Alive') & (synd_df2['status_at_discharge'] != 'Referred')]
d_df = synd_df2[synd_df2['outcome'] == 'Dead']
r_df = synd_df2[(synd_df2['outcome'] == 'Alive') & (synd_df2['status_at_discharge'] == 'Referred')]


d=d_df.groupby('hospital')['date_of_entry'].count()
r=r_df.groupby('hospital')['record_id'].count()
a=a_df.groupby('hospital')['date_of_entry'].count()
s=s.set_index('Hospital')

disch1 = pd.merge(s,a,left_index=True,right_index=True,how='outer')
disch2 = pd.merge(disch1,d,left_index=True,right_index=True,how='outer')
disch3 = pd.merge(disch2,r,left_index=True,right_index=True,how='outer').fillna(0)
disch4 = disch3.rename(columns={'date_of_entry_y':'Dead','record_id':'Referred','date_of_entry_x':'Alive'})

##Plot
ax = disch4[['Patients Discharged', 'Alive', 'Dead']].plot(kind='bar',figsize=(22,12),color=['#ff7f0e', '#2ca02c', '#d62728', '#1f77b4' ])

#add overall title
ax.set_title("Outcome at discharge by site", fontsize=24)
ax.set_xlabel('',fontsize=22)
ax.set_xticklabels(disch4.index, fontsize=16, rotation=0)
#ax.set_ylabel('Frequency',fontsize=22)
plt.yticks(fontsize=16)
#plt.grid()


plt.savefig('outcome3.png', dpi=400, bbox_inches="tight")
plt.show()
