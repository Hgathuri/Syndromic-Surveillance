# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:40:17 2023

@author: hgathuri
"""

s = synd_df4.groupby('hospital')['date_of_entry'].count().reset_index()
s = s.rename(columns={'hospital': 'Hospital','date_of_entry':'Patients Discharged'})


# =============================================================================
# #### Getting Kilifi's discharges
# k = kilifi_df1.groupby('redcap_data_access_group')['serial'].count().reset_index()
# k = k.rename(columns={'redcap_data_access_group': 'Hospital',
#                         'serial':'Patients Discharged'})
# 
# ### Concatenate the two dfs
# s2 = pd.concat([s,k])
# 
# ### Exclude CGTRH
# s2 = s2[s2['Hospital'] != 'CGTRH']
# 
# s2 = s2.set_index('Hospital')
# 
# ### Adjusting 
# #s2.loc['Kitale'] = s2.loc['Kitale'] - 4
# 
# =============================================================================

s2 = s
s2 = s2.set_index('Hospital')
#s2 = s2.set_index('Hospital').drop('CGTRH')
### Set font type
csfont = {'fontname':'Times New Roman'}

ax = s2.plot(kind='bar',figsize=(26,12),legend=False)

#add overall title
ax.set_title("Distribution of discharges in January by study site", fontsize=40,**csfont)
ax.set_xlabel('Study site',fontsize=26,**csfont)
ax.set_xticklabels(s2.index, fontsize=20, rotation=0,**csfont)
plt.yticks(fontsize=20,**csfont)
ax.set_ylabel('Number of patients',fontsize=26,**csfont)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.text(x+width/2, 
            y+height/2, 
            '{:.0f}'.format(height), 
            horizontalalignment='center', 
            verticalalignment='center',fontsize=22,**csfont,fontweight='bold')
    
plt.savefig('patients_discharged_by_site.png', dpi=400, bbox_inches="tight")
plt.show()



