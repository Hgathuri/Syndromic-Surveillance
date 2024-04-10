# -*- coding: utf-8 -*-
"""
Created on Sat May  6 00:08:12 2023

@author: hgathuri
"""

########### Key Priority Measures
# Documentation of HIV status, COVID vaccination, COVID tests, Comorbidities
   
#HIV Status
synd_df2['hiv_doc'] = 0
synd_df2.loc[(synd_df2['hiv_status'].notnull()) & (synd_df2['hiv_status'] != 'Empty'),'hiv_doc'] = 1
synd_df2['hiv_doc'].value_counts(dropna=False)

# COVID vaccination
synd_df2['covid_vacc_doc'] = 0
synd_df2.loc[(synd_df2['received_covid_19_vaccine'].notnull()) & (synd_df2['received_covid_19_vaccine'] != 'Empty'),'covid_vacc_doc'] = 1
synd_df2['covid_vacc_doc'].value_counts(dropna=False)

# covid_19_test
synd_df2['covid_test_doc'] = 0
synd_df2.loc[synd_df2['disease_specific_tests___5']=='Checked','covid_test_doc'] = 1
synd_df2['covid_test_doc'].value_counts(dropna=False)

# Comorbidities/Chronic illness
synd_df2['comorbidity_doc'] = 0
synd_df2.loc[(synd_df2['chronic_illness'].notnull()) & (synd_df2['chronic_illness'] != 'Empty'),'comorbidity_doc'] = 1
synd_df2['comorbidity_doc'].value_counts(dropna=False)

### Grouping and summing
synd_df2_hiv = synd_df2[synd_df2['hiv_doc'] == 1].groupby\
    (['region'])['hiv_doc'].sum()

synd_df2_covid_vacc = synd_df2[synd_df2['covid_vacc_doc'] == 1].groupby\
    (['region'])['covid_vacc_doc'].sum()

synd_df2_covid_test = synd_df2[synd_df2['covid_test_doc'] == 1].groupby\
    (['region'])['covid_test_doc'].sum()
    
synd_df2_comorbidity = synd_df2[synd_df2['comorbidity_doc'] == 1].groupby\
    (['region'])['comorbidity_doc'].sum()    


### Merging the above
pm_doc = pd.merge(synd_df2_hiv,synd_df2_covid_vacc,left_index=True,right_index=True,how='outer')
pm_doc = pd.merge(pm_doc,synd_df2_covid_test,left_index=True,right_index=True,how='outer')
pm_doc = pd.merge(pm_doc,synd_df2_comorbidity,left_index=True,right_index=True,how='outer')
pm_doc = pd.merge(pm_doc,apr_admissions,left_index=True,right_index=True,how='outer').fillna(0)
pm_doc = pm_doc.rename(columns={'region':'admissions'})

### Getting the percentages
pm_doc['hiv_pct'] = (round((pm_doc['hiv_doc']/pm_doc['admissions'])*100)).astype(int)
pm_doc['covid_vacc_pct'] = (round((pm_doc['covid_vacc_doc']/pm_doc['admissions'])*100)).astype(int)
pm_doc['covid_test_pct'] = (round((pm_doc['covid_test_doc']/pm_doc['admissions'])*100)).astype(int)
pm_doc['comorbidity_pct'] = (round((pm_doc['comorbidity_doc']/pm_doc['admissions'])*100)).astype(int)

###
pm_doc['HIV status'] = [f"{round(a)} {round(b)}%" for a,b in zip(pm_doc['admissions'],pm_doc['hiv_pct'])]
pm_doc['COVID vaccination'] = (pm_doc['covid_vacc_pct']).astype(str) + '%'
pm_doc['COVID tests'] = (pm_doc['covid_test_pct']).astype(str) + '%'
pm_doc['Comorbidities'] = (pm_doc['comorbidity_pct']).astype(str) + '%'

pm_doc = pm_doc[['HIV status', 'COVID vaccination', 
                         'COVID tests','Comorbidities']]


    ############# For Site Specific
for site in synd_df2['hospital'].unique():
    
    synd_df2_site = synd_df2.loc[synd_df2['hospital']== site]
    
    #HIV Status
    synd_df2_site['hiv_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['hiv_status'].notnull()) & (synd_df2_site['hiv_status'] != 'Empty'),'hiv_doc'] = 1
    
    # COVID vaccination
    synd_df2_site['covid_vacc_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['received_covid_19_vaccine'].notnull()) & (synd_df2_site['received_covid_19_vaccine'] != 'Empty'),'covid_vacc_doc'] = 1
    
    # covid_19_test
    synd_df2_site['covid_test_doc'] = 0
    synd_df2_site.loc[synd_df2_site['disease_specific_tests___5']=='Checked','covid_test_doc'] = 1
    
    # Comorbidities/Chronic illness
    synd_df2_site['comorbidity_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['chronic_illness'].notnull()) & (synd_df2_site['chronic_illness'] != 'Empty'),'comorbidity_doc'] = 1
    
    ### Grouping and summing
    synd_df2_site_hiv = synd_df2_site[synd_df2_site['hiv_doc'] == 1].groupby\
        (['hospital'])['hiv_doc'].sum()
    
    synd_df2_site_covid_vacc = synd_df2_site[synd_df2_site['covid_vacc_doc'] == 1].groupby\
        (['hospital'])['covid_vacc_doc'].sum()
    
    synd_df2_site_covid_test = synd_df2_site[synd_df2_site['covid_test_doc'] == 1].groupby\
        (['hospital'])['covid_test_doc'].sum()
        
    synd_df2_site_comorbidity = synd_df2_site[synd_df2_site['comorbidity_doc'] == 1].groupby\
        (['hospital'])['comorbidity_doc'].sum()    
    
    apr_site_admissions = synd_df2_site['hospital'].value_counts(dropna=False)
    
    ### Merging the above
    pm_apr_doc = pd.merge(synd_df2_site_hiv,synd_df2_site_covid_vacc,left_index=True,right_index=True,how='outer')
    pm_apr_doc = pd.merge(pm_apr_doc,synd_df2_site_covid_test,left_index=True,right_index=True,how='outer')
    pm_apr_doc = pd.merge(pm_apr_doc,synd_df2_site_comorbidity,left_index=True,right_index=True,how='outer')
    pm_apr_doc = pd.merge(pm_apr_doc,apr_site_admissions,left_index=True,right_index=True,how='outer').fillna(0)
    pm_apr_doc = pm_apr_doc.rename(columns={'hospital':'admissions'})
    
    ### Getting the percentages
    try:
        pm_apr_doc['hiv_pct'] = (round((pm_apr_doc['hiv_doc']/pm_apr_doc['admissions'])*100)).astype(int)
    except:
        pm_apr_doc['hiv_pct'] = 0
    try:
        pm_apr_doc['covid_vacc_pct'] = (round((pm_apr_doc['covid_vacc_doc']/pm_apr_doc['admissions'])*100)).astype(int)
    except:
        pm_apr_doc['covid_vacc_pct'] = 0
    try:
        pm_apr_doc['covid_test_pct'] = (round((pm_apr_doc['covid_test_doc']/pm_apr_doc['admissions'])*100)).astype(int)
    except:
        pm_apr_doc['covid_test_pct'] = 0
    try:
        pm_apr_doc['comorbidity_pct'] = (round((pm_apr_doc['comorbidity_doc']/pm_apr_doc['admissions'])*100)).astype(int)
    except:
        pm_apr_doc['comorbidity_pct'] = 0
    ###
    pm_apr_doc['HIV status'] = [f"{round(a)} {round(b)}%" for a,b in zip(pm_apr_doc['admissions'],pm_apr_doc['hiv_pct'])]
    pm_apr_doc['COVID vaccination'] = (pm_apr_doc['covid_vacc_pct']).astype(str) + '%'
    pm_apr_doc['COVID tests'] = (pm_apr_doc['covid_test_pct']).astype(str) + '%'
    pm_apr_doc['Comorbidities'] = (pm_apr_doc['comorbidity_pct']).astype(str) + '%'
    
    pm_apr_doc = pm_apr_doc[['HIV status', 'COVID vaccination', 
                             'COVID tests','Comorbidities']]
    
    ### Merge the 2 dfs
    kpm = pd.concat([pm_apr_doc,pm_doc])
    
    kpm.to_excel('Key_priority_measures_' + site + '.xlsx')
    
