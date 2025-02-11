from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import pickle
import mysql.connector
import os

app = Flask(__name__)

# Determine if running inside Docker
if os.getenv("DOCKER_ENV"):
    DB_HOST = "host.docker.internal"  # Use this in Docker
else:
    DB_HOST = "localhost"  # Use this when running locally

DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "insurancedata"

# MySQL connection with auto-reconnect
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

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
        data = [[age, sex, bmi, children, smoker, region]]

        input_ = pd.DataFrame(data, columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        with open("model/best_model.pkl", "rb") as file:
            pipeline = pickle.load(file)

        print(input_)    
        pred = pipeline.predict(input_)
        print(pred)

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO insurance (age, sex, bmi, children, smoker, region, charges) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (age, sex, bmi, children, smoker, region, float(pred[0]))

        try:
            cursor.execute(query, values)
            conn.commit()
            print("Data stored successfully in MySQL")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            conn.close()

        return jsonify({'prediction': f"${pred[0]:.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
