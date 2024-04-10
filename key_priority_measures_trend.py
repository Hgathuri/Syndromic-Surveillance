# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:49:15 2023

@author: hgathuri
"""

import pandas as pd
from matplotlib.font_manager import FontProperties

### After getting the full dataset

synd_df4_trend = synd_df3.copy()

site='Kisumu'
for site in synd_df4_trend['hospital'].unique(): 
    site_df = synd_df4_trend[synd_df4_trend['hospital']== site] 
    if site=='Kerugoya': 
        site_df = site_df.loc[site_df['date_of_outcome'] > '2023-07-01']
    else:
        pass
    
    #m1_admissions = site_df['hospital'].value_counts(dropna=False)
    
    
    ########### Key Priority Measures
    # Documentation of HIV status, COVID vaccination, COVID tests, Comorbidities
    
    #HIV Status
    site_df['hiv_doc'] = 0
    site_df.loc[(site_df['hiv_status'].notnull()) & (site_df['hiv_status'] != 'Empty'),'hiv_doc'] = 1
    
    # COVID vaccination
    site_df['covid_vacc_doc'] = 0
    site_df.loc[(site_df['received_covid_19_vaccine'].notnull()) & (site_df['received_covid_19_vaccine'] != 'Empty'),'covid_vacc_doc'] = 1
    
    
    # Comorbidities/Chronic illness
    site_df['comorbidity_doc'] = 0
    site_df.loc[(site_df['chronic_illness'].notnull()) & (site_df['chronic_illness'] != 'Empty'),'comorbidity_doc'] = 1
    
    
    
    ### Grouping and summing
       
    #### Convert the 'Date' column to datetime
    site_df['date_of_outcome'] = pd.to_datetime(site_df['date_of_outcome'])
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_hiv = site_df[site_df['hiv_doc'] == 1].groupby\
        (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['hiv_doc'].sum().reset_index()
    
    admissions = site_df.groupby(['hospital',site_df['date_of_outcome'].dt.to_period('M')])['record_id'].count().reset_index()
    
    ### Merge the two
    site_df_hiv2 = pd.merge(site_df_hiv,admissions,on=['hospital','date_of_outcome'],
             how='outer')
    
    site_df_hiv2 = site_df_hiv2.rename(columns={'record_id':'admissions'})
    site_df_hiv2['documentation'] = round((site_df_hiv2['hiv_doc']/site_df_hiv2['admissions'])*100)
    
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_hiv2['date_of_outcome'] = site_df_hiv2['date_of_outcome'].dt.to_timestamp()
    site_df_hiv2['date_of_outcome'] = site_df_hiv2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_hiv2['date_of_outcome'] = pd.to_datetime(site_df_hiv2['date_of_outcome'], format='%Y-%m')
    
    # Define the date range for filtering
    start_date = pd.to_datetime('2023-04', format='%Y-%m')
    end_date = pd.to_datetime('2024-01', format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_hiv3 = site_df_hiv2[(site_df_hiv2['date_of_outcome'] >= start_date) & (site_df_hiv2['date_of_outcome'] <= end_date)]
    
    # introduce the KPM
    site_df_hiv3['kpm'] = 'HIV status'
    
    
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_covid_vacc = site_df[site_df['covid_vacc_doc'] == 1].groupby\
        (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['covid_vacc_doc'].sum().reset_index()
    
    
    ### Merge the two
    site_df_covid_vacc2 = pd.merge(site_df_covid_vacc,admissions,on=['hospital','date_of_outcome'],
             how='outer')
    
    site_df_covid_vacc2 = site_df_covid_vacc2.rename(columns={'record_id':'admissions'})
    site_df_covid_vacc2['documentation'] = round((site_df_covid_vacc2['covid_vacc_doc']/site_df_covid_vacc2['admissions'])*100)
    
    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_covid_vacc2['date_of_outcome'] = site_df_covid_vacc2['date_of_outcome'].dt.to_timestamp()
    site_df_covid_vacc2['date_of_outcome'] = site_df_covid_vacc2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_covid_vacc2['date_of_outcome'] = pd.to_datetime(site_df_covid_vacc2['date_of_outcome'], format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_covid_vacc3 = site_df_covid_vacc2[(site_df_covid_vacc2['date_of_outcome'] >= start_date) & (site_df_covid_vacc2['date_of_outcome'] <= end_date)]
    
    # introduce the KPM
    site_df_covid_vacc3['kpm'] = 'COVID vaccination'
    
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_comorbidity = site_df[site_df['comorbidity_doc'] == 1].groupby\
        (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['comorbidity_doc'].sum().reset_index()
    
    
    ### Merge the two
    site_df_comorbidity2 = pd.merge(site_df_comorbidity,admissions,on=['hospital','date_of_outcome'],
             how='outer')
    
    site_df_comorbidity2 = site_df_comorbidity2.rename(columns={'record_id':'admissions'})
    site_df_comorbidity2['documentation'] = round((site_df_comorbidity2['comorbidity_doc']/site_df_comorbidity2['admissions'])*100)
    
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_comorbidity2['date_of_outcome'] = site_df_comorbidity2['date_of_outcome'].dt.to_timestamp()
    site_df_comorbidity2['date_of_outcome'] = site_df_comorbidity2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_comorbidity2['date_of_outcome'] = pd.to_datetime(site_df_comorbidity2['date_of_outcome'], format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_comorbidity3 = site_df_comorbidity2[(site_df_comorbidity2['date_of_outcome'] >= start_date) & (site_df_comorbidity2['date_of_outcome'] <= end_date)]
    
    # introduce the KPM
    site_df_comorbidity3['kpm'] = 'Comorbidities'
    
    ### Concatenate the 3 dfs
    kpm_concat1 = pd.concat([site_df_hiv3,site_df_covid_vacc3])
    kpm_concat2 = pd.concat([kpm_concat1,site_df_comorbidity3])
    
    kpm_concat3 = kpm_concat2[['date_of_outcome','kpm','documentation']]
    #kpm_concat3.to_csv('kpm_merge5.csv')
    
    # Sort the DataFrame by the 'Date' column in ascending order
    kpm_concat3 = kpm_concat3.sort_values(by='date_of_outcome').fillna(0)
    
    ### Plotting
    
    # Convert the 'Date' column to datetime
    #kpm_concat3['date_of_outcome'] = kpm_concat3['date_of_outcome'].dt.to_timestamp()
    
    # Extract the month names
    kpm_concat3['date_of_outcome'] = kpm_concat3['date_of_outcome'].dt.strftime('%b-%y')
    
    # Create a separate line plot for each unique category
    categories = kpm_concat3['kpm'].unique()
    plt.figure(figsize=(10, 6))
    
    for category in categories:
        category_data = kpm_concat3[kpm_concat3['kpm'] == category]
        plt.plot(category_data['date_of_outcome'], category_data['documentation'], label=category, marker='o')
    
    # Add labels and a title
    #plt.xlabel('Date')
    # Set y-axis ticks from 0 to 100
    plt.yticks(range(0, 101, 20))
    plt.xticks(fontsize=14, fontname='Times New Roman')
    plt.ylabel('Documentation(%)',fontsize=14,fontname='Times New Roman')
    plt.title('Trend of Key priority measures Over Time',fontsize=16, fontname='Times New Roman')
    
    # Create the legend
    legend_font = FontProperties(family='Times New Roman')
    legend = plt.legend(title='Key priority measures', prop=legend_font)
    
    # Set the font type of the legend title to Times New Roman
    legend.get_title().set_fontproperties(legend_font)
       
    plt.grid(True)
    plt.savefig('kpm_trends_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()



