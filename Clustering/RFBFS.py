# This file contains most important features(selection criteria-RFBFS) of whole dataset w.r.t each clusters 
x = df_orig.iloc[:,0:110]
y = df_orig.iloc[:,110:]

rf_for_feature_selection = RandomForestClassifier(n_estimators = 100 , random_state = 3)
sel = SelectFromModel(rf_for_feature_selection)
sel.fit(x, y)

selected_feat= x.columns[(sel.get_support())]
print(selected_feat)
print(sel.estimator_)
print(sel.threshold_)
print(sel.estimator_.feature_importances_)
sum(sel.estimator_.feature_importances_) / 111