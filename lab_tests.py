# -*- coding: utf-8 -*-
"""
Created on Sat May  6 14:29:15 2023

@author: hgathuri
"""
import pandas as pd
import matplotlib.pyplot as plt

#site='Busia'
for site in synd_df4['hospital'].unique():
#for site in ['Kisumu', 'Kitale']:   
    site_df = synd_df4[synd_df4['hospital']== site] 
    
    ##### 12. Laboratory tests done at admission by respective hospitals
    ### Haematology
    site_df['Full_Blood_Count'] = 0
    site_df.loc[site_df['haematology___1'] =='Checked', 'Full_Blood_Count'] = 1
                
    site_df['Haemoglobin_test'] = 0
    site_df.loc[site_df['haematology___2'] =='Checked', 'Haemoglobin_test'] = 1          
    
    ### Biochemistry
    site_df['Kidney_Function_test'] = 0
    site_df.loc[site_df['biochemistry___1'] =='Checked', 'Kidney_Function_test'] = 1             
    
    site_df['Liver_Function_test'] = 0
    site_df.loc[site_df['biochemistry___2'] =='Checked', 'Liver_Function_test'] = 1  
    
    site_df['Random_Blood_Sugar_test'] = 0
    site_df.loc[site_df['biochemistry___3'] =='Checked', 'Random_Blood_Sugar_test'] = 1 
    
    site_df['HbA1C_test'] = 0
    site_df.loc[site_df['biochemistry___4'] =='Checked', 'HbA1C_test'] = 1 
    
    site_df['Coagulation_profile'] = 0
    site_df.loc[site_df['biochemistry___8'] =='Checked', 'Coagulation_profile'] = 1 
    
    site_df['Other_Biochemistry_tests'] = 0
    site_df.loc[site_df['biochemistry___5'] =='Checked', 'Other_Biochemistry_tests'] = 1 
    
    ### Microbiology
    site_df['Urinalysis_test'] = 0
    site_df.loc[site_df['microbiology___1'] == 'Checked', 'Urinalysis_test'] = 1
    
    site_df['Urine_test'] = 0
    site_df.loc[site_df['microbiology___2'] =='Checked', 'Urine_test'] = 1
    
    site_df['Stool_test'] = 0
    site_df.loc[site_df['microbiology___5'] =='Checked', 'Stool_test'] = 1
    
    site_df['Blood_Culture_test'] = 0
    site_df.loc[site_df['microbiology___3'] =='Checked', 'Blood_Culture_test'] = 1
    
    site_df['Lumbar_Puncture'] = 0
    site_df.loc[site_df['microbiology___4'] =='Checked', 'Lumbar_Puncture'] = 1
    
    site_df['Other_Microbiology_tests'] = 0
    site_df.loc[site_df['microbiology___6'] =='Checked', 'Other_Microbiology_tests'] = 1
    
    ### Disease specific tests
    site_df['Malaria_test'] = 0
    site_df.loc[site_df['disease_specific_tests___1'] =='Checked', 'Malaria_test'] = 1
    
    site_df['Hiv_test'] = 0
    site_df.loc[site_df['disease_specific_tests___4'] =='Checked', 'Hiv_test'] = 1
    
    site_df['Covid_19_test'] = 0
    site_df.loc[site_df['disease_specific_tests___5'] =='Checked', 'Covid_19_test'] = 1
    
    site_df['TB_gene_Xpert_test'] = 0
    site_df.loc[site_df['disease_specific_tests___2'] =='Checked', 'TB_gene_Xpert_test'] = 1
    
    site_df['TB_Sputum_test'] = 0
    site_df.loc[site_df['disease_specific_tests___3'] =='Checked', 'TB_Sputum_test'] = 1
    
    site_df['CrAg_test'] = 0
    site_df.loc[site_df['disease_specific_tests___8'] =='Checked', 'CrAg_test'] = 1
    
    site_df['Other_disease_specific_tests'] = 0
    site_df.loc[site_df['disease_specific_tests___6'] =='Checked', 'Other_disease_specific_tests'] = 1
    
    ### Imaging
    #site_df['X_ray'] = 0
    #site_df.loc[site_df['routine_radiology___1'] =='Checked', 'X_ray'] = 1
    
    site_df['Ultrasound'] = 0
    site_df.loc[site_df['routine_radiology___2'] =='Checked', 'Ultrasound'] = 1
    
    #site_df['CT_Scan'] = 0
    #site_df.loc[site_df['routine_radiology___3'] =='Checked', 'CT_Scan'] = 1
    
    #site_df['MRI'] = 0
    #site_df.loc[site_df['routine_radiology___4'] =='Checked', 'MRI'] = 1
    
    #site_df['Other_imaging_tests'] = 0
    #site_df.loc[site_df['routine_radiology___6'] =='Checked', 'Other_imaging_tests'] = 1
    
    
    m1_Full_Blood_Count_df = site_df.groupby(['hospital'])['Full_Blood_Count'].sum()
    m1_Haemoglobin_test_df = site_df.groupby(['hospital'])['Haemoglobin_test'].sum()
    m1_Kidney_Function_test_df = site_df.groupby(['hospital'])['Kidney_Function_test'].sum()
    m1_Liver_Function_test_df = site_df.groupby(['hospital'])['Liver_Function_test'].sum()
    m1_Random_Blood_Sugar_test_df = site_df.groupby(['hospital'])['Random_Blood_Sugar_test'].sum()
    m1_HbA1C_test_df = site_df.groupby(['hospital'])['HbA1C_test'].sum()
    m1_Coagulation_profile_df = site_df.groupby(['hospital'])['Coagulation_profile'].sum()
    m1_Other_Biochemistry_tests_df = site_df.groupby(['hospital'])['Other_Biochemistry_tests'].sum()
    
    m1_Urinalysis_test_df = site_df.groupby(['hospital'])['Urinalysis_test'].sum()
    m1_Urine_test_df = site_df.groupby(['hospital'])['Urine_test'].sum()
    m1_Stool_test_df = site_df.groupby(['hospital'])['Stool_test'].sum()
    m1_Blood_Culture_test_df = site_df.groupby(['hospital'])['Blood_Culture_test'].sum()
    m1_Lumbar_Puncture_df = site_df.groupby(['hospital'])['Lumbar_Puncture'].sum()
    m1_Other_Microbiology_tests_df = site_df.groupby(['hospital'])['Other_Microbiology_tests'].sum()
    
    m1_Malaria_test_df = site_df.groupby(['hospital'])['Malaria_test'].sum()
    m1_Hiv_test_df = site_df.groupby(['hospital'])['Hiv_test'].sum()
    m1_Covid_19_test_df = site_df.groupby(['hospital'])['Covid_19_test'].sum()
    m1_TB_gene_Xpert_test_df = site_df.groupby(['hospital'])['TB_gene_Xpert_test'].sum()
    m1_TB_Sputum_test_df = site_df.groupby(['hospital'])['TB_Sputum_test'].sum()
    m1_CrAg_test_df = site_df.groupby(['hospital'])['CrAg_test'].sum()
    m1_Other_disease_specific_tests_df = site_df.groupby(['hospital'])['Other_disease_specific_tests'].sum()
    
    #m1_X_ray_df = site_df.groupby(['hospital'])['X_ray'].sum()
    m1_Ultrasound_df = site_df.groupby(['hospital'])['Ultrasound'].sum()
    #m1_CT_Scan_df = site_df.groupby(['hospital'])['CT_Scan'].sum()
    #m1_MRI_df = site_df.groupby(['hospital'])['MRI'].sum()
    #m1_Other_imaging_tests_df = site_df.groupby(['hospital'])['Other_imaging_tests'].sum()
    
    
    m1_lab = pd.merge(m1_Full_Blood_Count_df,m1_Haemoglobin_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Kidney_Function_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Liver_Function_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Random_Blood_Sugar_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_HbA1C_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Coagulation_profile_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Other_Biochemistry_tests_df,left_index=True,right_index=True)
    
    m1_lab = pd.merge(m1_lab,m1_Urinalysis_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Urine_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Stool_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Blood_Culture_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Lumbar_Puncture_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Other_Microbiology_tests_df,left_index=True,right_index=True)
    
    m1_lab = pd.merge(m1_lab,m1_Malaria_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Hiv_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Covid_19_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_TB_gene_Xpert_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_TB_Sputum_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_CrAg_test_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Other_disease_specific_tests_df,left_index=True,right_index=True)
    
    #m1_lab = pd.merge(m1_lab,m1_X_ray_df,left_index=True,right_index=True)
    m1_lab = pd.merge(m1_lab,m1_Ultrasound_df,left_index=True,right_index=True)
    #m1_lab = pd.merge(m1_lab,m1_CT_Scan_df,left_index=True,right_index=True)
    #m1_lab = pd.merge(m1_lab,m1_MRI_df,left_index=True,right_index=True)
    #m1_lab = pd.merge(m1_lab,m1_Other_imaging_tests_df,left_index=True,right_index=True)
    
    
    ### Separating the bars
    m1_lab.columns = m1_lab.columns.str.replace('_', ' ')
    m1_lab2 = m1_lab.T
    m1_lab2 = m1_lab2.rename(columns={site:'Investigations requested'})
    
    ### Haematology done
    site_df['Full_Blood_Count_done'] = 0
    site_df.loc[(site_df['haematology___1'] =='Checked') &
                 (site_df['full_blood_count_done'] =='Yes'), 'Full_Blood_Count_done'] = 1
                
    site_df['Haemoglobin_test_done'] = 0
    site_df.loc[(site_df['haematology___2'] =='Checked') &
               (site_df['haemoglobin_test_done'] =='Yes'), 'Haemoglobin_test_done'] = 1
           
    
    ### Biochemistry
    site_df['Kidney_Function_test_done'] = 0
    site_df.loc[(site_df['biochemistry___1'] =='Checked') &
               (site_df['kidney_function_tests_done'] =='Yes'), 'Kidney_Function_test_done'] = 1             
    
    site_df['Liver_Function_test_done'] = 0
    site_df.loc[(site_df['biochemistry___2'] =='Checked') &
               (site_df['liver_function_tests_done'] =='Yes'), 'Liver_Function_test_done'] = 1  
    
    site_df['Random_Blood_Sugar_test_done'] = 0
    site_df.loc[(site_df['biochemistry___3'] =='Checked') &
               (site_df['rbs_test_done'] =='Yes'), 'Random_Blood_Sugar_test_done'] = 1 
    
    site_df['HbA1C_test_done'] = 0
    site_df.loc[(site_df['biochemistry___4'] =='Checked') &
               (site_df['hba1c_test_done'] =='Yes'), 'HbA1C_test_done'] = 1 
    
    site_df['Coagulation_profile_done'] = 0
    site_df.loc[(site_df['biochemistry___8'] =='Checked') &
               (site_df['coagulation_profile_done'] =='Yes'), 'Coagulation_profile_done'] = 1 
    
    site_df['Other_Biochemistry_tests_done'] = 0
    site_df.loc[(site_df['biochemistry___5'] =='Checked') &
               (site_df['other_tests_done'] =='Yes'), 'Other_Biochemistry_tests_done'] = 1 
    
    ### Microbiology
    site_df['Urinalysis_test_done'] = 0
    site_df.loc[(site_df['microbiology___1'] == 'Checked') &
               (site_df['urinalysis_test_done'] =='Yes'), 'Urinalysis_test_done'] = 1
    
    site_df['Urine_test_done'] = 0
    site_df.loc[(site_df['microbiology___2'] =='Checked') &
               (site_df['urine_m_c_s_test_done'] =='Yes'), 'Urine_test_done'] = 1
    
    site_df['Stool_test_done'] = 0
    site_df.loc[(site_df['microbiology___5'] =='Checked') &
               (site_df['stool_m_c_s_test_done'] =='Yes'), 'Stool_test_done'] = 1
    
    site_df['Blood_Culture_test_done'] = 0
    site_df.loc[(site_df['microbiology___3'] =='Checked') &
               (site_df['blood_culture_test_done'] =='Yes'), 'Blood_Culture_test_done'] = 1
    
    site_df['Lumbar_Puncture_done'] = 0
    site_df.loc[(site_df['microbiology___4'] =='Checked') &
               (site_df['lp_done'] =='Yes'), 'Lumbar_Puncture_done'] = 1
    
    site_df['Other_Microbiology_tests_done'] = 0
    site_df.loc[(site_df['microbiology___6'] =='Checked') &
               (site_df['other_microbio_tests_done'] =='Yes'), 'Other_Microbiology_tests_done'] = 1
    
    ### Disease specific tests
    site_df['Malaria_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___1'] =='Checked') &
               (site_df['malaria_bs_test_done'] =='Yes'), 'Malaria_test_done'] = 1
    
    site_df['Hiv_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___4'] =='Checked') &
               (site_df['hiv_test_done'] =='Yes'), 'Hiv_test_done'] = 1
    
    site_df['Covid_19_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___5'] =='Checked') &
               (site_df['covid_19_test_done'] =='Yes'), 'Covid_19_test_done'] = 1
    
    site_df['TB_gene_Xpert_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___2'] =='Checked') &
               (site_df['tb_gene_xpert_test_done'] =='Yes'), 'TB_gene_Xpert_test_done'] = 1
    
    site_df['TB_Sputum_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___3'] =='Checked') &
               (site_df['tb_sputum_m_c_s_test_done'] =='Yes'), 'TB_Sputum_test_done'] = 1
    
    site_df['CrAg_test_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___8'] =='Checked') &
               (site_df['crag_test_test_done'] =='Yes'), 'CrAg_test_done'] = 1
    
    site_df['Other_disease_specific_tests_done'] = 0
    site_df.loc[(site_df['disease_specific_tests___6'] =='Checked') &
               (site_df['other_disease_tests_done'] =='Yes'), 'Other_disease_specific_tests_done'] = 1
    
    ### Imaging
    #site_df['X_ray_done'] = 0
    #site_df.loc[(site_df['routine_radiology___1'] =='Checked') &
    #           (site_df['specified_xray_done'] =='Yes'), 'X_ray_done'] = 1
    
    site_df['Ultrasound_done'] = 0
    site_df.loc[(site_df['routine_radiology___2'] =='Checked') &
               (site_df['specified_ultrasound_done'] =='Yes'), 'Ultrasound_done'] = 1
    
    #site_df['CT_Scan_done'] = 0
    #site_df.loc[(site_df['routine_radiology___3'] =='Checked') &
    #           (site_df['specified_ct_scan_done'] =='Yes'), 'CT_Scan_done'] = 1
    
    #site_df['MRI_done'] = 0
    #site_df.loc[(site_df['routine_radiology___4'] =='Checked') &
    #           (site_df['specified_mri_done'] =='Yes'), 'MRI_done'] = 1
    
    #site_df['Other_imaging_tests_done'] = 0
    #site_df.loc[(site_df['routine_radiology___6'] =='Checked') &
    #           (site_df['other_radiology_done'] =='Yes'), 'Other_imaging_tests_done'] = 1
    
    m1_Full_Blood_Count_done_df = site_df.groupby(['hospital'])['Full_Blood_Count_done'].sum()
    m1_Haemoglobin_test_done_df = site_df.groupby(['hospital'])['Haemoglobin_test_done'].sum()
    m1_Kidney_Function_test_done_df = site_df.groupby(['hospital'])['Kidney_Function_test_done'].sum()
    m1_Liver_Function_test_done_df = site_df.groupby(['hospital'])['Liver_Function_test_done'].sum()
    m1_Random_Blood_Sugar_test_done_df = site_df.groupby(['hospital'])['Random_Blood_Sugar_test_done'].sum()
    m1_HbA1C_test_done_df = site_df.groupby(['hospital'])['HbA1C_test_done'].sum()
    m1_Coagulation_profile_done_df = site_df.groupby(['hospital'])['Coagulation_profile_done'].sum()
    m1_Other_Biochemistry_tests_done_df = site_df.groupby(['hospital'])['Other_Biochemistry_tests_done'].sum()
    
    m1_Urinalysis_test_done_df = site_df.groupby(['hospital'])['Urinalysis_test_done'].sum()
    m1_Urine_test_done_df = site_df.groupby(['hospital'])['Urine_test_done'].sum()
    m1_Stool_test_done_df = site_df.groupby(['hospital'])['Stool_test_done'].sum()
    m1_Blood_Culture_test_done_df = site_df.groupby(['hospital'])['Blood_Culture_test_done'].sum()
    m1_Lumbar_Puncture_done_df = site_df.groupby(['hospital'])['Lumbar_Puncture_done'].sum()
    m1_Other_Microbiology_tests_done_df = site_df.groupby(['hospital'])['Other_Microbiology_tests_done'].sum()
    
    m1_Malaria_test_done_df = site_df.groupby(['hospital'])['Malaria_test_done'].sum()
    m1_Hiv_test_done_df = site_df.groupby(['hospital'])['Hiv_test_done'].sum()
    m1_Covid_19_test_done_df = site_df.groupby(['hospital'])['Covid_19_test_done'].sum()
    m1_TB_gene_Xpert_test_done_df = site_df.groupby(['hospital'])['TB_gene_Xpert_test_done'].sum()
    m1_TB_Sputum_test_done_df = site_df.groupby(['hospital'])['TB_Sputum_test_done'].sum()
    m1_CrAg_test_done_df = site_df.groupby(['hospital'])['CrAg_test_done'].sum()
    m1_Other_disease_specific_tests_done_df = site_df.groupby(['hospital'])['Other_disease_specific_tests_done'].sum()
    
    #m1_X_ray_done_df = site_df.groupby(['hospital'])['X_ray_done'].sum()
    m1_Ultrasound_done_df = site_df.groupby(['hospital'])['Ultrasound_done'].sum()
    #m1_CT_Scan_done_df = site_df.groupby(['hospital'])['CT_Scan_done'].sum()
    #m1_MRI_done_df = site_df.groupby(['hospital'])['MRI_done'].sum()
    #m1_Other_imaging_tests_done_df = site_df.groupby(['hospital'])['Other_imaging_tests_done'].sum()
    
    
    m2_lab = pd.merge(m1_Full_Blood_Count_done_df,m1_Haemoglobin_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Kidney_Function_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Liver_Function_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Random_Blood_Sugar_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_HbA1C_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Coagulation_profile_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Other_Biochemistry_tests_done_df,left_index=True,right_index=True)
    
    m2_lab = pd.merge(m2_lab,m1_Urinalysis_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Urine_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Stool_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Blood_Culture_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Lumbar_Puncture_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Other_Microbiology_tests_done_df,left_index=True,right_index=True)
    
    m2_lab = pd.merge(m2_lab,m1_Malaria_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Hiv_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Covid_19_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_TB_gene_Xpert_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_TB_Sputum_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_CrAg_test_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Other_disease_specific_tests_done_df,left_index=True,right_index=True)
    
    #m2_lab = pd.merge(m2_lab,m1_X_ray_done_df,left_index=True,right_index=True)
    m2_lab = pd.merge(m2_lab,m1_Ultrasound_done_df,left_index=True,right_index=True)
    #m2_lab = pd.merge(m2_lab,m1_CT_Scan_done_df,left_index=True,right_index=True)
    #m2_lab = pd.merge(m2_lab,m1_MRI_done_df,left_index=True,right_index=True)
    #m2_lab = pd.merge(m2_lab,m1_Other_imaging_tests_done_df,left_index=True,right_index=True)
    
    ### Separating the bars
    m2_lab.columns = m2_lab.columns.str.replace('_done', '')
    m2_lab.columns = m2_lab.columns.str.replace('_', ' ')
    m2_lab2 = m2_lab.T
    m2_lab2 = m2_lab2.rename(columns={site:'Investigations done'})
    
    ### Merging the two dfs
    m3_lab = pd.merge(m1_lab2,m2_lab2,left_index=True,right_index=True,how='outer').fillna(0)
    #m3_lab.to_csv('m3_lab.csv')
    
    ### Get percentages
    m3_lab['lab_pct'] = round((m3_lab['Investigations done'] / m3_lab['Investigations requested']) * 100).fillna(0)
    
    
    m3_lab = m3_lab.sort_values(by='Investigations requested',ascending=True).tail(10)
    #m3_lab = m3_lab.drop('lab_pct',axis=1)
    m3_lab['difference'] = m3_lab['Investigations requested'] - m3_lab['Investigations done']
    
    ### Plotting
    ### Set font type
    csfont = {'fontname':'Times New Roman'}
    # Create a stacked horizontal bar plot
    fig, ax = plt.subplots(figsize=(12,6))
    width = 0.6  # Width of the bars
    
    # Create bars for Value1
    bars1 = ax.barh(m3_lab.index, m3_lab['Investigations done'], height=width, label='Investigations done')
    
    # Create bars for Value2 on top of Value1
    bars2 = ax.barh(m3_lab.index, m3_lab['difference'], height=width, left=m3_lab['Investigations done'], label='Investigations requested')
    
    # Annotate the bars with their values
    
    for bar1, bar2, val1, val2, proportion in zip(bars1, bars2, m3_lab['Investigations done'], m3_lab['Investigations requested'], m3_lab['lab_pct']):
        ax.text(bar1.get_x() + bar1.get_width()/2, bar1.get_y() + bar1.get_height() / 2, f'{val1} ({proportion:.0f}%)', ha='center', va='center',fontsize=10, **csfont,fontweight='bold')
        ax.text(bar2.get_x() + bar2.get_width()+0.1, bar2.get_y() + bar2.get_height() / 2, f'{val2}', ha='left', va='center',fontsize=10, **csfont,fontweight='bold')
    
    # Set the axis labels and legend
    ax.set_xlabel('Count')
    ax.set_ylabel('')
    ax.legend()
    ax.set_xlabel('Count',fontsize=16,**csfont)
    plt.xticks(fontsize=16,**csfont)
    plt.yticks(fontsize=16,**csfont)
    plt.savefig('Investigations_' + site + '.png', dpi=400, bbox_inches="tight")
    plt.show()






# =============================================================================
# 
# 
# 
# 
# #### ANNOTATING WITH DIFFERENT COUNT AND PROPORTION
# 
# ### Get percentages
# m3_lab['lab_pct'] = round((m3_lab['Investigations done'] / m3_lab['Investigations requested'].sum()) * 100)
# m3_lab = m3_lab.sort_values(by='lab_pct',ascending=False)
# 
# #m3_lab.to_csv('m3_lab.csv')
# 
# ## Plot
# ### Get proportions > 0
# m3_lab = m3_lab[m3_lab['lab_pct'] > 0]
# 
# fig, ax = plt.subplots(figsize=(28, 14))
# bars = ax.bar(m3_lab.index, m3_lab['lab_pct'], tick_label=m3_lab['Investigations requested'].astype(str))
# 
# # Annotate the bars with both proportions and counts
# for bar, count, proportion in zip(bars, m3_lab['Investigations requested'], m3_lab['lab_pct']):
#     ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() /2,
#                 f'({count})\n{proportion:.0f}%',
#                 ha='center', va='center',fontsize=20, **csfont)
# 
# # Add labels and a title
# ax.set_title("Distribution of Investigations done at admission", fontsize=30,**csfont)
# ax.set_xlabel('',fontsize=22)
# ax.set_xticklabels(m3_lab.index, fontsize=20, rotation=90,**csfont)
# ax.set_ylabel('Proportion',fontsize=26,**csfont)
# plt.yticks(fontsize=20,**csfont)
# 
# # Show the plot
# plt.tight_layout()
# plt.savefig('Investigations_' + site + '.png', dpi=400, bbox_inches="tight")
# plt.show()
# 
# 
# 
# 
# 
# 
# 
# =============================================================================







# =============================================================================
#     m1_lab = m1_lab.reset_index()
#     m1_lab['Month'] = 'April'
#     
#     
#     ### Concatenate the 3 dfs
#     lab_test = m1_lab
#     
#     lab_test_cols = ['Malaria_test', 'Haematology_test',
#        'Microbiology', 'Imaging', 'Tb_test', 'Glucose_test',
#        #'Hiv_test', 'Investigations_for_urine',
#        'Investigations_for_stool', 'Covid_19_test']
#     
#     ### dropping the site name column
#     lab_test = lab_test.drop('hospital',axis=1)
#     
#     lab_test = lab_test.groupby(['Month'],sort=False)[lab_test_cols].sum()
#     
#     ##Plot
#     ax = lab_test.plot(kind='bar',figsize=(14,8))
#     
#     #add overall title
#     ax.set_title("Distribution of Investigations done at admission", fontsize=20)
#     ax.set_xlabel('',fontsize=22)
#     ax.set_ylabel('Count', fontsize=16)
#     ax.set_xticklabels('', fontsize=16, rotation=0)
#     
#     plt.yticks(fontsize=16)
#     
#     for p in ax.patches: 
#         ax.annotate(format(round(p.get_height()), '.0f'),
#                        (p.get_x() + p.get_width() / 2., p.get_height()/2),
#                        ha='center', va='center',
#                        size=14,
#                        xytext=(0, -12),
#                        textcoords='offset points')
#     
#       
#     plt.savefig('Investigations' + site + '.png', dpi=400, bbox_inches="tight")
#     plt.show()
#         
# 
# =============================================================================

# =============================================================================
# ### Separating the bars
# m1_lab.columns = m1_lab.columns.str.replace('_', ' ')
# m1_lab2 = m1_lab.T
# 
# ### Get percentages
# #m1_lab2['m1_lab_pct'] = round((m1_lab2[site] / m1_lab2[site].sum()) * 100)
# 
# ### dropping the count('Kakamega') column
# # m1_lab3 = m1_lab2.drop(site,axis=1)
# 
# ##Plot
# ax = m1_lab2.plot(kind='bar',figsize=(16,10),legend=False)
# 
# #add overall title
# ax.set_title("Distribution of Investigations done at admission", fontsize=30,**csfont)
# ax.set_xlabel('',fontsize=22)
# ax.set_xticklabels(m1_lab2.index, fontsize=20, rotation=90,**csfont)
# ax.set_ylabel('Count',fontsize=26,**csfont)
# plt.yticks(fontsize=20,**csfont)
# 
# for p in ax.patches:
#     width, height = p.get_width(), p.get_height()
#     x, y = p.get_xy() 
#     ax.text(x+width/2, 
#             y+height/2, 
#             '{:.0f}'.format(height), 
#             horizontalalignment='center', 
#             verticalalignment='center',fontsize=20,**csfont)
# 
# plt.savefig('Investigations_' + site + '.png', dpi=400, bbox_inches="tight")
# plt.show()
#     
# 
# =============================================================================
