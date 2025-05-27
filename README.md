## 📱 Mobile Price Range Prediction - Flask App

This is a web application built using Flask that predicts the price range (Low, Medium, High) of a mobile phone based on user-input features. The machine learning model is pre-trained and loaded using pickle.

## Demo 

Click on this link to see demo of the project: https://mobile-price-classifier.onrender.com

## 🔧 Features

Predicts mobile price category (Low, Medium, High)
Takes 20 inputs related to phone specifications
Clean and simple HTML front-end (index.html)
Backend logic using Flask
Pre-trained model loaded with pickle

## 🚀 How to Run the Project

1. Clone the Repository
git clone https://github.com/your-username/mobile-price-predictor.git
cd mobile-price-predictor

2. Install Required Libraries
Make sure you have Python installed. Then install dependencies:
pip install flask numpy
If using a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install flask numpy

3. Add Files
Make sure the following files are in the project directory:
app.py (your main Flask script)
model.pkl (your trained model)
templates/index.html (HTML form)

4. Run the Flask App
python app.py
The app will run at: http://127.0.0.1:5000/

## 📥 Input Features

The following 20 features are required as input:
Feature	Description
battery_power	Battery capacity (mAh)
blue	Bluetooth (0 or 1)
clock_speed	Processor speed (GHz)
dual_sim	Supports dual SIM (0 or 1)
fc	Front camera (MP)
four_g	Supports 4G (0 or 1)
int_memory	Internal memory (GB)
m_dep	Mobile depth (cm)
mobile_wt	Weight of mobile (grams)
n_cores	Number of cores in processor
pc	Primary camera (MP)
px_height	Pixel height
px_width	Pixel width
ram	RAM (MB)
sc_h	Screen height (cm)
sc_w	Screen width (cm)
talk_time	Battery talk time (hours)
three_g	Supports 3G (0 or 1)
touch_screen	Is touch screen (0 or 1)
wifi	Supports WiFi (0 or 1)

## 🧠 Model Info

The model is trained on a dataset with mobile specifications and their corresponding price ranges.
model.pkl is a pre-trained machine learning model (like Decision Tree, Random Forest, etc.).

## 📁 Project Structure

mobile-price-predictor/
│
├── app.py
├── model.pkl
├── README.md
└── templates/
    └── index.html
## 📜 License

This project is open-source and free to use. You can modify and enhance it for learning or development purposes.
