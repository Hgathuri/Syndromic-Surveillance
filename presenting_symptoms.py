# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:17:02 2023

@author: hgathuri
"""

import pandas as pd
import matplotlib.pyplot as plt

#site='Busia'
for site in synd_df4['hospital'].unique():
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    ####11.	Symptoms present at admission
    site_df['presenting_symptoms'] = 'Undocumented'
    
    site_df.loc[site_df['fever'] =='Yes', 'presenting_symptoms'] = 'Fever'
    site_df.loc[site_df['cough'] =='Yes', 'presenting_symptoms'] = 'Cough'
    site_df.loc[site_df['chest_pain'] =='Yes', 'presenting_symptoms'] = 'Chest Pain'
    site_df.loc[site_df['vomiting'] =='Yes', 'presenting_symptoms'] = 'Vomiting'
    site_df.loc[site_df['diarrhoea'] =='Yes', 'presenting_symptoms'] = 'Diarrhoea'
    site_df.loc[site_df['headache'] =='Yes', 'presenting_symptoms'] = 'Headache'
    site_df.loc[site_df['difficulty_in_breathing'] =='Yes', 'presenting_symptoms'] = 'Difficulty in breathing'
    site_df.loc[site_df['abdominal_pain'] =='Yes', 'presenting_symptoms'] = 'Abdominal pain'
    site_df.loc[site_df['generalised_weakness'] =='Yes', 'presenting_symptoms'] = 'Generalised weakness'
    site_df.loc[site_df['easy_fatigability'] =='Yes', 'presenting_symptoms'] = 'Easy fatigability'
    site_df.loc[site_df['dysuria'] =='Yes', 'presenting_symptoms'] = 'Dysuria'
    site_df.loc[site_df['loss_of_consciousness'] =='Yes', 'presenting_symptoms'] = 'Altered level of consciousness'
    
    site_df.loc[site_df['other_complaint1'] =='Yes', 'presenting_symptoms'] = 'Other'
    site_df.loc[site_df['other_complaint2'] =='Yes', 'presenting_symptoms'] = 'Other'
    site_df.loc[site_df['other_complaint3'] =='Yes', 'presenting_symptoms'] = 'Other'
    site_df.loc[site_df['other_complaint4'] =='Yes', 'presenting_symptoms'] = 'Other'
    site_df.loc[site_df['other_complaint5'] =='Yes', 'presenting_symptoms'] = 'Other'
    site_df.loc[site_df['other_complaint6'] =='Yes', 'presenting_symptoms'] = 'Other'
    
    symptoms = pd.DataFrame(site_df['presenting_symptoms'].value_counts(dropna=False))
    
    ### Get percentages after dropping 'other and undocumented'
    symptoms2 = symptoms.reset_index()
    symptoms3 = symptoms2.loc[(symptoms2['presenting_symptoms']!='Other') & (symptoms2['presenting_symptoms']!='Undocumented')]
    symptoms3 = symptoms3.set_index('presenting_symptoms')
   
    symptoms3['symptoms_pct'] = round((symptoms3['count'] / symptoms3['count'].sum()) * 100)
    
    
    ### Get top 5 symptoms
    symptoms4 = symptoms3.sort_values(by='symptoms_pct', ascending=False).head(5)
    
    ##Plot
    ### Set font type
    csfont = {'fontname':'Times New Roman'}
    ax = symptoms4['symptoms_pct'].plot(kind='bar',figsize=(20,10),legend=False)
    
    #add overall title
    ax.set_title("Distribution of Presenting Symptoms at Admission", fontsize=30,**csfont)
    ax.set_xlabel('',fontsize=22)
    ax.set_xticklabels(symptoms4.index, fontsize=20, rotation=0,**csfont)
    ax.set_ylabel('Proportion (%)',fontsize=26,**csfont)
    plt.yticks(fontsize=20,**csfont)
    
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy() 
        ax.text(x+width/2, 
                y+height/2, 
                '{:.0f}%'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center',fontsize=20,**csfont,fontweight='bold')
    
    plt.savefig('Symptoms_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()
        



