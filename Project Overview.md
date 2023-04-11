**Project Overview:**

-   This application not only allows patients to have an idea of whether they have diabetes or not but also aims to be used as an auxiliary tool in the diagnosis process of doctors.
-   The data set used for the model consists of 768 rows and 9 columns. The columns are:
    -   Pregnancies
    -   Glucose
    -   BloodPressure
    -   SkinThickness
    -   Insulin
    -   BMI
    -   DiabetesPedigreeFunction
    -   Age
    -   Outcome
-   Built a client facing API using streamlit

**Code and Resources Used:**

-   Python Verison:3.10.9
-   Packages:pandas,numpy,matplotlib,seaborn,sklearn,xgboost,lightgbm,pickle,stramlit and warnings

**Data Cleaning:**

-   When I examined the variables with df.describe(), I saw that the min value of the values that could not be 0 in terms of health was 0. These variables are:
    -   Glucose
    -   BloodPressure
    -   SkinThickness
    -   Insulin
    -   BMI

![](media/8ce261f2408d5fb6aa7a93fee19382a5.png)

-   By examining the distributions of these values, I filled the 0 values with the mean and median values

    ![](media/8b4f08b553e92b79f940d7c17b31a529.png)

-   Then I drew a boxplot to examine the outliers in the variables:

    ![](media/aea9c86a3b1823b6d8e62e4fb620245d.png)

-   I equated outliers to upper bound or lower bound with suppression method

Feature Selection :

-   First I examined the relationships between the corr table and the data
-   Then I visualized these relationships with a heatmap:

    ![](media/1b3fec464055c722376f72bd79efa8bf.png)

-   Then, by calling the summary function on the OLS object, I examined the significance levels of the variables for the outcome value.

    ![](media/b6845926d2bc23e80c34f10c3af4e83d.png)

-   As a result of the above output, I threw the skin thickness from the x variable.

Model Building:

-   I used many classification algorithms in this project. These are:
    -   KNN
    -   Naive Bayes
    -   Decision Tree
    -   Random Forest
    -   Logistic Regression
    -   XGBoost
    -   LightGBM

Model Performence :

-   Based on accuracy score:
    -   **KNN:** 0.7012987012987013
    -   **Naive Bayes**0.7467532467532467
    -   **SVM:**0.7402597402597403
    -   **Decision Tree**0.7922077922077922,
    -   **Random Forest** 0.7597402597402597
    -   **Logistic Regression**0.7792207792207793
    -   **XGBoost**0.7337662337662337
    -   **Light GBM**0.7272727272727273
-   I chose the decision tree as the model since the highest accuracy score value came with the decision tree.

Model Saving:

-   **Finally, after saving the model using the pickle library, I deployed my model with the streamlite library and finally, my application outputs the information on whether there is diabetes in line with the information entered by the user.**

![](media/b12eccd88c13915e5b4322d04b310814.png)
