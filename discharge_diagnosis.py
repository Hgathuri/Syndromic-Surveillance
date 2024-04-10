# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:19:24 2023

@author: hgathuri
"""

import numpy as np
from pylab import MaxNLocator
#site='JOOTRH'
for site in synd_df4['hospital'].unique():
     site_df = synd_df4[synd_df4['hospital']== site] 
     
     diag_cols = ['discharge_diagnosis_1','discharge_diagnosis_2','discharge_diagnosis_3',
                  'discharge_diagnosis_4','discharge_diagnosis_5', 'discharge_diagnosis_6',
                  'discharge_diagnosis_7','discharge_diagnosis_8']
     
     #Getting the frequency of diagnosis per site 
     disch_diag = site_df.groupby('hospital').agg({i:'value_counts' for i in site_df[diag_cols]})
     
     disch_diag['discharge_diagnosis_count'] = disch_diag.sum(axis=1, numeric_only=True)
     
     # Groupby using DataFrame.agg() Method.
     disch_diag2 = disch_diag.reset_index()
     disch_diag3 = disch_diag2.sort_values(by=['hospital','discharge_diagnosis_count'],ascending = [True,False])
     
     disch_diag4 = disch_diag3[['hospital', 'level_1', 'discharge_diagnosis_count']]
     
     disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='None']
     disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='Missing']
     
     #disch_diag4.to_csv('disch_diag41.csv')
     
     ### Categorize in ICD 11 Codes
     icd_map = {'1':'Certain infectious or parasitic diseases',
     '2':'Neoplasms',
     '3':'Diseases of the blood or blood-forming organs',
     '4':'Diseases of the immune system',
     '5':'Endocrine, nutritional or metabolic diseases',
     '6':'Mental, behavioural or neurodevelopmental disorders',
     '7':'Sleep-wake disorders',
     '8':'Diseases of the nervous system',
     '9':'Diseases of the visual system',
     'A':'Diseases of the ear or mastoid process',
     'B':'Diseases of the circulatory system',
     'C':'Diseases of the respiratory system',
     'D':'Diseases of the digestive system',
     'E':'Diseases of the skin',
     'F':'Diseases of the musculoskeletal system or connective tissue',
     'G':'Diseases of the genitourinary system',
     'H':'Conditions related to sexual health',
     'J':'Pregnancy, childbirth or the puerperium',
     'K':'Certain conditions originating in the perinatal period',
     'L':'Developmental anomalies',
     'M':'Symptoms, signs or clinical findings, not elsewhere classified',
     'N':'Injury, poisoning or certain other consequences of external causes',
     'P':'External causes of morbidity or mortality',
     'Q':'Factors influencing health status or contact with health services',
     'R':'Codes for special purposes',
     'S':'Supplementary Chapter Traditional Medicine Conditions - Module I',
     'V':'Supplementary section for functioning assessment',
     'X':'Extension Codes',
     }
     
     disch_diag4['diagnosis_grouped'] = np.nan
     
     for a1, a2 in icd_map.items():
         disch_diag4.loc[disch_diag4['level_1'].str.startswith(a1),'diagnosis_grouped'] = a2
     
     
     disch_diag5 = disch_diag4.groupby(['hospital','diagnosis_grouped']).\
         agg({'discharge_diagnosis_count':sum}).sort_values(['hospital','discharge_diagnosis_count'],
                                                                  ascending=False).reset_index()
     disch_diag4.to_excel('disch_diag_BG1.xlsx',index=False)
     
     
    ### Get percentages
     disch_diag5['discharge_diagnosis_pct'] = (disch_diag5['discharge_diagnosis_count'] / disch_diag5['discharge_diagnosis_count'].sum()) * 100
    
     disch_diag5['discharge_diagnosis_pct'] = round(disch_diag5['discharge_diagnosis_pct'])
    
    
     
    
     
    
     ### Get top 10 in every site
     ### First drop the count col
     disch_diag6 = disch_diag5.drop('discharge_diagnosis_count',axis=1)
     disch_diag6 = disch_diag6.groupby('hospital').head(10)
     
     
     #disch_diag5.to_csv('test1.csv')
     
     #disch_diag7 = disch_diag6.pivot(index='hospital', 
     #                                     columns='diagnosis_grouped', 
     #                                     values='discharge_diagnosis_pct').fillna(0)
     
     #disch_diag5.to_excel('disch_diag51.xlsx',index=False)
     #disch_diag6.to_csv('disch_diag6.csv')
     
     disch_diag7 = disch_diag6.drop('hospital',axis=1).set_index('diagnosis_grouped')
     
     ### Set font type
     csfont = {'fontname':'Times New Roman'}
     
     disch_diag8 = disch_diag7.sort_values('discharge_diagnosis_pct',ascending=True)
     
     ax = disch_diag8.plot(kind='barh',figsize=(34,28),legend=False)
     
     
     #add overall title
     #ax.set_title("Distribution of Top 10 discharge diagnosis by study sites", fontsize=24)
     ax.set_ylabel('',fontsize=60)
     ax.set_yticklabels(disch_diag8.index, fontsize=60, rotation=0,**csfont)
     ##removes the title appearing in legend
     #handles, labels = ax.get_legend_handles_labels()
     #ax.legend(handles=handles[1:], labels=labels[1:])
     ax.set_xlabel('Proportion (%)',fontsize=60,**csfont)
     ya = ax.get_xaxis()
     ya.set_major_locator(MaxNLocator(integer=True))
     plt.xticks(fontsize=60,**csfont)
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #          fancybox=True, shadow=True, ncol=2, fontsize=16)
     
    
     for p in ax.patches: 
          ax.annotate(format(round(p.get_width()), '.0f')+"%",
                        (p.get_x() + p.get_width()/2, p.get_y()+.2),
                        ha = 'center', va = 'center', **csfont,
                        size=40,
                       # xytext=(0, 1),
                        textcoords='offset points',fontweight='bold')
    
     plt.savefig('disease_patterns_at_discharge_top_10_' + site + '.png', dpi=400, bbox_inches="tight")
     plt.show()
    
    
    
    
  
