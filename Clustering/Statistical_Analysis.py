"""Zero cluster"""

zero_cluster = kmeans.feature_importances_[0][:10]
zero_cluster

df_feat_importances_zero_cluster = df_with_clusters.loc[(df_with_clusters.Cluster==0),
       ['n_r_ecg_p_04','LID_S_n','ant_im', 'JELUD_TAH','n_r_ecg_p_03',
 'fibr_ter_02', 'LID_KB','lat_im','zab_leg_02','LET_IS']]

print(' ')
for i in list(df_feat_importances_zero_cluster.columns):
    print(df_feat_importances_zero_cluster[[i]].value_counts())
    print('--------------------------------------')
    print(' ')


"""first cluster"""

kmeans.feature_importances_[1][:10]

df_feat_importances_first_cluster = df_with_clusters.loc[(df_with_clusters.Cluster==1),
       ['DLIT_AG','GB','SEX','STENOK_AN','FK_STENOK','endocr_01','IBS_POST',
        'INF_ANAM']]

print(' ')
for i in list(df_feat_importances_first_cluster.columns):
    print(df_feat_importances_first_cluster[[i]].value_counts())
    print('--------------------------------------')
    print(' ')


Do the same for 2,3 & 4 clusters