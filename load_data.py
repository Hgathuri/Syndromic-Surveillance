# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:30:04 2023

@author: hgathuri
"""

import requests
import pandas as pd
import numpy as np
import datetime
from io import StringIO
from datetime import date, timedelta
import matplotlib.pyplot as plt
from scipy.stats import iqr
import matplotlib.font_manager as font_manager

#### Baseline

data1 = {
    'token': '',
    'content': 'record',
    'format': 'csv',
    'type': 'flat',
    'csvDelimiter': '',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'true',
    'returnFormat': 'csv'
}
synd_r = requests.post('https://.........../',data=data1)
print('HTTP Status: ' + str(synd_r.status_code))

##Transform data into a dataframe
synd_bl_df1 = pd.read_csv(StringIO(synd_r.text),low_memory=False)


### Current Tool (April 2023 onwards)
data2 = {
    'token': '',
    'content': 'record',
    'format': 'csv',
    'type': 'flat',
    'csvDelimiter': '',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'true',
    'returnFormat': 'csv'
}
synd_live = requests.post('https://.............../',data=data2)
print('HTTP Status: ' + str(synd_live.status_code))


##Transform data into a dataframe
synd_live_df = pd.read_csv(StringIO(synd_live.text),low_memory=False)

### Remove CGTRH records from the current tool
synd_live_df = synd_live_df.loc[synd_live_df['redcap_data_access_group']!='CGTRH']


### Load records in CGTRH's project
#!/usr/bin/env python

data3 = {
    'token': '',
    'content': 'record',
    'format': 'csv',
    'type': 'flat',
    'csvDelimiter': '',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'true',
    'returnFormat': 'csv'
}
cgtrh = requests.post('https://............../',data=data3)
print('HTTP Status: ' + str(cgtrh.status_code))

##Transform data into a dataframe
synd_cgtrh_df = pd.read_csv(StringIO(cgtrh.text),low_memory=False)

### Re-label the hospital variable 
synd_cgtrh_df.loc[synd_cgtrh_df['hospital']==87,'hospital'] = 'Coast General Teaching and Referral Hospital'
synd_cgtrh_df.loc[synd_cgtrh_df['hospital']==83,'hospital'] = 'Kilifi County Hospital'

###Concat live tool and CGTRH's
synd_live_df2 = pd.concat([synd_live_df, synd_cgtrh_df], ignore_index=True)


#### 
cols1 = list(synd_bl_df1.columns)
cols2 = list(synd_live_df2.columns)

set(cols2) - set(cols1)
set(cols1) - set(cols2)


### Matching variables in baseline with those in current tool

recode_vars = {'age_verbatim':'age_years',
'patient_information_complete':'biodata_complete',
'weight_admission':'weight'}

synd_bl_df1 = synd_bl_df1.rename(columns=recode_vars)


### Condensing variables in current tool

#### microbiology
synd_live_df2['microbiology'] = 'No'
synd_live_df2.loc[synd_live_df2['microbiology___7']=='Unchecked','microbiology'] = 'Yes'

#### malaria_test
synd_live_df2['malaria_test'] = 'No'
synd_live_df2.loc[synd_live_df2['disease_specific_tests___1']=='Checked','malaria_test'] = 'Yes'

#### imaging
synd_live_df2['imaging'] = 'No'
synd_live_df2.loc[synd_live_df2['routine_radiology___5']=='Unchecked','imaging'] = 'Yes'

#### chemistry_investigations
synd_live_df2['chemistry_investigations'] = 'No'
synd_live_df2.loc[synd_live_df2['biochemistry___6']=='Unchecked','chemistry_investigations'] = 'Yes'

#### haematology_test
synd_live_df2['haematology_test'] = 'No'
synd_live_df2.loc[(synd_live_df2['haematology___1']=='Checked') |
                 (synd_live_df2['haematology___2']=='Checked'),'haematology_test'] = 'Yes'

#### COVID-19 Test
synd_live_df2['covid_19_test'] = 'No'
synd_live_df2.loc[synd_live_df2['disease_specific_tests___5']=='Checked','covid_19_test'] = 'Yes'

#### HIV Test
synd_live_df2['hiv_test_ordered'] = 'No'
synd_live_df2.loc[synd_live_df2['disease_specific_tests___4']=='Checked','hiv_test_ordered'] = 'Yes'

#### TB test
synd_live_df2['tb_test_ordered'] = 'No'
synd_live_df2.loc[(synd_live_df2['disease_specific_tests___2']=='Checked') |
                 (synd_live_df2['disease_specific_tests___3']=='Checked'),'tb_test_ordered'] = 'Yes'

#### Glucose test
synd_live_df2['glucose_ordered'] = 'No'
synd_live_df2.loc[(synd_live_df2['biochemistry___3']=='Checked') |
                 (synd_live_df2['biochemistry___4']=='Checked'),'glucose_ordered'] = 'Yes'

#### Investigations_for_urine
synd_live_df2['investigations_for_urine'] = 'No'
synd_live_df2.loc[(synd_live_df2['microbiology___1']=='Checked') |
                 (synd_live_df2['microbiology___2']=='Checked'),'investigations_for_urine'] = 'Yes'


#### Investigations_for_stool
synd_live_df2['investigations_for_stool'] = 'No'
synd_live_df2.loc[synd_live_df2['microbiology___5']=='Checked','investigations_for_stool'] = 'Yes'


### Merge the two datasets
synd_full_df = pd.concat([synd_live_df2, synd_bl_df1], ignore_index=True)

####Shortening the hosp names
hosp_map = {'Bungoma County Hospital':'Bungoma',
'Busia County Referral Hospital':'Busia',
'Coast General Teaching and Referral Hospital':'CGTRH',
'Embu Level 5 Teaching and Referral Hospital':'Embu',
'Homabay County Referral Hospital':'Homabay',
'Kakamega County General & Teaching Referral Hospital':'Kakamega',
'Kenyatta University Teaching and Referral Hospital':'KUTRH',
'Kiambu Level 5 Hospital':'Kiambu',
'Kisii Teaching and Referral Hospital':'Kisii',
'Kisumu County Hospital':'Kisumu',
'Kitale County Referral Hospital':'Kitale',
'Macalder Sub County Hospital':'Macalder',
'Machakos Level 5 Hospital':'Machakos',
'Mama Lucy Kibaki Hospital':'Mama Lucy',
'Mbagathi Hospital':'Mbagathi',
'Migori County Hospital':'Migori',
'Naivasha County Referral Hospital':'Naivasha',
'Jaramogi Oginga Odinga Teaching and Referral Hospital':'JOOTRH',
'Kerugoya County Referral Hospital': 'Kerugoya',
'Moi University Teaching and Referral Hospital':'MTRH',
'Kilifi County Hospital':'Kilifi'
}

for a1, a2 in hosp_map.items():
    synd_full_df.loc[synd_full_df['hospital']==a1, 'hospital']=a2


## use DAG where hospital name is missing
synd_full_df.loc[synd_full_df['hospital'].isnull(),'hospital'] = synd_full_df['redcap_data_access_group']

synd_df3 = synd_full_df

### merge dates of outcome
synd_df3['date_of_outcome'] = synd_df3['date_of_discharge']
synd_df3.loc[((synd_df3['date_of_discharge'].isnull()) & (synd_df3['date_of_death'].notnull())),'date_of_outcome'] = synd_df3['date_of_death']
synd_df3.loc[((synd_df3['date_of_discharge'].isnull()) & (synd_df3['status_at_discharge'] =='Absconded')),'date_of_outcome'] = synd_df3['date_of_abscondment']
synd_df3.loc[((synd_df3['date_of_discharge'].isnull()) & (synd_df3['status_at_discharge'] =='Referred')),'date_of_outcome'] = synd_df3['date_of_referral']
synd_df3.loc[((synd_df3['date_of_discharge'].isnull()) & (synd_df3['status_at_discharge'] =='DAMA')),'date_of_outcome'] = synd_df3['date_of_dama']

#### Pick records with both dates of adm and dates of outcome
synd_df3 = synd_df3.loc[(synd_df3['date_of_admission'].notnull()) & 
                  (synd_df3['date_of_outcome'].notnull())]


### Filter discharges for the reporting month
synd_df4 = synd_df3.loc[synd_df3['date_of_outcome'].between('2024-02-01','2024-02-29')]

## Correcting the record below
#synd_df4.loc[synd_df4['record_id']=='437-261','hospital'] = 'Kilifi'


### Load abd data
#kilifi_df = pd.read_stata('C:/Users/hgathuri/OneDrive - Kemri Wellcome Trust/Git/SYNDROMIC/Kilifi/CIN_DataMonthly_Aug.dta')

### Introduce region variable
#kilifi_df['redcap_data_access_group'] = 'Kilifi'

### Subset for the month of interest
#kilifi_df1 = kilifi_df.loc[kilifi_df['dod'].between('2023-09-01','2023-09-31')]

### Get admissions for the year 2023
synd_df5 = synd_df3.loc[synd_df3['date_of_admission'].between('2023-01-01','2023-12-31')]


# =============================================================================
# ### Fill the blanks hospitals based on the reecord ids
# synd_df5.loc[(synd_df5['record_id'].str.startswith('68')) & (synd_df5['hospital'].isnull()),'hospital'] = 'Kitale'
# 
# synd_df5['hospital'].value_counts(dropna=False).to_excel('Annual_admissions_2023.xlsx')
# synd_df5.groupby('hospital')['record_id'].count()
# 
# synd_df5.loc[synd_df5['hospital'].isnull()].head()
# 
# =============================================================================
