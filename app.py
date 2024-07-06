from flask import Flask, render_template, url_for, request, jsonify
import joblib
model = joblib.load('linear_regression_model.lb')

app = Flask(__name__)

@app.route('/')   
def home():
    return render_template('home.html')

@app.route('/user_data')
def user_data():
    return render_template('user_data.html')

#POST
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        brand_name = request.form['brand_name']
        Kms_Driven = request.form['Kms_Driven']
        owner = request.form['owner']
        age = request.form['age']
        power = request.form['power']

        user_data = [[owner, brand_name, Kms_Driven, age, power]]
        pred = model.predict(user_data)[0][0]

        # return jsonify(user_data)
        prediction = str(round(pred, 2))
        return render_template('user_data.html', prediction_text=prediction)

    
if __name__ =="__main__":
    app.run(debug=True)     