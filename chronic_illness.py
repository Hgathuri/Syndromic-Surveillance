# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:20:11 2023

@author: hgathuri
"""


for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 

    
    if site_df.shape[0]==0: 
        pass
    ### Comorbidity at Admission
    chronic_illness = site_df['chronic_illness'].\
    value_counts(dropna=False).reset_index().rename(columns={'chronic_illness':'m1'})
    
    chronic_merge3 = chronic_illness.set_index('index')
   
    # Calculate Percentage
    chronic_merge3['m1_percent'] = (chronic_merge3['m1'] / chronic_merge3['m1'].sum()) * 100
    
    chronic_merge3.loc['Total'] = chronic_merge3.sum()
    
    try:
        chronic_merge3['Proportion (%)'] = [f"{round(a)} ({round(b)}%)" for a,
                           b in zip(chronic_merge3['m1'],chronic_merge3['m1_percent'])]
    except:
        chronic_merge3['Proportion (%)'] = 0
    
   
    chronic_merge4 = chronic_merge3['Proportion (%)'].reset_index()
   
    ## rename 'Empty'
    chronic_merge4.loc[chronic_merge4['index']=='Empty','index'] = 'Undocumented'
    
    chronic_merge4 = chronic_merge4.rename(columns={'index':'Comorbidity at Admission'}).set_index('Comorbidity at Admission')
    
    chronic_merge4.to_excel('comorbidity_at_admission_' + site + '.xlsx')
    
    