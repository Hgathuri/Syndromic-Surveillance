# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:45:41 2023

@author: hgathuri
"""

from pylab import MaxNLocator
#site='Mbagathi'
for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
     
    diag_cols = ['discharge_diagnosis_1','discharge_diagnosis_2','discharge_diagnosis_3',
                 'discharge_diagnosis_4','discharge_diagnosis_5', 'discharge_diagnosis_6',
                 'discharge_diagnosis_7','discharge_diagnosis_8']
    
    
    # =============================================================================
    # ### Retrieve records containing 'Retrovirus' as the discharge diagnosis
    # # Value to search for
    # diag = 'XN6FR,Retrovirus'
    # 
    # # Check if the diagnosis is present in any of the columns
    # Retrovirus_diag = site_df[diag_cols].apply(lambda x: x == diag).any(axis=1)
    # 
    # # Get the rows where the diagnosis is present
    # Retrovirus_diag_df = site_df[Retrovirus_diag]
    # 
    # ### Export the records
    # Retrovirus_diag_df[['record_id','ipno','discharge_diagnosis_1','discharge_diagnosis_2','discharge_diagnosis_3',
    #              'discharge_diagnosis_4','discharge_diagnosis_5', 'discharge_diagnosis_6',
    #              'discharge_diagnosis_7','discharge_diagnosis_8']].to_csv('Retrovirus_diagnosis_Mbbagathi.csv',index=False)
    # 
    # =============================================================================
    
    #Getting the frequency of diagnosis per site 
    disch_diag = site_df.groupby('hospital').agg({i:'value_counts' for i in site_df[diag_cols]})
    
    disch_diag['discharge_diagnosis_count'] = disch_diag.sum(axis=1, numeric_only=True)
    
    # Groupby using DataFrame.agg() Method.
    disch_diag2 = disch_diag.reset_index()
    disch_diag3 = disch_diag2.sort_values(by=['hospital','discharge_diagnosis_count'],ascending = [True,False])
    
    disch_diag4 = disch_diag3[['hospital', 'level_1', 'discharge_diagnosis_count']]
    
    ### Omit these when calculating proportions 
    disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='None']
    disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='Missing']
    disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='Other']
    disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='Undocumented']
    
    disch_diag4.to_csv('disch_diag4.csv')
    
    b = disch_diag4.loc[disch_diag4['level_1']=='XN6FR,Retrovirus']
    
    ### Omit Retrovirus
    disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='XN6FR,Retrovirus']
    
    ### Get proportions
    disch_diag4['discharge_diagnosis_pct'] = (disch_diag4['discharge_diagnosis_count'] / disch_diag4['discharge_diagnosis_count'].sum()) * 100
    disch_diag4['discharge_diagnosis_pct'] = round(disch_diag4['discharge_diagnosis_pct'],2)
    
    ### Get top 5 in every site
    disch_diag5 = disch_diag4.head(5)
    
    ### To include 'others' uncomment below
    # =============================================================================
    # disch_diag5 = disch_diag5.groupby(['hospital', 'level_1'])[['discharge_diagnosis_count',
    #        'discharge_diagnosis_pct']].sum()
    # 
    # ### Lump the records after Top 5 to others
    # disch_diag6 = disch_diag4.tail(-5)
    # disch_diag6['level_1'] = 'Others'
    # disch_diag7 = disch_diag6.groupby(['hospital', 'level_1'])[['discharge_diagnosis_count',
    #        'discharge_diagnosis_pct']].sum()
    # 
    # ## Concat the top 5 and others
    # #symptoms443 = symptoms442.reset_index()
    # 
    # #disch_diag71 = disch_diag7.reset_index()
    # 
    # disch_diag8 = pd.concat([disch_diag5, disch_diag7])
    # disch_diag81 = disch_diag8.reset_index()
    # disch_diag9 = disch_diag81.set_index('level_1')
    # =============================================================================
    
    ### Plotting
    disch_diag52 = disch_diag5.set_index('level_1')
    
    ### Plotting
    ### Set font type
    csfont = {'fontname':'Times New Roman'}
    
    disch_diag53 = disch_diag52['discharge_diagnosis_pct'].sort_values(ascending=True)
    ax = disch_diag53.plot(kind='barh',figsize=(34,28), legend=False)
     
     
    #add overall title
    ax.set_ylabel('',fontsize=60)
    ax.set_yticklabels(disch_diag53.index, fontsize=60, rotation=0,**csfont)
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
    
    plt.savefig('top_5_discharge_diagnosis_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()


