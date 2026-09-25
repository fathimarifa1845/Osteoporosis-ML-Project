🦴 Osteoporosis Risk Prediction System
An end-to-end Machine Learning web application designed to predict osteoporosis risk using demographic, lifestyle, nutritional, and medical-history features.

The project covers the complete Machine Learning workflow — from data preprocessing and exploratory data analysis to model training, hyperparameter tuning, evaluation, model serialization, and Streamlit deployment.

🚀 Live Demo
🌐 Try the Application
👉[Osteoporosis Risk Prediction app](https://osteoporosis-risk-prediction-fathimarifa1.streamlit.app/)

The application can be accessed directly from a web browser on desktop or mobile devices without requiring local installation.

📌 Project Overview
🎯 Objective
Develop a Machine Learning classification model capable of predicting whether a patient is at risk of osteoporosis based on demographic, lifestyle, nutritional, and medical-history attributes.

The objective is to support early risk identification and demonstrate an end-to-end Machine Learning deployment workflow.

🧠 Machine Learning Approach
Problem Type: Binary Classification
Target Variable: Osteoporosis
Target Classes:
0 → Negative
1 → Positive
Dataset Size: 1,958 records
Input Features: 14
Identifier: Id — removed before model training
Train/Test Split: 80/20 stratified split
Preprocessing: ColumnTransformer
Numerical Processing: StandardScaler
Categorical Processing: OneHotEncoder(handle_unknown="ignore")
Class Imbalance: No SMOTE required because the target dataset is exactly balanced.
Final Model: Tuned Gradient Boosting Classifier
📊 Dataset Summary
The dataset contains demographic, lifestyle, nutritional, and medical-history information.

Dataset Dimensions
Property	Value
Rows	1,958
Columns	16
Numerical Features	1
Categorical Features	14
Identifier	1
Target	Osteoporosis
Target Distribution	50% / 50%
Features
Feature	Description
Age	Age of the patient
Gender	Gender
Hormonal Changes	Hormonal change status
Family History	Family history of osteoporosis
Race/Ethnicity	Race/Ethnicity
Body Weight	Body weight category
Calcium Intake	Calcium intake category
Vitamin D Intake	Vitamin D intake category
Physical Activity	Physical activity level
Smoking	Smoking status
Alcohol Consumption	Alcohol consumption status
Medical Conditions	Existing medical conditions
Medications	Medication information
Prior Fractures	History of previous fractures
Osteoporosis	Target variable
The Id column is an identifier and was excluded from model training.

🔄 End-to-End Machine Learning Workflow
Import Libraries
      ↓
Load Dataset
      ↓
Data Understanding
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis (EDA)
      ↓
Define Features and Target
      ↓
Train / Test Split (80/20)
      ↓
Identify Numerical & Categorical Features
      ↓
Preprocessing Pipeline
(StandardScaler + OneHotEncoder)
      ↓
Initial Model Training
      ↓
Initial Model Comparison
      ↓
Hyperparameter Tuning
(GridSearchCV on Training Data)
      ↓
Tuned Model Comparison
      ↓
Select Final Model
      ↓
Final Evaluation on Untouched Test Set
      ↓
Feature Importance Analysis
      ↓
Save Complete ML Pipeline
      ↓
Test Saved Model
      ↓
Streamlit Application
      ↓
Deployment
🧹 Data Cleaning
The following preprocessing steps were performed:

Checked dataset dimensions and data types.
Checked missing values.
Checked duplicate rows.
Checked duplicate identifiers.
Confirmed there were no duplicate rows.
Missing values were present in:
Alcohol Consumption — 988
Medical Conditions — 647
Medications — 985
Missing categorical values were replaced with:
Not Reported
The Id identifier column was removed before model training.
No SMOTE was applied because the target classes were already perfectly balanced.
📈 Exploratory Data Analysis
The EDA focused on understanding the relationship between patient characteristics and osteoporosis status.

Important visualizations included:

Target class distribution
Age distribution by osteoporosis status
Gender vs osteoporosis
Prior fractures vs osteoporosis
Physical activity vs osteoporosis
Vitamin D intake vs osteoporosis
The target distribution contained:

Osteoporosis = 0 → 979
Osteoporosis = 1 → 979
This represents an exactly balanced target dataset.

⚙️ Feature Processing
The dataset contains both numerical and categorical variables.

Numerical Feature
Age
Categorical Features
Gender
Hormonal Changes
Family History
Race/Ethnicity
Body Weight
Calcium Intake
Vitamin D Intake
Physical Activity
Smoking
Alcohol Consumption
Medical Conditions
Medications
Prior Fractures
A ColumnTransformer was used to apply different preprocessing operations.

Numerical Processing
StandardScaler
Categorical Processing
OneHotEncoder(handle_unknown="ignore")
The preprocessing was integrated into the Machine Learning pipeline to ensure that the same transformations are applied during training, testing, and Streamlit prediction.

🤖 Models Tested
Five classification algorithms were evaluated:

Logistic Regression
Decision Tree
Random Forest
Gradient Boosting
XGBoost
The initial models were compared using:

Accuracy
Precision
Recall
F1-Score
ROC-AUC
🎯 Hyperparameter Tuning
The most promising models were further optimized using:

GridSearchCV
The hyperparameter search was performed only on the training dataset using cross-validation.

Final Gradient Boosting Configuration
n_estimators = 100
learning_rate = 0.05
max_depth = 4
subsample = 0.8
Cross-Validation Performance
CV F1-Score = 0.9141
🏆 Final Model
Tuned Gradient Boosting Classifier
The final model was selected after comparing the tuned models using cross-validation on the training data.

The final evaluation was then performed on the untouched test set.

📊 Final Model Performance
Test Set
Test Samples = 392
Metric	Score
Accuracy	87.76%
Precision	98.05%
Recall	77.04%
F1-Score	86.29%
ROC-AUC	88.71%
Confusion Matrix
Predicted Negative	Predicted Positive
Actual Negative	193	3
Actual Positive	45	151
True Negatives  = 193
False Positives = 3
False Negatives = 45
True Positives  = 151
📌 Feature Importance
The final Gradient Boosting model was also analyzed to identify which input features contributed most strongly to the model's predictions.

Top Model Features
Feature	Importance
Age	94.23%
Medical Conditions — Rheumatoid Arthritis	0.42%
Race/Ethnicity — African American	0.40%
Body Weight — Underweight	0.36%
Prior Fractures — Yes	0.32%
Hormonal Changes — Postmenopausal	0.32%
Note: These values represent feature importance within this trained Machine Learning model. They should not be interpreted as clinical causal effects or as a medical diagnosis.

🖥️ Streamlit Application
The trained Machine Learning pipeline was integrated into an interactive Streamlit web application.

Application Features
Patient information input form
Interactive prediction interface
Input fields for all 14 model features
Osteoporosis prediction
Predicted risk probability
Low/high risk status display
Dynamic guidance based on prediction
User-friendly interface
Model inference using the saved complete preprocessing + classification pipeline
Application File
Streamlit application/
└── app_osteoporosis.py
🌐 Deployment
The application is deployed using:

Streamlit Community Cloud

The deployment is connected directly to the GitHub repository.

Access the Application
👉 Osteoporosis Risk Prediction app[](https://osteoporosis-risk-prediction-fathimarifa1.streamlit.app/)

Once deployed, the application can be opened from:

💻 Desktop
💻 Laptop
📱 Smartphone
📱 Tablet
No local Python environment is required for users accessing the deployed application.

📁 Project Structure
Osteoporosis/
│
├── Dataset/
│   ├── Data Dictionary.docx
│   └── osteoporosis.csv
│
├── Notebook & Saved Model/
│   ├── osteoporosis_model.pkl
│   └── Osteoporosis3.ipynb
│
├── Report/
│   └── REPORT on osteoporosis.pdf
│
├── Streamlit application/
│   └── app_osteoporosis.py
│
├── README.md
│
└── requirements.txt
📓 Jupyter Notebook
The complete Machine Learning workflow is available in:

Notebook & Saved Model/Osteoporosis3.ipynb
The notebook contains:

Data loading
Data understanding
Data cleaning
EDA
Feature preprocessing
Train/test split
Model training
Model comparison
Hyperparameter tuning
Final model evaluation
Feature importance
Model serialization
Saved-model testing
💾 Saved Machine Learning Model
The final trained model is saved as:

osteoporosis_model.pkl
The saved file contains the complete preprocessing and classification pipeline.

This allows the Streamlit application to directly load the trained pipeline and process new patient inputs using the same transformations applied during training.

📄 Project Report
The detailed project report is available here:

Report/REPORT on osteoporosis.pdf
The report covers:

Project overview
Dataset summary
Machine Learning workflow
Data preprocessing
Exploratory data analysis
Model development
Hyperparameter tuning
Final model evaluation
Feature importance
Streamlit application
Deployment
Conclusion
🛠️ Technologies Used
Programming
Python
Data Analysis
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Machine Learning
Scikit-learn
XGBoost
Model Deployment
Streamlit
Streamlit Community Cloud
Development Environment
Jupyter Notebook
Anaconda
Version Control
Git
GitHub
📦 Installation
Clone the repository:

git clone https://github.com/fathimarifa1845/Osteoporosis-ML-Project.git
Navigate to the project directory:

cd Osteoporosis-ML-Project
Create and activate your environment if required.

Install the required dependencies:

pip install -r requirements.txt
▶️ Run the Streamlit Application Locally
Navigate to the Streamlit application directory:

cd "Streamlit application"
Run:

streamlit run app_osteoporosis.py
The application will open in your default web browser.

☁️ Streamlit Community Cloud Deployment
To deploy the application publicly:

Upload the complete project to GitHub.
Sign in to Streamlit Community Cloud.
Create a new application.
Select the GitHub repository.
Select the branch containing the project.
Set the main application file to:
Streamlit application/app_osteoporosis.py
Deploy the application.
Copy the generated public URL.
Replace:
YOUR_STREAMLIT_APP_URL
in this README with the generated URL.

🩺 Important Disclaimer
This application is an educational Machine Learning project and is not a medical diagnostic tool.

The predictions generated by the application should not be used as a substitute for professional medical advice, diagnosis, or treatment.

Clinical decisions should always be made by qualified healthcare professionals using appropriate clinical evaluation and diagnostic procedures.

🔮 Future Improvements
Potential future improvements include:

Larger and more diverse clinical datasets
External validation using an independent dataset
Additional clinical biomarkers
Model explainability using SHAP
Probability calibration
More extensive hyperparameter optimization
Improved clinical risk visualization
Continuous model monitoring
API-based deployment
Cloud-based model serving
⭐ Project
If you find this project useful, feel free to explore the repository and the live application.

🦴 Osteoporosis Risk Prediction System
Machine Learning → Model Pipeline → Streamlit → Cloud Deployment
