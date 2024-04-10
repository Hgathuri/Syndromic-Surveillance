# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:25:40 2023

@author: hgathuri
"""

#### Mortality Trend
synd_df4_trend = synd_df3.copy()

#site = 'Bungoma'
for site in synd_df4_trend['hospital'].unique(): 
    site_df = synd_df4_trend[synd_df4_trend['hospital']== site] 
    if site=='Kerugoya': 
        site_df = site_df.loc[site_df['date_of_outcome'] > '2023-07-01']
    else:
        pass
    
    ### Convert to datetime
    site_df['date_of_outcome'] = pd.to_datetime(site_df['date_of_outcome'])
    
    ### Get the count of outcome by month per Hospital
    outcome_df1 = site_df.groupby(['hospital',site_df['date_of_outcome'].dt.to_period('M')])['outcome'].\
        agg('value_counts').reset_index(name='Count')
    
    
    ### Calculate the total count within each group
    outcome_df1['Total'] = outcome_df1.groupby(['hospital','date_of_outcome'])['Count'].transform('sum')
    
    # Calculate the percentage within each group
    outcome_df1['Percentage'] = round((outcome_df1['Count'] / outcome_df1['Total']) * 100)
    
    ### Get Mortalities
    mortality_df = outcome_df1[outcome_df1['outcome']=='Dead']
    
    # Define the date range for filtering
    start_date = pd.to_datetime('2023-04', format='%Y-%m')
    end_date = pd.to_datetime('2024-01', format='%Y-%m')
    
    # Filter rows with dates between the desired range
    # Convert the 'Date' column to datetime format
    #mortality_df['date_of_outcome'] = mortality_df['date_of_outcome'].dt.to_timestamp()
    mortality_df['date_of_outcome'] = mortality_df['date_of_outcome'].dt.strftime('%Y-%m')
    
    mortality_df['date_of_outcome'] = pd.to_datetime(mortality_df['date_of_outcome'], format='%Y-%m')
        
    mortality_df2 = mortality_df[(mortality_df['date_of_outcome'] >= start_date) & (mortality_df['date_of_outcome'] <= end_date)]
    
    
    ### Plotting
    ### Set font type
    csfont = {'fontname':'Times New Roman'}
    
    # Extract the month names
    mortality_df2['date_of_outcome'] = mortality_df2['date_of_outcome'].dt.strftime('%b-%y')
    
    mortality_df3 = mortality_df2[['date_of_outcome','Percentage']].set_index('date_of_outcome')
    
    ax = mortality_df3.plot(figsize=(10,6),marker='o',legend=False)
    #add overall title
    ax.set_title("Trend of Mortality over Time", fontsize=16,**csfont)
    # Convert index values to a list of strings
    xtick_labels = list(mortality_df3.index)
    # Set xticks to show all values from the DataFrame column
    plt.xticks(range(len(xtick_labels)), xtick_labels, fontsize=14, **csfont, rotation=0)
    ax.set_ylabel('Proportion (%)',fontsize=16,**csfont)
    ax.set_xlabel('')
    plt.yticks(range(0, 101, 10),fontsize=14,**csfont)
    plt.grid()
    
        
    plt.savefig('Mortality_trend_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()


