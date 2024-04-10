# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:48:43 2023

@author: hgathuri
"""

#site = 'Mama_Lucy'
for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
       
    #### Covid-19 vaccine status of admitted patients
    ####Replace null with Empty
    site_df.loc[site_df['received_covid_19_vaccine']==-1,
                   'received_covid_19_vaccine'] = 'Empty'
    
    received_covid_19_vaccine = site_df['received_covid_19_vaccine'].\
        value_counts(dropna=False).reset_index().\
            rename(columns={'received_covid_19_vaccine':'m1'})
    
    vacc_merge2 = received_covid_19_vaccine
    
    ### Replacing Null values
    vacc_merge3 = vacc_merge2.fillna(0).set_index('m1')
    
    
    # Calculate Percentage
    vacc_merge3['m1_percent'] = (round((vacc_merge3['count']) / (vacc_merge3['count'].sum()) * 100)).astype(int)
    
    
    vacc_merge3.loc['Total'] = vacc_merge3.sum()
    
    try:
        vacc_merge3['Patients (%)'] = [f"{round(a)} ({round(b)}%)" for a,
                               b in zip(vacc_merge3['count'],vacc_merge3['m1_percent'])]
    except:
        vacc_merge3['Patients (%)'] = '0' + '%'
      
    
        
    vacc_merge4 = vacc_merge3['Patients (%)'].reset_index()
    
    ## rename 'Empty'
    vacc_merge4.loc[vacc_merge4['m1']=='Empty','m1'] = 'Undocumented'
    
    vacc_merge4 = vacc_merge4.rename(columns={'m1':'COVID-19 Vaccination Status'}).\
        set_index('COVID-19 Vaccination Status')
    vacc_merge4.to_excel('vacc_status_' + site + '.xlsx')


