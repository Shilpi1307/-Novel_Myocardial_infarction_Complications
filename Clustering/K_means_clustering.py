# PCA and fitting kmeans

pca = PCA(2)
pca_np = pca.fit_transform(scaled_df)

kmeans7 = KMeans(n_clusters=5, init="k-means++", max_iter=500, n_init=10, random_state=40)
label7 = kmeans7.fit_predict(pca_np)
centroids7 = kmeans7.cluster_centers_
u_labels7 = np.unique(label7)

#feature importances in each clusters

!git clone https://github.com/YousefGh/kmeans-feature-importance
cd "kmeans-feature-importance/"
from kmeans_interp.kmeans_feature_imp import KMeansInterp
KMeansInterp
kmeans = KMeansInterp(n_clusters=5, init="k-means++", max_iter=500, n_init=10, random_state=40,
                    ordered_feature_names=df_orig.columns.to_list(),
                    feature_importance_method='wcss_min').fit(scaled_df)

# Add the cluster labels to the dataframe:
# labels = pd.DataFrame({'Cluster':label7})
# labeledDF = pd.concat((imputed_df, labels), axis = 1)
# labeledDF