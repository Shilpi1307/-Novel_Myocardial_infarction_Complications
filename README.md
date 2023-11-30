# -Novel_Myocardial_infarction_Complications
**Title**: Myocardial Infarction Complications - Phenotyping using Machine Learning

**Introduction**:

# Hypertensive-Retinopathy
## Introduction and Description
Hypertensive Retinopathy (HR) is a type of retinal damage caused by high blood pressure and Hypertension and prompts vision loss. HR is generally diagnosed at a later stage of illness when the retinal damage starts affecting the vision. The HR damages the pathological lesions of eyes including arteriolar narrowing, retinal hemorrhage, macular edema, cotton wool spots and swollen blood vessels. If detected at an early stage, the effect can be reversed. Therefore, it is essential for Patients of Hypertension to get their eyes checked regularly.<br>
The analysis of HR mostly relies on manual inspection and experience of the ophthalmologists. Hence, a Deep Learning based approach is necessary to assist ophthalmologists to analyze the progression of disease. 
### Datasets
1. [Hypertensive Retinopathy Detection competition Dataset](https://codalab.lisn.upsaclay.fr/competitions/11877#participate-get-data).
2. [Ocular Disease Intelligent Recognition (ODIR)](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k).
3. [1000 Fundus images](https://www.kaggle.com/datasets/linchundan/fundusimage1000).
### Functioning of the models
For this research, I have used various deep learning and machine learning models.<br>
There are four folders in the repository :
1. Models: Contains the models implemented on the dataset.
2. Images: Contains some of the images from the original dataset to run tests.
3. Plots: Contains the code for plots using matplotlib to track the traing and performance on the model.
4. Tests: contains the unttest files for Resnet50 and random forest.
### Technologies and libraries used

The contents of this repository were created and implemented in Python IDLE 3.10.10 and Jupyter notebook in Visual Studio .
The following libraries were majorily used:
1. Pandas
2. numpy
3. tensorflow
4. keras
5. scikit-learn
6. matplotlib
## Contents
1. Introduction and Description
2. Functioning of the models
3. Technologies and libraries used
4. Installations required
5. Running the scripts
6. Using the project
7. License
## Installations
1. To install [python 3.10.x](https://www.python.org/downloads/)
2. To install [Visual Studio Code](https://code.visualstudio.com/download)
3. To install [Jupyter notebok through Anaconda](https://jupyter.org/install)   
4. To install the required modules:<br>
   ```
   pip install "module name"
   ```
## Running the script
To clone this repository:<br>
   ```git
   git clone "https://github.com/KesharwaniArpita/Hypertensive-Retinopathy"
   ```
## Using the project
To use the project :
1. Download the complete datasets.
2. Set apart a portion of images as test from thewhole datasets .
3. Provide the paths to the training folder, test folder and groundtruth excel file to the models .
4. The models will be trained to the traing images and same the weights from traing in an .h5 file to the location where your scipt is saved.
5. After the first time, one can train the model using those weights and can make predictions too.
## License
This project is licensed under the MIT-License - Please see the LICENSE file for details.



































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
