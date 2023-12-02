from flask import Flask, render_template, request
from function import airplane, places, sub_date, hotel
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

user_information = dict()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        global result
        result = request.form
        # r_key = []
        # for keys, values in result.items():
        #     r_key.append(keys)
        #     user_information.append(values)
        # df = pd.DataFrame(user_information)
        # print(user_information)
        position = airplane(result)  # 지역 명소
        # d(result) # 날짜 계산
        return render_template("airplane.html", result=position)
    else:
        return render_template("airplane.html")


@app.route("/a", methods=["GET", "POST"])
def test1():
    if request.method == "POST":
        position = places(result["place"])  # 지역 명소

        return render_template("places.html", result=position)


@app.route("/b", methods=["GET", "POST"])
def test2():
    if request.method == "POST":
        position = hotel(result)  # 지역 명소

        return render_template("places.html", result=position, to=result)


if __name__ == "__main__":
    app.run(debug=True)
