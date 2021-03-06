#import modules
#import modules
from flask import Flask, render_template,jsonify
#from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from collections import defaultdict

#create an engine and create the reference for table in output.sqlite through ORM
engine=create_engine("sqlite:///db/output.db")
result=engine.execute("select* from Real_Estate").fetchall()

app=Flask(__name__)

@app.route("/templates/main.html")
@app.route("/")
def home_page():
    return render_template("main.html")

@app.route("/templates/hpidata.html")
@app.route("/hpidata.html")
@app.route("/hpidata")
def hpi_data():
    return render_template("hpidata.html")

@app.route("/templates/geodata.html")
@app.route("/geodata.html")
@app.route("/geodata")
def geo_data():
    return render_template("geodata.html")

@app.route("/templates/ontdata.html")
@app.route("/ontdata.html")
@app.route("/ontdata")
def ont_data():
    return render_template("ontdata.html")

@app.route("/city")
def city_list():
    city_name=[]
    for i in result:
        if i.Region not in city_name:
            city_name.append(i.Region)
    return jsonify(city_name)


@app.route("/metadata/<city>")
def city_house(city):
    metadata_city=defaultdict(list)
    for i in result:
        if i.Region==city:
            metadata_city["regionId"].append(i.Region)
            metadata_city["Date"].append(i.Date)
            metadata_city["Composite_Benchmark"].append(i.Composite_Benchmark)
            metadata_city["Single_Family_Benchmark"].append(i.Single_Family_Benchmark)
            metadata_city["One_Storey_Benchmark"].append(i.One_Storey_Benchmark)
            metadata_city["Two_Storey_Benchmark"].append(i.Two_Storey_Benchmark)
            metadata_city["Townhouse_Benchmark"].append(i.Townhouse_Benchmark)
            metadata_city["Apartment_Benchmark"].append(i.Apartment_Benchmark)
    return jsonify (metadata_city)

@app.route("/metadata")
def all_city_info():
    city_info=[]
    for i in result:
        #city_info.append([])
        #city_info[-1].append({"regionId":i.Region,"Date":i.Date})
        #city_info[-1].append({"Date":i.Date})
        #city_info[-1].append({"Composite_Benchmark":i.Composite_Benchmark})
        #city_info[-1].append({"Single_Family_Benchmark":i.Single_Family_Benchmark})
        #city_info[-1].append({"Two_Storey_Benchmark":i.Two_Storey_Benchmark})
        #city_info[-1].append({"Townhouse_Benchmark":i.Townhouse_Benchmark})
        #city_info[-1].append({"Apartment_Benchmark":i.Apartment_Benchmark})
        #metadata_allcity["regionId"].append(i.Region)
        #metadata_allcity["Date"].append(i.Date)
        #metadata_allcity["Composite_Benchmark"].append(i.Composite_Benchmark)
        #metadata_allcity["Single_Family_Benchmark"].append(i.Single_Family_Benchmark)
        #metadata_allcity["One_Storey_Benchmark"].append(i.One_Storey_Benchmark)
        #metadata_allcity["Two_Storey_Benchmark"].append(i.Two_Storey_Benchmark)
        #metadata_allcity["Townhouse_Benchmark"].append(i.Townhouse_Benchmark)
        #metadata_allcity["Apartment_Benchmark"].append(i.Apartment_Benchmark)
        metadata_allcity=defaultdict(list)
        metadata_allcity["regionId"]=i.Region
        metadata_allcity["Date"]=i.Date
        metadata_allcity["Composite_Benchmark"]=int(i.Composite_Benchmark)
        metadata_allcity["Single_Family_Benchmark"]=int(i.Single_Family_Benchmark)
        metadata_allcity["One_Storey_Benchmark"]=int(i.One_Storey_Benchmark)
        metadata_allcity["Two_Storey_Benchmark"]=int(i.Two_Storey_Benchmark)
        metadata_allcity["Townhouse_Benchmark"]=int(i.Townhouse_Benchmark)
        metadata_allcity["Apartment_Benchmark"]=int(i.Apartment_Benchmark)
        city_info.append(metadata_allcity)       
    return jsonify(city_info)

if __name__=="__main__":
    app.run(debug=True)



