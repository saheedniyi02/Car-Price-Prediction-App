# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask,render_template,request,flash
import pickle
import os

app=Flask(__name__)
app.config["SECRET_KEY"]="45554134536334ttrt565'
Model = pickle.load(open('model.pkl','rb'))

@app.route("/",methods=["POST","GET"])
@app.route("/predict",methods=['POST','GET'])
def predict():
	if request.method=="POST":
		mileage=int(request.form.get("mileage"))
		location=int(request.form.get('location'))
		year=int(request.form.get("Year"))
		transmission=int(request.form.get("Transmission"))
		condition=int(request.form.get("Condition"))
		fuel_type=int(request.form.get("FuelType"))
		make=int(request.form.get("Make"))
		model=int(request.form.get("Model"))
		data=[[model,year,condition,transmission,fuel_type,location,mileage,make]]
		prediction=Model.predict(data)[0]
		output=round(prediction,-3)
		flash(f"The price of the car is {output}","success")
	return render_template("index.html")

if __name__=="__main__":
	app.run()
