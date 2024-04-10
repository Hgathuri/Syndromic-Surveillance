# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:37:45 2023

@author: hgathuri
"""

from pylab import MaxNLocator
#site='Mbagathi'

for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    site_df.loc[(site_df['outcome']=='Dead') & 
                (site_df['cause_of_death'].isnull()),'cause_of_death'] = site_df['cause_of_death_file']
    
    site_df2 = site_df[site_df['outcome']=='Dead']
    #site_df2['cause_of_death'].value_counts(dropna=False)
    
    ### Export Asphyxia and XN6FR,Retrovirus
    #a = site_df2.loc[site_df2['cause_of_death']=='XN6FR,Retrovirus',['record_id','ipno','cause_of_death']]
    #a.to_csv('Retrovirus_records_Mbagathi.csv',index=False)
    
    
    #site_df2.loc[site_df2['cause_of_death']=='None','cause_of_death'] = 'Undocumented'
    site_df2.loc[site_df2['cause_of_death']=='MC82.Z,Cardiac arrest, unspecified','cause_of_death'] = site_df2['morbid_1']
    
    ### Omit these when calculating proportions 
    site_df2 = site_df2.loc[site_df2['cause_of_death']!='None']
    site_df2 = site_df2.loc[site_df2['cause_of_death']!='Missing']
    site_df2 = site_df2.loc[site_df2['cause_of_death']!='Other']
    site_df2 = site_df2.loc[site_df2['cause_of_death']!='Undocumented']
    
    cause_of_death_df = pd.DataFrame(site_df2['cause_of_death'].value_counts())
    
    ###Drop Asphyxia
    #cause_of_death_df = cause_of_death_df.drop('XN6FR,Retrovirus')
    
    ### Get proportions
    cause_of_death_df['cause_of_death_pct'] = (cause_of_death_df['count'] / cause_of_death_df['count'].sum()) * 100
    cause_of_death_df['cause_of_death_pct'] = round(cause_of_death_df['cause_of_death_pct'],2)
    
    ### Get top 5 in every site
    cause_of_death_df2 = cause_of_death_df.head(5)
    
    ### Plotting
    ### Set font type
    csfont = {'fontname':'Times New Roman'}
    
    cause_of_death_df3 = cause_of_death_df2.sort_values(by='cause_of_death_pct',ascending=True)
    
    
    if cause_of_death_df3.empty:
        pass
    else: 
        ax = cause_of_death_df3['cause_of_death_pct'].plot(kind='barh',figsize=(34,28),legend=False)
         
        #add overall title
        ax.set_ylabel('',fontsize=60)
        ax.set_yticklabels(cause_of_death_df3.index, fontsize=60, rotation=0,**csfont)
        ax.set_xlabel('Proportion (%)',fontsize=60,**csfont)
        ya = ax.get_xaxis()
        ya.set_major_locator(MaxNLocator(integer=True))
        plt.xticks(fontsize=60,**csfont)
        
        for p in ax.patches: 
             ax.annotate(format(round(p.get_width()), '.0f')+"%",
                         (p.get_x() + p.get_width()/2, p.get_y()+.2),
                         ha = 'center', va = 'center', **csfont,
                         size=40,
                         textcoords='offset points',fontweight='bold')
        
        plt.savefig('top5_causes_of_death_' + site + '.png', dpi=400, bbox_inches="tight")
        plt.show()