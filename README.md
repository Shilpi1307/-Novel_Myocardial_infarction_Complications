# Myocardial Infarction Complications - Phenotyping using Machine Learning
## Introduction and Description
Myocardial Infarction (MI), also known as a heart attack, is a serious condition that can lead to death. It happens when blood supply to the heart is blocked, which can damage or destroy heart muscle. The risk of MI is high in all countries, but it is especially high in urban areas of developed countries. This is because people in these areas are more likely to be exposed to chronic stress, unhealthy diets, and other risk factors for MI.<br>
The course of MI can vary from person to person. Some people have no complications, while others develop complications that can worsen the condition or even lead to death. Even experienced doctors cannot always predict who will develop complications. However, it is always crucial for phenotype patients to provide them with a better individual treatment predicting complications of myocardial infarction in order to timely carry out the necessary preventive measures is an important task.<br>
The significance of this study lies in its potential to improve individualized treatment and predictive measures for patients with MI complications. By identifying distinct phenotypes, clinicians can tailor treatment strategies based on the specific characteristics and risks associated with each cluster. This information can also be valuable for future clinical trials and the development of targeted intervention.
### Dataset
https://archive.ics.uci.edu/dataset/579/myocardial+infarction+complications.
### Functioning of the models
For this research, I have used various machine learning models.<br>
There are four folders in the repository :
1. Clustering: Contains the models implemented on the dataset.
2. Images: Contains images of the clusters, elbow curve,variation of clusters w.r.t each features  and the preprocessing images .
3. Plots: Contains the code for plots using matplotlib and plotly to plot the clusters and te visualisation of datasets.
4. Preprocessing: contains the presprocessing of the datasets such that handling missing values and outliers.
### Technologies and libraries used
The contents of this repository were created and implemented in Colab notebooks & jupyter notebook.
The following libraries were majorily used:
1. Pandas
2. numpy
3. Plotly  
4. Statistics
5. scikit-learn
6. matplotlib
7. Seaborn
## Contents
1. Introduction and Description
2. Functioning of the models
3. Technologies and libraries used
4. Installations required
5. Running the scripts
6. Using the project
7. License
## Installations
1. To install [Jupyter notebok through Anaconda](https://jupyter.org/install)   
4. To install the required modules:<br>
   ```
   pip install "module name"
   ```
## Running the script
To clone this repository:<br>
   ```git
   git clone "https://github.com/Shilpi1307/-Novel_Myocardial_infarction_Complication"
   ```
## Using the project
To use the project :
1. Download the complete datasets from UCI repository.
2. The CSV dataset lacks column headers, so we need to assign names to the columns.
3. Read the csv file and start exloring the dataset try different techniques for preprocessing.
4. after analysing the dataset scale the dataset by using Standard scaler then find out the suitable number of clusters using silhoutte average score .
5. After the selection of clusters one can find theirs clusters and use clusters for statistical analysis and can find theirs phenotypes.
## License
This project is licensed under the MIT-License - Please see the LICENSE file for details.






















