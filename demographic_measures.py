# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:33:31 2023

@author: hgathuri
"""


import pandas as pd
import numpy as np


### Creating 'age' variable

synd_df4['age'] = synd_df4['calculated_age']
synd_df4.loc[((synd_df4['calculated_age'].isnull()) & (synd_df4['age_years'].notnull())),'age'] = synd_df4['age_years']


### Removing the dtype error
synd_df4['age']=synd_df4['age'].astype('category')

#drop records missing ages
synd_df4.loc[synd_df4['age']=='-1','age'] = np.nan
synd_df4 = synd_df4.loc[synd_df4['age'].notnull()]

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
       
    ### Rate of documentation of Demographic measures i.e., Weight, height, Age and Sex
    
    ### Weight
    site_df['weight_doc'] = 0
    site_df.loc[(site_df['weight'].notnull()) & (site_df['weight'] != -1),'weight_doc'] = 1
    
    # Height
    site_df['height_doc'] = 0
    site_df.loc[(site_df['height'].notnull()) & (site_df['height'] != -1),'height_doc'] = 1
    
    # Age
    site_df['age_doc'] = 0
    site_df.loc[(site_df['age'].notnull()) & (site_df['age'] != -1),'age_doc'] = 1
    
    # sex
    site_df['sex_doc'] = 0
    site_df.loc[site_df['sex'].notnull(),'sex_doc'] = 1
    
    
    
    site_df_w = site_df[site_df['weight_doc'] == 1]
    site_df_h = site_df[site_df['height_doc'] == 1]
    site_df_a = site_df[site_df['age_doc'] == 1]
    site_df_s = site_df[site_df['sex_doc'] == 1]
    
    m1_weight_doc = site_df_w.groupby(['hospital'])['weight_doc'].sum()
    m1_height_doc = site_df_h.groupby(['hospital'])['height_doc'].sum()
    m1_age_doc = site_df_a.groupby(['hospital'])['age_doc'].sum()
    m1_sex_doc = site_df_s.groupby(['hospital'])['sex_doc'].sum()
    
    m1_admissions = site_df['hospital'].value_counts(dropna=False)
    
    m1_doc = pd.merge(m1_weight_doc,m1_height_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_age_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_sex_doc,left_index=True,right_index=True,how='outer')
    m1_doc = pd.merge(m1_doc,m1_admissions,left_index=True,right_index=True,how='outer')
    m1_doc = m1_doc.rename(columns={'count':'admissions'}).fillna(0)
    
    
    m1_doc['weight_pct'] = round((m1_doc['weight_doc']/m1_doc['admissions'])*100,2)
    m1_doc['height_pct'] = round((m1_doc['height_doc']/m1_doc['admissions'])*100,2)
    m1_doc['age_pct'] = round((m1_doc['age_doc']/m1_doc['admissions'])*100,2)
    m1_doc['sex_pct'] = round((m1_doc['sex_doc']/m1_doc['admissions'])*100,2)
    
    m1_doc['Weight_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['weight_pct'])]
    m1_doc['Height_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['height_pct'])]
    m1_doc['Sex_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['sex_pct'])]
    m1_doc['Age_m1'] = [f"{round(a)} ({round(b)}%)" for a,b in zip(m1_doc['admissions'],m1_doc['age_pct'])]
    
    m1_demographic = m1_doc[['Weight_m1','Height_m1','Sex_m1','Age_m1']]
    
    
    
    ### Merge the 3 dfs after Transposing
    m1_demographic.columns = m1_demographic.columns.str.replace(r'_m1', '')
    m1_demographic = m1_demographic.T
    m1_demographic = m1_demographic.rename(columns={site:'April'})
    
    
    Demographic_measures = m1_demographic
              
    ### Renaming index
    Demographic_measures = Demographic_measures.rename(columns={'April': 'Documentation'}) 
    Demographic_measures.index = Demographic_measures.index.set_names('Demographic Measures')
    Demographic_measures = Demographic_measures.rename_axis('', axis='columns')
                                                          
    Demographic_measures.to_excel('Demographic_measures_' + site + '.xlsx')
