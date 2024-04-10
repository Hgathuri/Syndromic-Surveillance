# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:19:13 2023

@author: hgathuri
"""
    
#b)	Vitals signs i.e., BP, temperature etc
# temp
#synd_df2.loc[synd_df2['temp']=='36.5@','temp'] = 36.5
synd_df2['temp_doc'] = 0
synd_df2.loc[(synd_df2['temp'].notnull()) & (synd_df2['temp'] != -1),'temp_doc'] = 1
synd_df2['temp_doc'].value_counts(dropna=False)

# R.R
synd_df2['resp_rate_doc'] = 0
synd_df2.loc[(synd_df2['resp_rate'].notnull()) & (synd_df2['resp_rate'] != -1),'resp_rate_doc'] = 1
synd_df2['resp_rate_doc'].value_counts(dropna=False)

# HR
synd_df2['heart_rate_doc'] = 0
synd_df2.loc[(synd_df2['heart_rate'].notnull()) & (synd_df2['heart_rate'] != -1),'heart_rate_doc'] = 1
synd_df2['heart_rate_doc'].value_counts(dropna=False)

# Oxygen saturation
synd_df2['oxygen_sat_doc'] = 0
synd_df2.loc[(synd_df2['oxygen_sat'].notnull()) & (synd_df2['oxygen_sat'] != -1),'oxygen_sat_doc'] = 1
synd_df2['oxygen_sat_doc'].value_counts(dropna=False)

# BP Sys
synd_df2['blood_pressure_sys_doc'] = 0
synd_df2.loc[(synd_df2['blood_pressure_sys'].notnull()) & (synd_df2['blood_pressure_sys'] != -1),'blood_pressure_sys_doc'] = 1
synd_df2['blood_pressure_sys_doc'].value_counts(dropna=False)

# BP Dias
synd_df2['blood_pressure_dia_doc'] = 0
synd_df2.loc[(synd_df2['blood_pressure_dia'].notnull()) & (synd_df2['blood_pressure_dia'] != -1),'blood_pressure_dia_doc'] = 1
synd_df2['blood_pressure_dia_doc'].value_counts(dropna=False)

synd_df2_tmp = synd_df2[synd_df2['temp_doc'] == 1]
synd_df2_rr = synd_df2[synd_df2['resp_rate_doc'] == 1]
synd_df2_hr = synd_df2[synd_df2['heart_rate_doc'] == 1]
synd_df2_os = synd_df2[synd_df2['oxygen_sat_doc'] == 1]
synd_df2_bps = synd_df2[synd_df2['blood_pressure_sys_doc'] == 1]
synd_df2_bpdia = synd_df2[synd_df2['blood_pressure_dia_doc'] == 1]

apr_temp_doc = synd_df2_tmp.groupby(['region'])['temp_doc'].sum()
apr_rr_doc = synd_df2_rr.groupby(['region'])['resp_rate_doc'].sum()
apr_hr_doc = synd_df2_hr.groupby(['region'])['heart_rate_doc'].sum()
apr_os_doc = synd_df2_os.groupby(['region'])['oxygen_sat_doc'].sum()
apr_bps_doc = synd_df2_bps.groupby(['region'])['blood_pressure_sys_doc'].sum()
apr_bpdia_doc = synd_df2_bpdia.groupby(['region'])['blood_pressure_dia_doc'].sum()

apr_admissions = synd_df2['region'].value_counts(dropna=False)

apr_doc = pd.merge(apr_temp_doc,apr_rr_doc,left_index=True,right_index=True,how='outer')
apr_doc = pd.merge(apr_doc,apr_hr_doc,left_index=True,right_index=True,how='outer')
apr_doc = pd.merge(apr_doc,apr_os_doc,left_index=True,right_index=True,how='outer')
apr_doc = pd.merge(apr_doc,apr_bps_doc,left_index=True,right_index=True,how='outer')
apr_doc = pd.merge(apr_doc,apr_bpdia_doc,left_index=True,right_index=True,how='outer')
apr_doc = pd.merge(apr_doc,apr_admissions,left_index=True,right_index=True,how='outer')

apr_doc = apr_doc.rename(columns={'region':'admissions'}).fillna(0)

## %pct
apr_doc['temp_pct'] = (round((apr_doc['temp_doc']/apr_doc['admissions'])*100)).astype(int)
apr_doc['rr_pct'] = (round((apr_doc['resp_rate_doc']/apr_doc['admissions'])*100)).astype(int)
apr_doc['hr_pct'] = (round((apr_doc['heart_rate_doc']/apr_doc['admissions'])*100)).astype(int)
apr_doc['os_pct'] = (round((apr_doc['oxygen_sat_doc']/apr_doc['admissions'])*100)).astype(int)
apr_doc['bps_pct'] = (round((apr_doc['blood_pressure_sys_doc']/apr_doc['admissions'])*100)).astype(int)
apr_doc['bpdia_pct'] = (round((apr_doc['blood_pressure_dia_doc']/apr_doc['admissions'])*100)).astype(int)


apr_doc['Temperature'] = [f"{round(a)} {round(b)}%" for a,b in zip(apr_doc['admissions'],apr_doc['temp_pct'])]
apr_doc['Respiratory rate'] = (apr_doc['rr_pct']).astype(str) + '%'
apr_doc['Heart Rate'] = (apr_doc['hr_pct']).astype(str) + '%'
apr_doc['Oxygen Saturation'] = (apr_doc['os_pct']).astype(str) + '%'
apr_doc['Blood Pressure'] = (apr_doc['bps_pct']).astype(str) + '%'


apr_vitals = apr_doc[['Temperature', 'Respiratory rate', 'Heart Rate', 'Oxygen Saturation',
         'Blood Pressure']]

for site in synd_df2['hospital'].unique():
    ######### For Specific sites
    synd_df2_site = synd_df2.loc[synd_df2['hospital']== site]
    
    synd_df2_site['temp_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['temp'].notnull()) & (synd_df2_site['temp'] != -1),'temp_doc'] = 1
    synd_df2_site['temp_doc'].value_counts(dropna=False)
    
    # R.R
    synd_df2_site['resp_rate_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['resp_rate'].notnull()) & (synd_df2_site['resp_rate'] != -1),'resp_rate_doc'] = 1
    synd_df2_site['resp_rate_doc'].value_counts(dropna=False)
    
    # HR
    synd_df2_site['heart_rate_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['heart_rate'].notnull()) & (synd_df2_site['heart_rate'] != -1),'heart_rate_doc'] = 1
    synd_df2_site['heart_rate_doc'].value_counts(dropna=False)
    
    # Oxygen saturation
    synd_df2_site['oxygen_sat_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['oxygen_sat'].notnull()) & (synd_df2_site['oxygen_sat'] != -1),'oxygen_sat_doc'] = 1
    synd_df2_site['oxygen_sat_doc'].value_counts(dropna=False)
    
    # BP Sys
    synd_df2_site['blood_pressure_sys_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['blood_pressure_sys'].notnull()) & (synd_df2_site['blood_pressure_sys'] != -1),'blood_pressure_sys_doc'] = 1
    synd_df2_site['blood_pressure_sys_doc'].value_counts(dropna=False)
    
    # BP Dias
    synd_df2_site['blood_pressure_dia_doc'] = 0
    synd_df2_site.loc[(synd_df2_site['blood_pressure_dia'].notnull()) & (synd_df2_site['blood_pressure_dia'] != -1),'blood_pressure_dia_doc'] = 1
    synd_df2_site['blood_pressure_dia_doc'].value_counts(dropna=False)
    
    synd_df2_site_tmp = synd_df2_site[synd_df2_site['temp_doc'] == 1]
    synd_df2_site_rr = synd_df2_site[synd_df2_site['resp_rate_doc'] == 1]
    synd_df2_site_hr = synd_df2_site[synd_df2_site['heart_rate_doc'] == 1]
    synd_df2_site_os = synd_df2_site[synd_df2_site['oxygen_sat_doc'] == 1]
    synd_df2_site_bps = synd_df2_site[synd_df2_site['blood_pressure_sys_doc'] == 1]
    synd_df2_site_bpdia = synd_df2_site[synd_df2_site['blood_pressure_dia_doc'] == 1]
    
    apr_site_temp_doc = synd_df2_site_tmp.groupby(['hospital'])['temp_doc'].sum()
    apr_site_rr_doc = synd_df2_site_rr.groupby(['hospital'])['resp_rate_doc'].sum()
    apr_site_hr_doc = synd_df2_site_hr.groupby(['hospital'])['heart_rate_doc'].sum()
    apr_site_os_doc = synd_df2_site_os.groupby(['hospital'])['oxygen_sat_doc'].sum()
    apr_site_bps_doc = synd_df2_site_bps.groupby(['hospital'])['blood_pressure_sys_doc'].sum()
    apr_site_bpdia_doc = synd_df2_site_bpdia.groupby(['hospital'])['blood_pressure_dia_doc'].sum()
    
    apr_site_admissions = synd_df2_site['hospital'].value_counts(dropna=False)
    
    apr_site_doc = pd.merge(apr_site_temp_doc,apr_site_rr_doc,left_index=True,right_index=True,how='outer')
    apr_site_doc = pd.merge(apr_site_doc,apr_site_hr_doc,left_index=True,right_index=True,how='outer')
    apr_site_doc = pd.merge(apr_site_doc,apr_site_os_doc,left_index=True,right_index=True,how='outer')
    apr_site_doc = pd.merge(apr_site_doc,apr_site_bps_doc,left_index=True,right_index=True,how='outer')
    apr_site_doc = pd.merge(apr_site_doc,apr_site_bpdia_doc,left_index=True,right_index=True,how='outer')
    apr_site_doc = pd.merge(apr_site_doc,apr_site_admissions,left_index=True,right_index=True,how='outer')
    
    apr_site_doc = apr_site_doc.rename(columns={'hospital':'admissions'}).fillna(0)
    
    ## %pct
    apr_site_doc['temp_pct'] = round((apr_site_doc['temp_doc']/apr_site_doc['admissions'])*100).astype(int)
    apr_site_doc['rr_pct'] = round((apr_site_doc['resp_rate_doc']/apr_site_doc['admissions'])*100).astype(int)
    apr_site_doc['hr_pct'] = round((apr_site_doc['heart_rate_doc']/apr_site_doc['admissions'])*100).astype(int)
    apr_site_doc['os_pct'] = round((apr_site_doc['oxygen_sat_doc']/apr_site_doc['admissions'])*100).astype(int)
    apr_site_doc['bps_pct'] = round((apr_site_doc['blood_pressure_sys_doc']/apr_site_doc['admissions'])*100).astype(int)
    apr_site_doc['bpdia_pct'] = round((apr_site_doc['blood_pressure_dia_doc']/apr_site_doc['admissions'])*100).astype(int)
    
    
    apr_site_doc['Temperature'] = [f"{round(a)} {round(b)}%" for a,b in zip(apr_site_doc['admissions'],apr_site_doc['temp_pct'])]
    apr_site_doc['Respiratory rate'] = (apr_site_doc['rr_pct']).astype(str) + '%'
    apr_site_doc['Heart Rate'] = (apr_site_doc['hr_pct']).astype(str) + '%'
    apr_site_doc['Oxygen Saturation'] = (apr_site_doc['os_pct']).astype(str) + '%'
    apr_site_doc['Blood Pressure'] = (apr_site_doc['bps_pct']).astype(str) + '%'
    
    
    apr_site_vitals = apr_site_doc[['Temperature', 'Respiratory rate', 'Heart Rate', 'Oxygen Saturation',
             'Blood Pressure']]
    
    ### Merge the 2 dfs
    Vitals = pd.concat([apr_site_vitals,apr_vitals])
    
    Vitals.to_excel('Vitals_' + site + '.xlsx')
