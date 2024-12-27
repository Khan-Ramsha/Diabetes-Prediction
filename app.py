from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd
import warnings

app=Flask(__name__)

warnings.filterwarnings(action='ignore')

scaler=pickle.load(open("Model/standardScalar.pkl", "rb"))
model = pickle.load(open("Model/modelForPrediction.pkl", "rb"))

## Route for Single data point prediction
@app.route('/',methods=['GET','POST'])
def predict_data():
    result=""

    if request.method=='GET':
        
        return render_template('home.html')
    else:
        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        predict=model.predict(new_data)
       
        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result ='Non-Diabetic'
            
        return render_template('results.html',result=result)

   
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)