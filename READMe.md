# Insurance Cost Prediction using Flask & Machine Learning
    # Overview

        This project is a Flask-based web application that predicts insurance costs based on user input. It uses a trained machine learning model, applies one-hot encoding for categorical features or standard scaler on numerical data ,combine all of the process inta a pipeline and make a pickle file from this file result is showing on a web interface.

    # Installation & Setup

        1. Clone the Repository

        git clone https://github.com/GAURAV-ERA/Insurance.git

        2. Create &  Activate a Virtual Environment

        python -m venv env
        source env/bin/activate   # On Mac/Linux
        env\Scripts\activate      # On Windows

        3. Install Dependencies

        pip install -r requirements.txt

        4. Run the Flask App
        
        python app.py

    # Web Interface

        1. index.html (Home Page)

        Displays an introduction and a form for user input.

        2. form.html (User Input Form)

        Accepts numerical & categorical inputs.
        Form fields: age, bmi, children, sex, smoker, region.

        3. result.html (Prediction Output)

        Displays the predicted insurance cost.


    # API Endpoints

        1. Home Page (/)

        Method: GET

        Description: Renders index.html


        2. form page (/forms)

        method: GET

        3. Prediction (/predict)

        Method: POST

        Description: fetch user input from form,make dataframe if input data, load pickle file, make prediction  and return(render) result in result.html
    
    # Machine Learning Model

        Algorithm: Linear regression,Decision Tree Regressor and Random Forest Regressor

        Preprocessing: OneHotEncoder, StandardScaler

        Training Data: insurance.csv

        Pipeline Components: Categorical Encoding: OneHotEncoder, Feature Scaling: StandardScaler

        Best Model : Random Forest Regressor
        

    # Model Pipeline

        The machine learning pipeline is structured as follows:

        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
        from sklearn.linear_model import LinearRegression
        from sklearn.compose import ColumnTransformer
        import pandas as pd
        import pickle

        # Define categorical and numerical features
        categorical_features = ['sex', 'smoker', 'region']
        numerical_features = ['age', 'bmi', 'children']

        # Define preprocessing steps
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ]
        )

        # Create the pipeline
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('model', LinearRegression())
        ])

        # Load dataset and train model
        df = pd.read_csv('insurance.csv')
        X = df.drop(columns=['charges'])
        y = df['charges']

        pipeline.fit(X, y)

         # Save and load the trained model

        with open('model.pkl', 'wb') as file:
            pickle.dump(pipeline, file)

        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)

    # Technologies Used

        1.Python (Flask, Pandas, NumPy, Scikit-learn)
        2.HTML/CSS 
        3.pickle

    # Contact & Contributions

        Author: Gaurav Jangid
        GitHub: https://github.com/Gauravjangid26
        Email: gauravjangid341542@gmail.com



