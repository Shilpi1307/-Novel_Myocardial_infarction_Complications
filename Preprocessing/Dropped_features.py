"""# Dropped features from dataset for time zone 1
Relapse of the pain in the first hours of the hospital period **(R_AB_1_n)**

Relapse of the pain in the second day of the hospital period **(R_AB_2_n)**

Relapse of the pain in the third day of the hospital period **(R_AB_3_n)**

Use of opioid drugs in the ICU in the second day of the hospital period **(NA_R_2_n)**

Use of opioid drugs in the ICU in the third day of the hospital period **(NA_R_3_n)**

Use of NSAIDs in the ICU in the first hours of the hospital period **(NOT_NA_1_n)**

Use of NSAIDs in the ICU in the second day of the hospital period**(NOT_NA_2_n)**

Use of NSAIDs in the ICU in the third day of the hospital period**(NOT_NA_3_n)**

"""


df.drop(['IBS_NASL','KFK_BLOOD','ID','S_AD_KBRIG','D_AD_KBRIG'], axis = 1, inplace = True)
imputed_df.drop(['R_AB_1_n','R_AB_2_n','R_AB_3_n','NA_R_2_n','NA_R_3_n','NOT_NA_1_n','NOT_NA_2_n','NOT_NA_3_n'], axis = 1, inplace = True)


