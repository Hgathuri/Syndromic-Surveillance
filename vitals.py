# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:48:28 2023

@author: hgathuri
"""

import pandas as pd

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
       
    m1_admissions = site_df['hospital'].value_counts(dropna=False)
    
    # temp
    site_df['temp_doc'] = 0
    site_df.loc[(site_df['temp'].notnull()) & (site_df['temp'] != -1),'temp_doc'] = 1
    
    # R.R
    site_df['resp_rate_doc'] = 0
    site_df.loc[(site_df['resp_rate'].notnull()) & (site_df['resp_rate'] != -1),'resp_rate_doc'] = 1
    
    # HR
    site_df['heart_rate_doc'] = 0
    site_df.loc[(site_df['heart_rate'].notnull()) & (site_df['heart_rate'] != -1),'heart_rate_doc'] = 1
    
    # Oxygen saturation
    site_df['oxygen_sat_doc'] = 0
    site_df.loc[(site_df['oxygen_sat'].notnull()) & (site_df['oxygen_sat'] != -1),'oxygen_sat_doc'] = 1
    
    # BP Sys
    site_df['blood_pressure_sys_doc'] = 0
    site_df.loc[(site_df['blood_pressure_sys'].notnull()) & (site_df['blood_pressure_sys'] != -1),'blood_pressure_sys_doc'] = 1
    
    # BP Dias
    site_df['blood_pressure_dia_doc'] = 0
    site_df.loc[(site_df['blood_pressure_dia'].notnull()) & (site_df['blood_pressure_dia'] != -1),'blood_pressure_dia_doc'] = 1
    
    site_df_tmp = site_df[site_df['temp_doc'] == 1]
    site_df_rr = site_df[site_df['resp_rate_doc'] == 1]
    site_df_hr = site_df[site_df['heart_rate_doc'] == 1]
    site_df_os = site_df[site_df['oxygen_sat_doc'] == 1]
    site_df_bps = site_df[site_df['blood_pressure_sys_doc'] == 1]
    site_df_bpdia = site_df[site_df['blood_pressure_dia_doc'] == 1]
    
    m1_temp_doc = site_df_tmp.groupby(['hospital'])['temp_doc'].sum()
    m1_rr_doc = site_df_rr.groupby(['hospital'])['resp_rate_doc'].sum()
    m1_hr_doc = site_df_hr.groupby(['hospital'])['heart_rate_doc'].sum()
    m1_os_doc = site_df_os.groupby(['hospital'])['oxygen_sat_doc'].sum()
    m1_bps_doc = site_df_bps.groupby(['hospital'])['blood_pressure_sys_doc'].sum()
    m1_bpdia_doc = site_df_bpdia.groupby(['hospital'])['blood_pressure_dia_doc'].sum()
    
    m1_doc = pd.merge(m1_temp_doc,m1_rr_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_hr_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_os_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_bps_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_bpdia_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_admissions,left_index=True,right_index=True,how='outer')
    
    m1_doc = m1_doc.rename(columns={'count':'admissions'}).fillna(0)
    
    ## %pct
    m1_doc['temp_pct'] = round((m1_doc['temp_doc']/m1_doc['admissions'])*100,2)
    m1_doc['rr_pct'] = round((m1_doc['resp_rate_doc']/m1_doc['admissions'])*100,2)
    m1_doc['hr_pct'] = round((m1_doc['heart_rate_doc']/m1_doc['admissions'])*100,2)
    m1_doc['os_pct'] = round((m1_doc['oxygen_sat_doc']/m1_doc['admissions'])*100,2)
    m1_doc['bps_pct'] = round((m1_doc['blood_pressure_sys_doc']/m1_doc['admissions'])*100,2)
    m1_doc['bpdia_pct'] = round((m1_doc['blood_pressure_dia_doc']/m1_doc['admissions'])*100,2)
    
    
    try:
        m1_doc['Temperature_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['temp_pct'])]
    except:
        m1_doc['Temperature_m1'] = 0
    try: 
        m1_doc['Respiratory rate_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['rr_pct'])]
    except:
        m1_doc['Respiratory rate_m1'] = 0
    try: 
        m1_doc['Heart Rate_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['hr_pct'])]
    except:
        m1_doc['Heart Rate_m1'] = 0
    try:
        m1_doc['Oxygen Saturation_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['os_pct'])]
    except:
        m1_doc['Oxygen Saturation_m1'] = 0
    try:
        m1_doc['Blood Pressure_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['bps_pct'])]
    except:
        m1_doc['Blood Pressure_m1'] = 0
    m1_vitals = m1_doc[['Temperature_m1', 'Respiratory rate_m1', 'Heart Rate_m1', 'Oxygen Saturation_m1',
             'Blood Pressure_m1']]
    
    ### Merge the 3 dfs after Transposing
    m1_vitals.columns = m1_vitals.columns.str.replace(r'_m1', '')
    m1_vitals = m1_vitals.T
    m1_vitals = m1_vitals.rename(columns={site:'April'})
    
    
    Vitals = m1_vitals
              
    ### Renaming index
    Vitals = Vitals.rename(columns={'April': 'Documentation'})
    Vitals.index = Vitals.index.set_names('Vitals')
    Vitals = Vitals.rename_axis('', axis='columns')
                                                          
    Vitals.to_excel('Vitals_' + site + '.xlsx')
