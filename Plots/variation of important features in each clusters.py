age_cluster = df_pca_clusters[["AGE","Cluster"]]
n_clusters = len(age_cluster['Cluster'].unique())
n_cols = int(np.ceil(np.sqrt(n_clusters)))
n_rows = int(np.ceil(n_clusters / n_cols))

# Create the figure and axis objects
fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 8),
                       gridspec_kw={'wspace':0.6, 'hspace':0.5})
ax = ax.flatten()
plt.suptitle("AGE", fontsize=18, y=0.95)

# Plot the histograms
for i, label in enumerate(sorted(age_cluster['Cluster'].unique())):
    cluster = age_cluster[age_cluster['Cluster'] == label]['AGE']
    sns.histplot(cluster, ax=ax[i], kde=True, color='b')
    ax[i].set_title(f'cluster {int (label)} ({len(cluster)} instances)')
    ax[i].set_xlabel("AGE")
    ax[i].set_ylabel("Count")
# Hide unused subplots
for i in range(n_clusters, n_rows * n_cols):
    ax[i].axis('off')

# Show the plot
plt.show()


stenok_cluster = df_pca_clusters[["STENOK_AN","Cluster"]]
n_clusters = len(stenok_cluster['Cluster'].unique())
n_cols = int(np.ceil(np.sqrt(n_clusters)))
n_rows = int(np.ceil(n_clusters / n_cols))

# Create the figure and axis objects
fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 8),
                       gridspec_kw={'wspace':0.6, 'hspace':0.5})
ax = ax.flatten()
plt.suptitle("STENOK_AN", fontsize=18, y=0.95)

# Plot the histograms
for i, label in enumerate(sorted(stenok_cluster['Cluster'].unique())):
    cluster = stenok_cluster[stenok_cluster['Cluster'] == label]['STENOK_AN']
    sns.histplot(cluster, ax=ax[i], kde=True, color='b')
    ax[i].set_title(f'cluster {int (label)} ({len(cluster)} instances)')
    ax[i].set_xlabel("STENOK_AN")
    ax[i].set_ylabel("Count")
# Hide unused subplots
for i in range(n_clusters, n_rows * n_cols):
    ax[i].axis('off')

# Show the plot
plt.show()



fk_cluster = df_pca_clusters[["FK_STENOK","Cluster"]]
n_clusters = len(fk_cluster['Cluster'].unique())
n_cols = int(np.ceil(np.sqrt(n_clusters)))
n_rows = int(np.ceil(n_clusters / n_cols))

# Create the figure and axis objects
fig, ax = plt.subplots(n_rows, n_cols, figsize=(10, 8),
                       gridspec_kw={'wspace':0.6, 'hspace':0.5})
ax = ax.flatten()
plt.suptitle("FK_STENOK", fontsize=18, y=0.95)

# Plot the histograms
for i, label in enumerate(sorted(fk_cluster['Cluster'].unique())):
    cluster = fk_cluster[fk_cluster['Cluster'] == label]['FK_STENOK']
    sns.histplot(cluster, ax=ax[i], kde=True, color='b')
    ax[i].set_title(f'cluster {int (label)} ({len(cluster)} instances)')
    ax[i].set_xlabel("FK_STENOK")
    ax[i].set_ylabel("Count")
# Hide unused subplots
for i in range(n_clusters, n_rows * n_cols):
    ax[i].axis('off')

# Show the plot
plt.show()


Do the same for remainng important features of clusters