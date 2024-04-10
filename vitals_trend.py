# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:19:32 2023

@author: hgathuri
"""
import pandas as pd
from matplotlib.font_manager import FontProperties

### After getting the full dataset

synd_df4_trend = synd_df3.copy()

#site='Kerugoya'
for site in synd_df4_trend['hospital'].unique(): 
    site_df = synd_df4_trend[synd_df4_trend['hospital']== site] 
    if site=='Kerugoya': 
        site_df = site_df.loc[site_df['date_of_outcome'] > '2023-07-01']
    else:
        pass
    ### Rate of documentation of Vital Signs
   
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

   
     ### Grouping and summing 
    
     #### Convert the 'Date' column to datetime
    site_df['date_of_outcome'] = pd.to_datetime(site_df['date_of_outcome'])
     
     # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_temp = site_df[site_df['temp_doc'] == 1].groupby\
     (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['temp_doc'].sum().reset_index()
     
    admissions = site_df.groupby(['hospital',site_df['date_of_outcome'].dt.to_period('M')])['record_id'].count().reset_index()
    
     ### Merge the two
    site_df_temp2 = pd.merge(site_df_temp,admissions,on=['hospital','date_of_outcome'],
     how='outer')
   
    site_df_temp2 = site_df_temp2.rename(columns={'record_id':'admissions'})
    site_df_temp2['documentation'] = round((site_df_temp2['temp_doc']/site_df_temp2['admissions'])*100)
   
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_temp2['date_of_outcome'] = site_df_temp2['date_of_outcome'].dt.to_timestamp()
    site_df_temp2['date_of_outcome'] = site_df_temp2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_temp2['date_of_outcome'] = pd.to_datetime(site_df_temp2['date_of_outcome'], format='%Y-%m')
    
    # Define the date range for filtering
    start_date = pd.to_datetime('2023-04', format='%Y-%m')
    end_date = pd.to_datetime('2024-01', format='%Y-%m')
    
    # Filter rows with dates between the desired range
    site_df_temp3 = site_df_temp2[(site_df_temp2['date_of_outcome'] >= start_date) & (site_df_temp2['date_of_outcome'] <= end_date)]
   
    # introduce the vitals
    site_df_temp3['vitals'] = 'Temperature'
   
   
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_resp_rate = site_df[site_df['resp_rate_doc'] == 1].groupby\
    (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['resp_rate_doc'].sum().reset_index()
    
   
    ### Merge the two
    site_df_resp_rate2 = pd.merge(site_df_resp_rate,admissions,on=['hospital','date_of_outcome'],
     how='outer')
    
    site_df_resp_rate2 = site_df_resp_rate2.rename(columns={'record_id':'admissions'})
    site_df_resp_rate2['documentation'] = round((site_df_resp_rate2['resp_rate_doc']/site_df_resp_rate2['admissions'])*100)
    
    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_resp_rate2['date_of_outcome'] = site_df_resp_rate2['date_of_outcome'].dt.to_timestamp()
    site_df_resp_rate2['date_of_outcome'] = site_df_resp_rate2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_resp_rate2['date_of_outcome'] = pd.to_datetime(site_df_resp_rate2['date_of_outcome'], format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_resp_rate3 = site_df_resp_rate2[(site_df_resp_rate2['date_of_outcome'] >= start_date) & (site_df_resp_rate2['date_of_outcome'] <= end_date)]
   
    # introduce the vitals
    site_df_resp_rate3['vitals'] = 'Respiratory rate'
    
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_heart_rate = site_df[site_df['heart_rate_doc'] == 1].groupby\
    (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['heart_rate_doc'].sum().reset_index()
 
 
    ### Merge the two
    site_df_heart_rate2 = pd.merge(site_df_heart_rate,admissions,on=['hospital','date_of_outcome'],
     how='outer')
 
    site_df_heart_rate2 = site_df_heart_rate2.rename(columns={'record_id':'admissions'})
    site_df_heart_rate2['documentation'] = round((site_df_heart_rate2['heart_rate_doc']/site_df_heart_rate2['admissions'])*100)
 
    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_heart_rate2['date_of_outcome'] = site_df_heart_rate2['date_of_outcome'].dt.to_timestamp()
    site_df_heart_rate2['date_of_outcome'] = site_df_heart_rate2['date_of_outcome'].dt.strftime('%Y-%m')

    site_df_heart_rate2['date_of_outcome'] = pd.to_datetime(site_df_heart_rate2['date_of_outcome'], format='%Y-%m')
 
    # Filter rows with dates between December 2022 and August 2023
    site_df_heart_rate3 = site_df_heart_rate2[(site_df_heart_rate2['date_of_outcome'] >= start_date) & (site_df_heart_rate2['date_of_outcome'] <= end_date)]
 
    # introduce the vitals
    site_df_heart_rate3['vitals'] = 'Heart Rate' 
    
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_oxygen_sat = site_df[site_df['oxygen_sat_doc'] == 1].groupby\
    (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['oxygen_sat_doc'].sum().reset_index()


    ### Merge the two
    site_df_oxygen_sat2 = pd.merge(site_df_oxygen_sat,admissions,on=['hospital','date_of_outcome'],
     how='outer')

    site_df_oxygen_sat2 = site_df_oxygen_sat2.rename(columns={'record_id':'admissions'})
    site_df_oxygen_sat2['documentation'] = round((site_df_oxygen_sat2['oxygen_sat_doc']/site_df_oxygen_sat2['admissions'])*100)

    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_oxygen_sat2['date_of_outcome'] = site_df_oxygen_sat2['date_of_outcome'].dt.to_timestamp()
    site_df_oxygen_sat2['date_of_outcome'] = site_df_oxygen_sat2['date_of_outcome'].dt.strftime('%Y-%m')

    site_df_oxygen_sat2['date_of_outcome'] = pd.to_datetime(site_df_oxygen_sat2['date_of_outcome'], format='%Y-%m')

    # Filter rows with dates between December 2022 and August 2023
    site_df_oxygen_sat3 = site_df_oxygen_sat2[(site_df_oxygen_sat2['date_of_outcome'] >= start_date) & (site_df_oxygen_sat2['date_of_outcome'] <= end_date)]

    # introduce the vitals
    site_df_oxygen_sat3['vitals'] = 'Oxygen Saturation'
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_blood_pressure_sys = site_df[site_df['blood_pressure_sys_doc'] == 1].groupby\
    (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['blood_pressure_sys_doc'].sum().reset_index()


    ### Merge the two
    site_df_blood_pressure_sys2 = pd.merge(site_df_blood_pressure_sys,admissions,on=['hospital','date_of_outcome'],
     how='outer')

    site_df_blood_pressure_sys2 = site_df_blood_pressure_sys2.rename(columns={'record_id':'admissions'})
    site_df_blood_pressure_sys2['documentation'] = round((site_df_blood_pressure_sys2['blood_pressure_sys_doc']/site_df_blood_pressure_sys2['admissions'])*100)

    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_blood_pressure_sys2['date_of_outcome'] = site_df_blood_pressure_sys2['date_of_outcome'].dt.to_timestamp()
    site_df_blood_pressure_sys2['date_of_outcome'] = site_df_blood_pressure_sys2['date_of_outcome'].dt.strftime('%Y-%m')

    site_df_blood_pressure_sys2['date_of_outcome'] = pd.to_datetime(site_df_blood_pressure_sys2['date_of_outcome'], format='%Y-%m')

    # Filter rows with dates between December 2022 and August 2023
    site_df_blood_pressure_sys3 = site_df_blood_pressure_sys2[(site_df_blood_pressure_sys2['date_of_outcome'] >= start_date) & (site_df_blood_pressure_sys2['date_of_outcome'] <= end_date)]

    # introduce the vitals
    site_df_blood_pressure_sys3['vitals'] = 'Blood Pressure'
    
    
   
    ### Concatenate the 5 dfs
    vitals_concat2 = pd.concat([site_df_temp3,site_df_resp_rate3])
    vitals_concat2 = pd.concat([vitals_concat2,site_df_heart_rate3])
    vitals_concat2 = pd.concat([vitals_concat2,site_df_oxygen_sat3])
    vitals_concat2 = pd.concat([vitals_concat2,site_df_blood_pressure_sys3])
   
    vitals_concat3 = vitals_concat2[['date_of_outcome','vitals','documentation']]
    #vitals_concat3.to_csv('vitals_merge5.csv')
   
    # Sort the DataFrame by the 'Date' column in ascending order
    vitals_concat3 = vitals_concat3.sort_values(by='date_of_outcome').fillna(0)
   
    ### Plotting
    
    # Convert the 'Date' column to datetime
    #vitals_concat3['date_of_outcome'] = vitals_concat3['date_of_outcome'].dt.to_timestamp()
   
    # Extract the month names
    vitals_concat3['date_of_outcome'] = vitals_concat3['date_of_outcome'].dt.strftime('%b-%y')
    
    # Create a separate line plot for each unique category
    categories = vitals_concat3['vitals'].unique()
    plt.figure(figsize=(10, 6))
   
    for category in categories:
        category_data = vitals_concat3[vitals_concat3['vitals'] == category]
        plt.plot(category_data['date_of_outcome'], category_data['documentation'], label=category, marker='o')
       
    # Add labels and a title
    #plt.xlabel('Date')
    # Set y-axis ticks from 0 to 100
    plt.yticks(range(0, 101, 10))
    plt.xticks(fontsize=14, fontname='Times New Roman')
    plt.ylabel('Documentation(%)',fontsize=14,fontname='Times New Roman')
    plt.title('Trend of Vitals Documentation Over Time',fontsize=16, fontname='Times New Roman')
    
    # Create the legend
    legend_font = FontProperties(family='Times New Roman')
    legend = plt.legend(title='Vitals', prop=legend_font)
    
    # Set the font type of the legend title to Times New Roman
    legend.get_title().set_fontproperties(legend_font)
   
    plt.grid(True)
    plt.savefig('vitals_trends_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()



