# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:31:50 2023

@author: hgathuri
"""

####Outcome at discharge per hospital – Alive, dead, referred.

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site]
    
    outcome1 = pd.DataFrame(site_df['status_at_discharge'].value_counts())
    outcome2 = pd.DataFrame(site_df['outcome'].value_counts())
    outcome2 = outcome2.reset_index()
    outcome2 = outcome2[outcome2['outcome'] == 'Dead']
    outcome2 = outcome2.rename(columns={'outcome':'status_at_discharge'}).set_index('status_at_discharge')
    
    ## Concat the two dfs
    outcome3 = pd.concat([outcome1,outcome2])
    outcome3 = outcome3.rename(index={'Discharged':'Alive'})
    
    ## Save to plot with excel
    outcome3.to_excel('outcome_pct_' + site + '.xlsx')
      
    
# =============================================================================
#     
#     s=site_df.groupby('hospital')['date_of_entry'].count().reset_index()
#     s=s.rename(columns={'hospital': 'Hospital','date_of_entry':'Patients Discharged'})
#     
#     outcome = site_df['outcome'].value_counts(dropna=False)
#     #outcome.to_csv('outcome.csv')
#     
#     status_at_discharge = site_df['status_at_discharge'].value_counts(dropna=False)	
#     #status_at_discharge.to_csv('status_at_discharge.csv')
#     
#     
#     ######### Create a bar graph with these columns for each hospital.
#     ### Alive, Dead, Referred
#     
#     a_df = site_df[(site_df['outcome'] == 'Alive') & (site_df['status_at_discharge'] == 'Discharged')]
#     d_df = site_df[site_df['outcome'] == 'Dead']
#     r_df = site_df[(site_df['outcome'] == 'Alive') & (site_df['status_at_discharge'] == 'Referred')]
#     absc_df = site_df[(site_df['outcome'] == 'Alive') & (site_df['status_at_discharge'] == 'Absconded')]
#     dama_df = site_df[(site_df['outcome'] == 'Alive') & (site_df['status_at_discharge'] == 'DAMA')]
#     
#     d=d_df.groupby('hospital')['date_of_entry'].count()
#     r=r_df.groupby('hospital')['record_id'].count()
#     a=a_df.groupby('hospital')['date_of_entry'].count()
#     s=s.set_index('Hospital')
#     
#     disch1 = pd.merge(s,a,left_index=True,right_index=True,how='outer')
#     disch2 = pd.merge(disch1,d,left_index=True,right_index=True,how='outer')
#     disch3 = pd.merge(disch2,r,left_index=True,right_index=True,how='outer').fillna(0)
#     disch4 = disch3.rename(columns={'date_of_entry_y':'Dead','record_id':'Referred','date_of_entry_x':'Alive'})
#     
#     disch5 = disch4[['Alive', 'Dead', 'Referred']].T
#     
#     ### Get percentages
#     disch5['outcome_pct'] = (disch5[site] / disch5[site].sum()) * 100
#     disch5['outcome_pct'] = round(disch5['outcome_pct'])
#     
#     
#     ## Save to plot with excel
#     disch5.to_excel('outcome_pct_' + site + '.xlsx')
#     
# # =============================================================================
# =============================================================================
#     ##Plot
#     ax = disch4.plot(kind='pie',figsize=(12,8),color=['#1f77b4','#2ca02c', '#d62728','#ff7f0e' ])
#     
#     #add overall title
#     ax.set_title("Outcome at discharge", fontsize=20)
#     ax.set_xlabel('',fontsize=22)
#     ax.set_xticklabels('', fontsize=16, rotation=0)
#     #ax.set_ylabel('Frequency',fontsize=22)
#     plt.yticks(fontsize=16)
#     #plt.grid()
#     
#     
#     #plt.savefig('Outcome_' + site + '.png', dpi=400, bbox_inches="tight")
#     plt.show()
# 
# =============================================================================
