# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:07:18 2024

@author: hgathuri
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:35:01 2024

@author: hgathuri
"""

### Get synd_df4 from the full datset script

# temp
synd_df4['temp_doc'] = 0
synd_df4.loc[(synd_df4['temp'].notnull()) & (synd_df4['temp'] != -1),'temp_doc'] = 1

# R.R
synd_df4['resp_rate_doc'] = 0
synd_df4.loc[(synd_df4['resp_rate'].notnull()) & (synd_df4['resp_rate'] != -1),'resp_rate_doc'] = 1

# HR
synd_df4['heart_rate_doc'] = 0
synd_df4.loc[(synd_df4['heart_rate'].notnull()) & (synd_df4['heart_rate'] != -1),'heart_rate_doc'] = 1

# Oxygen saturation
synd_df4['oxygen_sat_doc'] = 0
synd_df4.loc[(synd_df4['oxygen_sat'].notnull()) & (synd_df4['oxygen_sat'] != -1),'oxygen_sat_doc'] = 1

# BP Sys
synd_df4['blood_pressure_sys_doc'] = 0
synd_df4.loc[(synd_df4['blood_pressure_sys'].notnull()) & (synd_df4['blood_pressure_sys'] != -1),'blood_pressure_sys_doc'] = 1


Vitals_doc = synd_df4.groupby(['hospital'])[['temp_doc','resp_rate_doc','heart_rate_doc', 'oxygen_sat_doc','blood_pressure_sys_doc']].sum()

## Getting the total number of patients per site
synd_df4_admissions = synd_df4['hospital'].value_counts(dropna=False)

### Merge the documentations rates
Vitals_doc2 = pd.merge(Vitals_doc,synd_df4_admissions,left_index=True,right_index=True)

# Calculate proportions 
Vitals_doc2[['Temperature', 'Respiratory rate', 'Heart Rate', 'Oxygen Saturation','Blood Pressure']] = round(Vitals_doc2[['temp_doc', 'resp_rate_doc', 'heart_rate_doc', 'oxygen_sat_doc','blood_pressure_sys_doc']].div(Vitals_doc2['count'], axis=0)*100).astype(int)

Vitals_doc3 = Vitals_doc2[['Temperature', 'Respiratory rate', 'Heart Rate', 'Oxygen Saturation','Blood Pressure']]

# Append a row with median values of the top 3 values in each column
median_values = Vitals_doc3.apply(lambda col: col.nlargest(3).median())

Vitals_doc3.loc['Median of Top 3'] = median_values
Vitals_doc3 = Vitals_doc3.T

for col in Vitals_doc3[['Kitale','JOOTRH','Mama Lucy','Busia']]:
    synd_df7 = Vitals_doc3[[col,'Median of Top 3']]
    synd_df7['admissions'] = synd_df4_admissions.loc[col]
    synd_df7['Documentation'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(synd_df7['admissions'],synd_df7[col])]
    synd_df7['Median of Top 3'] = (synd_df7['Median of Top 3'].astype(int)).astype(str) + '%'
    
    synd_df7[['Documentation','Median of Top 3']].to_excel('Vitals_median_' + col + '.xlsx')
    
    

    
    
    
    
    
    