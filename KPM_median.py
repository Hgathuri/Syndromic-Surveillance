# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:22:16 2024

@author: hgathuri
"""

#HIV Status
synd_df4['hiv_doc'] = 0
synd_df4.loc[(synd_df4['hiv_status'].notnull()) & (synd_df4['hiv_status'] != 'Empty'),'hiv_doc'] = 1

# COVID vaccination
synd_df4['covid_vacc_doc'] = 0
synd_df4.loc[(synd_df4['received_covid_19_vaccine'].notnull()) & (synd_df4['received_covid_19_vaccine'] != 'Empty'),'covid_vacc_doc'] = 1

# Comorbidities/Chronic illness
synd_df4['comorbidity_doc'] = 0
synd_df4.loc[(synd_df4['chronic_illness'].notnull()) & (synd_df4['chronic_illness'] != 'Empty'),'comorbidity_doc'] = 1
 

KPM_doc = synd_df4.groupby(['hospital'])[['hiv_doc','covid_vacc_doc','comorbidity_doc']].sum()

## Getting the total number of patients per site
synd_df4_admissions = synd_df4['hospital'].value_counts(dropna=False)

### Merge the documentations rates
KPM_doc2 = pd.merge(KPM_doc,synd_df4_admissions,left_index=True,right_index=True)


# Calculate proportions 
KPM_doc2[['HIV status', 'COVID vaccination', 'Comorbidities']] = round(KPM_doc2[['hiv_doc', 'covid_vacc_doc', 'comorbidity_doc']].div(KPM_doc2['count'], axis=0)*100).astype(int)

KPM_doc3 = KPM_doc2[['HIV status', 'COVID vaccination', 'Comorbidities']]

# Append a row with median values of the top 3 values in each column
median_values = KPM_doc3.apply(lambda col: col.nlargest(3).median())

KPM_doc3.loc['Median of Top 3'] = median_values
KPM_doc3 = KPM_doc3.T

for col in KPM_doc3[['Kitale','JOOTRH','Mama Lucy','Busia']]:
    synd_df7 = KPM_doc3[[col,'Median of Top 3']]
    synd_df7['admissions'] = synd_df4_admissions.loc[col]
    
    synd_df7['Documentation'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(synd_df7['admissions'],synd_df7[col])]
    synd_df7['Median of Top 3'] = (synd_df7['Median of Top 3'].astype(int)).astype(str) + '%'

    
    synd_df7[['Documentation','Median of Top 3']].to_excel('KPM_' + col + '.xlsx')