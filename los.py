# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:25:44 2023

@author: hgathuri
"""

####Length of hospital stay

import pandas as pd

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    ### Convert the dates to datetime
    site_df['date_of_outcome'] = pd.to_datetime(site_df['date_of_outcome'])
    site_df['date_of_admission'] = pd.to_datetime(site_df['date_of_admission'])
    site_df['date_of_discharge'] = pd.to_datetime(site_df['date_of_discharge'])
    
    los_m1 = site_df['date_of_outcome'] - site_df['date_of_admission']
    
    
    ### los by site
    site_df['los_m1'] = site_df['date_of_outcome'] - site_df['date_of_admission']
    
    sites_los_iqr1_m1 = site_df.groupby(['hospital'])['los_m1'].quantile([0, 0.25, 0.5, 0.75, 0.95, 1]).reset_index()
    ### Reshape
    sites_los_iqr1_m1 = sites_los_iqr1_m1.pivot(index='hospital', columns='level_1', values='los_m1')
    sites_los_iqr1_m1 = sites_los_iqr1_m1.rename(columns={0.0:'min',0.25:'25th_percentile',0.5:'median',0.75:'75th_percentile',1.0:'max'})
    try:
        sites_los_iqr1_m1['25th_percentile'] = sites_los_iqr1_m1['25th_percentile'].dt.days
    except:
        sites_los_iqr1_m1['25th_percentile'] = 0
    try: 
        sites_los_iqr1_m1['75th_percentile'] = sites_los_iqr1_m1['75th_percentile'].dt.days
    except:
        sites_los_iqr1_m1['75th_percentile'] = 0
    try: 
        sites_los_iqr1_m1['median'] = sites_los_iqr1_m1['median'].dt.days
    except:
        sites_los_iqr1_m1['median'] = 0
        
    sites_los_iqr1_m1['median'] = sites_los_iqr1_m1['median'].astype(str) + ' days'
    sites_los_iqr1_m1['IQR'] = sites_los_iqr1_m1['25th_percentile'].astype(str) + ' - ' + sites_los_iqr1_m1['75th_percentile'].astype(str) + ' days'
    
    sites_los_iqr1_m1 = sites_los_iqr1_m1.reset_index().\
        rename(columns={'hospital':'Study Site',
                        'median':'Median Duration of hospital stay_m1',
                        'IQR':'Interquartile Range_m1'})
    
    sites_los_iqr1_m1 = sites_los_iqr1_m1[['Study Site','Median Duration of hospital stay_m1',
                        'Interquartile Range_m1']].set_index('Study Site')
    sites_los_iqr1_m1 = sites_los_iqr1_m1.rename_axis('', axis='columns')
    
    
      ### Merge the 3 dfs after Transposing
    sites_los_iqr1_m1.columns = sites_los_iqr1_m1.columns.str.replace(r'_m1', '')
    sites_los_iqr1_m1 = sites_los_iqr1_m1.T
    sites_los_iqr1_m1 = sites_los_iqr1_m1.rename(columns={site:'April'})
  
    
      ### 
    los_hosp = sites_los_iqr1_m1
    
    ### Renaming index
    los_hosp = los_hosp.rename(columns={'April': 'Duration'}) 
    los_hosp.index = los_hosp.index.set_names('')
    los_hosp = los_hosp.rename_axis('', axis='columns')
  
    los_hosp.to_excel('los_' + site + '.xlsx')