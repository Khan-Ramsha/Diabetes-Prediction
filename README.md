## 🩺 Diabetes Prediction Flask App
This repository contains a Flask web application for predicting diabetes using a trained Decision Tree model. The application accepts user inputs through a form, processes the inputs, and displays the prediction results.

### Project Overview

The application predicts whether a person is diabetic or non-diabetic based on the following input features:

🤰 Pregnancies

🍬 Glucose

💉 BloodPressure

🧴 SkinThickness

💉 Insulin

🏋️‍♀️ BMI

📈 DiabetesPedigreeFunction

🎂 Age

The prediction model is trained using a Decision Tree classifier, which provided the best accuracy compared to other models like Naive Bayes and SVC.

### Features

🏠 Home Page: A form for users to input their health data.

🔍 Prediction: Displays whether the user is diabetic or non-diabetic based on the input data.

### Technologies Used

🌐 Flask: A lightweight WSGI web application framework in Python.

🧠 scikit-learn: Machine learning library for model training and prediction.

📦 Pickle: For model serialization and deserialization.

🚀 GitHub Actions: For CI/CD to build, test, and deploy the application.

🌍 Render: For hosting the live application.

### Installation

Clone the repository:

```
git clone https://github.com/yourusername/diabetes-prediction-flask-app.git
cd diabetes-prediction-flask-app
```
Install the required packages:

```
pip install -r requirements.txt
```
Place the modelForPrediction.pkl and standardScalar.pkl files in the Model directory.

Usage
Run the Flask application:

```
python app.py
```
Open your web browser and go to http://localhost:5000 to access the application.

## Deployment

This application is deployed using Render. You can view the live app here- https://flask-diabetes-prediction-app.onrender.com/

### CI/CD with GitHub Actions

GitHub Actions is used to automate the build, test, and deployment process. The workflow file is defined in .github/workflows/deploy.yml.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
