# -Novel_Myocardial_infarction_Complications
**Title**: Myocardial Infarction Complications - Phenotyping using Machine Learning

**Introduction**:
This repository contains the code and data for a research study on Myocardial Infarction (MI) complications phenotyping using machine learning techniques. The study aims to identify distinct phenotypes of patients with MI complications at the beginning of their hospital admission. By clustering patients based on their clinical features, this research seeks to enhance the understanding of different subpopulations, potentially leading to improved individualized treatment and predictive measures.

**Dataset:**
The dataset used in this study contains information on 1700 patients with myocardial infarction, collected at Krasnoyarsk Interdistrict Clinical Hospital (Russia) between 1992 and 1995. It includes 111 clinical features and 12 features related to myocardial infarction complications. The dataset is publicly available and can be downloaded from [https://archive.ics.uci.edu/dataset/579/myocardial+infarction+complications]

**Methodology:**
Detailed information on the methodology used in this study is provided in the file Preaprocessing.py & clustering.py. It includes a description of data preprocessing steps, k-means clustering algorithm, Silhouette Average Score for determining the optimal number of clusters, and the Random Forest Based Feature Selection Method (RFBFS) to identify the most relevant features associated with mortality.

**Code:**
The code is written in Python and utilizes popular machine learning libraries such as scikit-learn, pandas, and numpy.

**Results:**
The results of the clustering analysis and the identification of distinct phenotypes are presented in the file cluster.png. This section includes tables and figures showcasing the clusters' characteristics and the most relevant features associated with mortality for each cluster.

**Usage:**
To reproduce the results of this study, follow these steps:

Download the dataset from [https://archive.ics.uci.edu/dataset/579/myocardial+infarction+complications] and place it in the data directory.
Run the data preprocessing script in the code directory to handle missing values and irrelevant variables.
Execute the clustering algorithm to identify distinct phenotypes using the k-means script.
Determine the most relevant features associated with mortality using the RFBFS script.
Analyze the results and generate visualizations using the code provided.
