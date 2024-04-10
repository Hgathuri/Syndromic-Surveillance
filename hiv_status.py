# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:10:36 2023

@author: hgathuri
"""


for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    
    ### HIV status of admitted patients. 
    hiv_status = site_df['hiv_status'].\
        value_counts(dropna=False).reset_index().rename(columns={'hiv_status':'m1'})
    
      
    hiv_merge2 = hiv_status
       
    ### Replacing Null values
    hiv_merge3 = hiv_merge2.fillna(0).set_index('m1')
    
    # Calculate Percentage
    hiv_merge3['m1_percent'] = (round((hiv_merge3['count']) / (hiv_merge3['count'].sum()) * 100)).astype(int)
    
    
    hiv_merge3.loc['Total'] = hiv_merge3.sum()
    
    try:
        hiv_merge3['Patients (%)'] = [f"{round(a)} ({round(b)}%)" for a,
                               b in zip(hiv_merge3['count'],hiv_merge3['m1_percent'])]
    except:
        hiv_merge3['Patients (%)'] = '0' + '%'
      
    
        
    hiv_merge4 = hiv_merge3['Patients (%)'].reset_index()
    
    ## rename 'Empty'
    hiv_merge4.loc[hiv_merge4['m1']=='Empty','m1'] = 'Undocumented'
    
    hiv_merge4 = hiv_merge4.rename(columns={'m1':'HIV Status'}).\
        set_index('HIV Status')
    hiv_merge4.to_excel('hiv_status_' + site + '.xlsx')

   