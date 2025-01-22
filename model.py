import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model(file_path):
    
    data = pd.read_csv(file_path)
    X = data[['Coolant_Temperature', 'Hydraulic_Pressure(bar)', 'Coolant_Pressure(bar)', 'Air_System_Pressure(bar)','Spindle_Vibration(?m)','Cutting(kN)','Torque(Nm)','Voltage(volts)','Spindle_Speed(RPM)']]
    y = data['Downtime']
    
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    

    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

   
    joblib.dump(model, './model.pkl')

    return acc, f1

def make_prediction(data):
    model = joblib.load('./model.pkl')
    prediction = model.predict([list(data.values())])
    return {"Downtime": "Yes" if prediction[0] == 1 else "No"}
