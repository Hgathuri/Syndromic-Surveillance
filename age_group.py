# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:30:36 2023

@author: hgathuri
"""
import numpy as np
from pylab import MaxNLocator
#site = 'Mbagathi'
##Age group distribution of the admitted patients
for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    site_df['age'] = site_df['calculated_age']
    site_df.loc[((site_df['calculated_age'].isnull()) & (site_df['age_years'].notnull())),'age'] = site_df['age_years']
    
    site_df['age'].value_counts(dropna=False)
    
    # Convert the column to float with 'coerce' option
    site_df['age'] = pd.to_numeric(site_df['age'], errors='coerce')
    
    ### Removing the dtype error
    site_df['age']=site_df['age'].astype(float)
    
    #drop records missing ages
    site_df.loc[(site_df['age']=='-1') | (site_df['age']==-1),'age'] = np.nan
    site_df = site_df.loc[site_df['age'].notnull()]
    
    
    bins2 = [0,17,20,30,40,50,60,200]
    labels = ['10-17 years','18-20 years','21-30 years', '31-40 years', '41-50 years','51-60 years','> 60 years']
    site_df['age_grouped'] = pd.cut(site_df['age'], bins2, labels = labels,include_lowest = True)
    
    
    age = site_df['age_grouped'].value_counts(dropna=False).sort_index()
    
    ##renaming NAN
    try:
        age.rename(index={np.nan:'Missing'},inplace=True)
    except:
        pass
    
    #age.to_csv('age.csv')
    
    ### Adjusting to match the previous loaded data
    #age.iloc[6] = 48
    #age.iloc[3] = 45
    
    ##plotting for age
    ### removing the nan
    #age = age.iloc[:-1]
    ax = age.plot(kind='bar',figsize=(18,8))
    
    #add overall title
    ax.set_title("Patients Age group Distribution", fontsize=30,**csfont)
    ax.set_xticklabels(age.index, fontsize=22, **csfont, rotation=0)
    ya = ax.get_yaxis()
    ya.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylabel('Count',fontsize=26,**csfont)
    ax.set_xlabel('')
    plt.yticks(fontsize=22,**csfont)
    
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.text(x+width/2, 
                y+height/2, 
                '{:.0f}'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center',fontsize=22,**csfont,fontweight='bold')
        
    plt.savefig('age_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()

### Lowest  Age and Site
#site_df['age'].min()
#site_df.loc[site_df['age']==12,['redcap_data_access_group','age']]

## Retrieving records with missing ages
#site_df.loc[((site_df['calculated_age'].isnull()) & (site_df['age_verbatim'].isnull())),['record_id','age','redcap_data_access_group']]
   
      