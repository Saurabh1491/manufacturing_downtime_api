git clone <repository_url>
cd <project_folder>
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt


# Upload CSV
curl -X POST -F "file=@data.csv" http://localhost:5000/upload

# Train Model
curl -X POST http://localhost:5000/train

# Prediction
curl -X POST -H "Content-Type: application/json" -d '{"Hydraulic_Pressure(bar)":71.04,"Coolant_Pressure(bar)":6.933724915,"Air_System_Pressure(bar)":6.284964506,"Coolant_Temperature":25.6,"Spindle_Vibration(?m)":1.291,"Spindle_Speed(RPM)":25892.0,"Voltage(volts)":335.0,"Torque(Nm)":24.05532601,"Cutting(kN)":3.58}' http://localhost:5000/predict
