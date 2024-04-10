# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:33:47 2023

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
     
    ### Rate of documentation of Demographic measures i.e., Weight, height, Age and Sex
    
    ### Weight
    site_df['weight_doc'] = 0
    site_df.loc[(site_df['weight'].notnull()) & (site_df['weight'] != -1),'weight_doc'] = 1
    
    # Height
    site_df['height_doc'] = 0
    site_df.loc[(site_df['height'].notnull()) & (site_df['height'] != -1),'height_doc'] = 1
    
     
     
     ### Grouping and summing
    
     #### Convert the 'Date' column to datetime
    site_df['date_of_outcome'] = pd.to_datetime(site_df['date_of_outcome'])
     
     # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_weight = site_df[site_df['weight_doc'] == 1].groupby\
     (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['weight_doc'].sum().reset_index()
     
    admissions = site_df.groupby(['hospital',site_df['date_of_outcome'].dt.to_period('M')])['record_id'].count().reset_index()
    
     ### Merge the two
    site_df_weight2 = pd.merge(site_df_weight,admissions,on=['hospital','date_of_outcome'],
     how='outer')
   
    site_df_weight2 = site_df_weight2.rename(columns={'record_id':'admissions'})
    site_df_weight2['documentation'] = round((site_df_weight2['weight_doc']/site_df_weight2['admissions'])*100)
   
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_weight2['date_of_outcome'] = site_df_weight2['date_of_outcome'].dt.to_timestamp()
    site_df_weight2['date_of_outcome'] = site_df_weight2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_weight2['date_of_outcome'] = pd.to_datetime(site_df_weight2['date_of_outcome'], format='%Y-%m')
    
    # Define the date range for filtering
    start_date = pd.to_datetime('2023-04', format='%Y-%m')
    end_date = pd.to_datetime('2024-01', format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_weight3 = site_df_weight2[(site_df_weight2['date_of_outcome'] >= start_date) & (site_df_weight2['date_of_outcome'] <= end_date)]
   
    # introduce the demographic_measure
    site_df_weight3['demographic_measure'] = 'Weight'
   
   
    
    # Group by 'Category' and 'Date' (by month) and calculate the sum
    site_df_height = site_df[site_df['height_doc'] == 1].groupby\
    (['hospital',site_df['date_of_outcome'].dt.to_period('M')])['height_doc'].sum().reset_index()
    
   
    ### Merge the two
    site_df_height2 = pd.merge(site_df_height,admissions,on=['hospital','date_of_outcome'],
     how='outer')
    
    site_df_height2 = site_df_height2.rename(columns={'record_id':'admissions'})
    site_df_height2['documentation'] = round((site_df_height2['height_doc']/site_df_height2['admissions'])*100)
    
    # Filter rows for dates between December and August
    # Filter rows for dates between December and August
    # Convert the 'Date' column to datetime format
    site_df_height2['date_of_outcome'] = site_df_height2['date_of_outcome'].dt.to_timestamp()
    site_df_height2['date_of_outcome'] = site_df_height2['date_of_outcome'].dt.strftime('%Y-%m')
    
    site_df_height2['date_of_outcome'] = pd.to_datetime(site_df_height2['date_of_outcome'], format='%Y-%m')
    
    # Filter rows with dates between December 2022 and August 2023
    site_df_height3 = site_df_height2[(site_df_height2['date_of_outcome'] >= start_date) & (site_df_height2['date_of_outcome'] <= end_date)]
   
    # introduce the demographic_measure
    site_df_height3['demographic_measure'] = 'Height'
   
   
    ### Concatenate the 2 dfs
    demographic_measure_concat2 = pd.concat([site_df_weight3,site_df_height3])
   
    demographic_measure_concat3 = demographic_measure_concat2[['date_of_outcome','demographic_measure','documentation']]
    #demographic_measure_concat3.to_csv('demographic_measure_merge5.csv')
   
    # Sort the DataFrame by the 'Date' column in ascending order
    demographic_measure_concat3 = demographic_measure_concat3.sort_values(by='date_of_outcome').fillna(0)
   
    ### Plotting
    
    # Convert the 'Date' column to datetime
    #demographic_measure_concat3['date_of_outcome'] = demographic_measure_concat3['date_of_outcome'].dt.to_timestamp()
   
    # Extract the month names
    demographic_measure_concat3['date_of_outcome'] = demographic_measure_concat3['date_of_outcome'].dt.strftime('%b-%y')
    
    # Create a separate line plot for each unique category
    categories = demographic_measure_concat3['demographic_measure'].unique()
    plt.figure(figsize=(10, 6))
   
    for category in categories:
        category_data = demographic_measure_concat3[demographic_measure_concat3['demographic_measure'] == category]
        plt.plot(category_data['date_of_outcome'], category_data['documentation'], label=category, marker='o')
       
    # Add labels and a title
    #plt.xlabel('Date')
    # Set y-axis ticks from 0 to 100
    plt.yticks(range(0, 101, 10))
    plt.xticks(fontsize=14, fontname='Times New Roman')
    plt.ylabel('Documentation(%)',fontsize=14,fontname='Times New Roman')
    plt.title('Trend of Demographic measures Over Time',fontsize=16, fontname='Times New Roman')
    
    # Create the legend
    legend_font = FontProperties(family='Times New Roman')
    legend = plt.legend(title='Demographic measures', prop=legend_font)
    
    # Set the font type of the legend title to Times New Roman
    legend.get_title().set_fontproperties(legend_font)
   
    plt.grid(True)
    plt.savefig('demographic_measure_trends_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()



