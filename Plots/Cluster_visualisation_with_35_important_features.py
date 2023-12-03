df_pca_clusters = pd.concat([df_pca, df_with_clusters], axis=1)
df_pca_clusters

list_cols_df_with_clusters_clean = list(df_most_relevant.columns)[0:25]
list_cols_df_with_clusters_clean

fig = px.scatter(
        df_pca_clusters,
        x=0,
        y=1,
        color="Cluster",
        hover_data=list_cols_df_with_clusters_clean
      )
fig.show();