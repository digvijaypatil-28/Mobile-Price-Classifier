from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form.get(f)) for f in [
        'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc',
        'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores',
        'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w',
        'talk_time', 'three_g', 'touch_screen', 'wifi'
    ]]
    prediction = model.predict([features])[0]
    labels = ['Low', 'Medium', 'High']
    result = labels[prediction]
    return render_template('index.html', prediction_text=f'Price Range: {result}')

if __name__ == "__main__":
    app.run(debug=True)
