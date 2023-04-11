# Project Overview
* This application not only allows patients to have an idea of whether they have diabetes or not but also aims to be used as an auxiliary tool in the diagnosis process of doctors.
* The data set used for the model consists of 768 rows and 9 columns. The columns are:
	* Pregnancies
	* Glucose
	* BloodPressure
	* SkinThickness
	* Insulin
	* BMI
	* DiabetesPedigreeFunction
	* Age
	* Outcome
* Built a client facing API using streamlit

# Code and Resources Used:
* **Python Version** : 3.10.9
* **Packages** : pandas,numpy,matplotlib,seaborn,sklearn,xgboost,lightgbm,pickle,streamlit and warnings

# Data Cleaning
* When I examined the variables with df.describe(), I saw that the min value of the values that could not be 0 in terms of health was 0. These variables are:
	* Glucose
	* BloodPressure
	* SkinThickness
	* Insulin
	* BMI


![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/describe.png "Describe")

* By examining the distributions of these values, I filled the 0 values with the mean and median values
![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/hist.png "Hist Graph")

* Then I drew a boxplot to examine the outliers in the variables:
![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/outlier.png "Outlier-Boxplot")

* I equated outliers to upper bound or lower bound with suppression method

# Feature Seleciton
* First I examined the relationships between the corr table and the data
* Then I visualized these relationships with a heatmap:
![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/heatmap%20.png "Heatmap")

* Then, by calling the summary function on the OLS object, I examined the significance levels of the variables for the outcome value.

![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/summary.png "OLS summary")
* As a result of the above output, I threw the skin thickness from the x variable.

* Model Building
* I used many classification algorithms in this project. These are:
	* KNN
	* Naive Bayes
	* SVM
	* Decision Tree
	* Random Forest
	* Logistic Regression
	* XGBoost
	* LightGBM
# Model Performance 
* KNN : **0.701**
* Naive Bayes : **0.746**
* SVM : **0.740**
* Decision Tree : **0.792**
* Random Forest : **0.759**
* Logistic Regression : **0.779**
* XGBoost : **0.733**
* LightGBM : **0.727**
* I chose the decision tree as the model since the highest accuracy score value came with the decision tree.

# Model Saving
* Finally, after saving the model using the pickle library, I deployed my model with the streamlit library and finally, my application outputs the information on whether there is diabetes in line with the information entered by the user.

![alt text](https://github.com/gamzeaslan/diabetes_prediction_app/blob/main/web.png "WEB")


