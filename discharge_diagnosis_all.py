# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:02:56 2023

@author: hgathuri
"""
import numpy as np

diag_cols = ['discharge_diagnosis_1','discharge_diagnosis_2','discharge_diagnosis_3',
             'discharge_diagnosis_4','discharge_diagnosis_5', 'discharge_diagnosis_6',
             'discharge_diagnosis_7','discharge_diagnosis_8']

#Getting the frequency of diagnosis per site 
disch_diag = synd_df2.groupby('hospital').agg({i:'value_counts' for i in synd_df2[diag_cols]})

disch_diag['discharge_diagnosis_count'] = disch_diag.sum(axis=1, numeric_only=True)

# Groupby using DataFrame.agg() Method.
disch_diag2 = disch_diag.reset_index()
disch_diag3 = disch_diag2.sort_values(by=['hospital','discharge_diagnosis_count'],ascending = [True,False])

disch_diag4 = disch_diag3[['hospital', 'level_1', 'discharge_diagnosis_count']]

disch_diag4 = disch_diag4.loc[disch_diag4['level_1']!='None']

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
#disch_diag5.to_excel('disch_diag51.xlsx',index=False)


### Get top 5 in every site
disch_diag6 = disch_diag5.groupby('hospital').head(3)


#disch_diag5.to_csv('test1.csv')

disch_diag7 = disch_diag6.pivot(index='hospital', 
                                     columns='diagnosis_grouped', 
                                     values='discharge_diagnosis_count').fillna(0)

#disch_diag5.to_excel('disch_diag51.xlsx',index=False)
#disch_diag6.to_csv('disch_diag6.csv')

### Plotting
# =============================================================================
# ax = disch_diag7.plot(kind='bar',figsize=(24,12), stacked=True,
#                       color=['#ff7f0e', '#2ca02c', '#d62728', '#1f77b4',
#                               '#FFA500','#9DFFCA','#CAFF9D', '#CA9DFF',
#                               '#7F0EFF', '#A6A64C','#EF48A8', '#0E7FFF'])
# =============================================================================


ax = disch_diag7.plot(kind='bar',figsize=(24,12), stacked=True)


#add overall title
#ax.set_title("Distribution of Top 10 discharge diagnosis by study sites", fontsize=24)
ax.set_xlabel('',fontsize=22)
ax.set_xticklabels(disch_diag7.index, fontsize=16, rotation=0)
##removes the title appearing in legend
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles=handles[1:], labels=labels[1:])
#ax.set_ylabel('Frequency',fontsize=22)
plt.yticks(fontsize=16)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=2, fontsize=16)

plt.savefig('discharge_diagnosis_top3_all4.png', dpi=400, bbox_inches="tight")
plt.show()




####Changing colors
# =============================================================================
# 
# overlap = {name for name in mcolors.CSS4_COLORS
#            if f'xkcd:{name}' in mcolors.XKCD_COLORS}
# 
# ax = disch_diag6.plot(kind='bar',figsize=(24,12), stacked=True,color=overlap)
# #NUM_COLORS = len(disch_diag6.columns)
# #add overall title
# #ax.set_title("Distribution of Top 10 discharge diagnosis by study sites", fontsize=24)
# ax.set_xlabel('',fontsize=22)
# ax.set_xticklabels(disch_diag6.index, fontsize=16, rotation=0)
# #cm = plt.get_cmap('gist_rainbow')
# #ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
# ##removes the title appearing in legend
# #handles, labels = ax.get_legend_handles_labels()
# #ax.legend(handles=handles[1:], labels=labels[1:])
# #ax.set_ylabel('Frequency',fontsize=22)
# plt.yticks(fontsize=16)
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
#           fancybox=True, shadow=True, ncol=2, fontsize=14)
# 
# #plt.savefig('disch_diag_top5_kiambu.png', dpi=400, bbox_inches="tight")
# plt.show()
# =============================================================================
