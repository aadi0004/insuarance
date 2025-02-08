from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import pickle
import mysql.connector

app = Flask(__name__)

conn= mysql.connector.connect(host = 'localhost' , 
                               user = 'root' , 
                               password = '' , 
                               database = 'insurancedata')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('forms.html') 

@app.route('/submit_data', methods=['POST'])
def submit_data():
    try:
        age = request.form.get('age')
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        data=[[age, sex, bmi, children, smoker, region]]
        

        input_=pd.DataFrame(data,columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
        
        with open("insurance-ML-main/model/best_model.pkl","rb") as file:
            pipeline=pickle.load(file)
        print(input_)    
        pred=pipeline.predict(input_)
        print(pred)
        
        cursor=conn.cursor()
        query = """
            INSERT INTO insurance (age,sex,bmi,children,smoker,region,charges) 
            VALUES (%s, %s, %s, %s, %s, %s,%s)
        """
        values = (age, sex, bmi, children, smoker, region,float(pred[0]))

        try:
            cursor.execute(query, values)
            conn.commit()  
            print("Data stored successfully in MySQL")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            
            
        return jsonify({'prediction': f"${pred[0]:.2f}"})


    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
