
import pickle
import numpy as np
from flask import Flask, render_template, request
 
#/Users/yunsu/seoul_mosquito_status_project/model/prediction_model_211007.pickle
app = Flask(__name__)
model = pickle.load(open("seoul_mosquito_status_project/model/model_211007.pickle","rb"))

#메인 페이지 라우팅
@app.route("/")
def base():
    return render_template("home.html")

#데이터 예측처리
@app.route("/predict",methods=["GET","POST"])
def make_prediction():

    avg_temp = request.form['avg_temp']
    min_temp = request.form['min_temp']
    max_temp = request.form['max_temp']
    precipitation = request.form['precipitation']

    arr = np.array([[avg_temp, min_temp, max_temp, precipitation]])
    pred = model.predict(arr)
        
    return render_template("results.html", data=pred) 

if __name__ == '__main__':
    app.run(debug=True)