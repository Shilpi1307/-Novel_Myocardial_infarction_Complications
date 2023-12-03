# calculate k using python, with the elbow method
inertia = []
# define our possible k values
possible_K_values = [i for i in range(2,40)]
# we start with 2, as we can not have 0 clusters in k means, and 1 cluster is just a dataset
# iterate through each of our values
for each_value in possible_K_values:
    # iterate through, taking each value from
    model = KMeans(n_clusters=each_value, init='k-means++',random_state=32)
    # fit it on YOUR dataframe
    model.fit(df_orig)
    # append the inertia to our array
    inertia.append(model.inertia_)
plt.plot(possible_K_values, inertia)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()


# new model
model = KMeans(n_clusters=15, init='k-means++',random_state=32)
# re-fit our model
model.fit(scaled_df)
# compute an average silhouette score for each point
silhouette_score_average = silhouette_score(scaled_df, model.predict(scaled_df))
# lets see what that score it
print(silhouette_score_average)
# while that's nice, what does that tell us? there could still be a points with a negative value
# let's see the points
silhouette_score_individual = silhouette_samples(scaled_df, model.predict(scaled_df))
# iterate through to find any negative values
for each_value in silhouette_score_individual:
    if each_value < 0:
       print(f'We have found a negative silhouette score: {each_value}')


# re-do our loop, try to find values with no negative scores, or one with the least!!
bad_k_values = {}

possible_K_values = [i for i in range(5,20)]

# iterate through each of our values
for each_value in possible_K_values:

    # iterate through, taking each value from
    model = KMeans(n_clusters=each_value, init='k-means++',random_state=32)
    # fit it
    model.fit(scaled_df)
    # find each silhouette score
    silhouette_score_individual = silhouette_samples(scaled_df, model.predict(scaled_df))
    # iterate through to find any negative values
    for each_silhouette in silhouette_score_individual:
        # if we find a negative, lets start counting them
        if each_silhouette < 0:
            if each_value not in bad_k_values:
                bad_k_values[each_value] = 1
            else:
                bad_k_values[each_value] += 1
for key, val in bad_k_values.items():
    print(f' This Many Clusters: {key} | Number of Negative Values: {val}')


