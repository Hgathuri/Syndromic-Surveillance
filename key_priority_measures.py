# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:05:16 2023

@author: hgathuri
"""
import pandas as pd

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    m1_admissions = site_df['hospital'].value_counts(dropna=False)
    
    
    ########### Key Priority Measures
    # Documentation of HIV status, COVID vaccination, COVID tests, Comorbidities
    
    #HIV Status
    site_df['hiv_doc'] = 0
    site_df.loc[(site_df['hiv_status'].notnull()) & (site_df['hiv_status'] != 'Empty'),'hiv_doc'] = 1
    
    # COVID vaccination
    site_df['covid_vacc_doc'] = 0
    site_df.loc[(site_df['received_covid_19_vaccine'].notnull()) & (site_df['received_covid_19_vaccine'] != 'Empty'),'covid_vacc_doc'] = 1
    
    # covid_19_test
    #site_df['covid_test_doc'] = 0
    #site_df.loc[site_df['disease_specific_tests___5']=='Checked','covid_test_doc'] = 1
    
    # Comorbidities/Chronic illness
    site_df['comorbidity_doc'] = 0
    site_df.loc[(site_df['chronic_illness'].notnull()) & (site_df['chronic_illness'] != 'Empty'),'comorbidity_doc'] = 1
    
    
    ### Grouping and summing
    site_df_hiv = site_df[site_df['hiv_doc'] == 1].groupby\
        (['hospital'])['hiv_doc'].sum()
    
    site_df_covid_vacc = site_df[site_df['covid_vacc_doc'] == 1].groupby\
        (['hospital'])['covid_vacc_doc'].sum()
    
    #site_df_covid_test = site_df[site_df['covid_test_doc'] == 1].groupby(['hospital'])['covid_test_doc'].sum()
        
    site_df_comorbidity = site_df[site_df['comorbidity_doc'] == 1].groupby\
        (['hospital'])['comorbidity_doc'].sum()    
    
    
    ### Merging the above
    m1_pm_doc = pd.merge(site_df_hiv,site_df_covid_vacc,left_index=True,right_index=True,how='outer')
    #m1_pm_doc = pd.merge(m1_pm_doc,site_df_covid_test,left_index=True,right_index=True,how='outer')
    m1_pm_doc = pd.merge(m1_pm_doc,site_df_comorbidity,left_index=True,right_index=True,how='outer')
    m1_pm_doc = pd.merge(m1_pm_doc,m1_admissions,left_index=True,right_index=True,how='outer').fillna(0)
    m1_pm_doc = m1_pm_doc.rename(columns={'count':'admissions'})
    
    
    ###Adjusting
    #m1_pm_doc['hospital'] = 98
    
    
    
    ### Getting the percentages
    m1_pm_doc['hiv_pct'] = round((m1_pm_doc['hiv_doc']/m1_pm_doc['admissions'])*100,2)
    m1_pm_doc['covid_vacc_pct'] = round((m1_pm_doc['covid_vacc_doc']/m1_pm_doc['admissions'])*100,2)
   #m1_pm_doc['covid_test_pct'] = round((m1_pm_doc['covid_test_doc']/m1_pm_doc['admissions'])*100,2)
    m1_pm_doc['comorbidity_pct'] = round((m1_pm_doc['comorbidity_doc']/m1_pm_doc['admissions'])*100,2)
    
    ###
    try: 
        m1_pm_doc['HIV status_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_pm_doc['admissions'],m1_pm_doc['hiv_pct'])]
    except:
        m1_pm_doc['HIV status_m1'] = 0
    try: 
        m1_pm_doc['COVID vaccination_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_pm_doc['admissions'],
                                                                           m1_pm_doc['covid_vacc_pct'])]
    except:
        m1_pm_doc['COVID vaccination_m1'] = 0
   # try: 
   #     m1_pm_doc['COVID tests_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_pm_doc['admissions'],
   #                                                                  m1_pm_doc['covid_test_pct'])]
   # except:
   #     m1_pm_doc['COVID tests_m1'] = 0
    try: 
        m1_pm_doc['Comorbidities_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_pm_doc['admissions'],
                                                                     m1_pm_doc['comorbidity_pct'])]
    except:
        m1_pm_doc['Comorbidities_m1'] = 0
        
    m1_pm_doc = m1_pm_doc[['HIV status_m1', 'COVID vaccination_m1','Comorbidities_m1']]
    
    
    ### Transpose the df
    m1_pm_doc.columns = m1_pm_doc.columns.str.replace(r'_m1', '')
    m1_pm_doc = m1_pm_doc.T
    m1_pm_doc = m1_pm_doc.rename(columns={site:'April'})
       
    ### 
    Key_priority_measures = m1_pm_doc
    
    ### Renaming index
    Key_priority_measures = Key_priority_measures.rename(columns={'April': 'Documentation'})
    Key_priority_measures.index = Key_priority_measures.\
        index.set_names('Key Priority Measures')
    Key_priority_measures = Key_priority_measures.rename_axis('', axis='columns')
    
    Key_priority_measures.to_excel('Key_priority_measures_' + site + '.xlsx')
