from flask import Flask, request, make_response, session, render_template, redirect, url_for, sessions
import xml.etree.ElementTree as ET
import numpy as np
import os, glob, random
from sklearn.naive_bayes import GaussianNB
import datetime
import pdfkit

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

def pass_data(data):
    files = glob.glob(os.path.join("data/", "*.xml"))
    # print(files)
    # tree = []
    root = []
    for i, f in enumerate(files):
        tree = ET.parse(f)
        root.append(tree.getroot())

    x = []
    y = []

    for r in root:
        for child in r:
            for subchild in child:
                if subchild.tag == "time":
                    tmp = []
                    for subsubchild in subchild:
                        # print(subsubchild.tag, subsubchild.attrib)
                        if subsubchild.tag == "symbol":
                            a = subsubchild.get("name")
                            y.append(a)
                        if subsubchild.tag == ("windSpeed"):
                            windspeed = subsubchild.get("mps")
                            tmp.append(windspeed)
                            # print(windspeed)
                        if subsubchild.tag == ("temperature"):
                            tem = subsubchild.get("value")
                            tmp.append(tem)
                        if subsubchild.tag == ("pressure"):
                            p = subsubchild.get("value")
                            tmp.append(p)
                        if subsubchild.tag == ("humidity"):
                            h = subsubchild.get("value")
                            tmp.append(h)
                        if subsubchild.tag == ("clouds"):
                            c = subsubchild.get("all")
                            tmp.append(c)
                    x.append(tmp)
                    # print("--------")

    x = np.array(x, dtype=np.float)
    # print(len(y))

    gnb = GaussianNB()
    y_pred = gnb.fit(x, y).predict(data)

    return y_pred



@app.route('/weather')
def index():
    return render_template("index.html")

@app.route('/weather', methods=['POST'])
def prediction():
    temp = float(request.form['Temp'])
    clouds = float(request.form['Clouds'])
    speed = float(request.form['speed'])
    humidity= float(request.form['Humidity'])
    pressure= float(request.form['Pressure'])

    data = [temp,clouds,speed,humidity,pressure]
    arr=[]
    for i in range (2):
        arr.append(data)
    res = pass_data(arr)
    print(data)
    print (res)
    # session['result'] = res[0]
    # return  redirect(url_for('result'))#render_template('result.html', prediction_result = res[0])
    if res[0] == 'broken clouds':
        return redirect(url_for('result_brokenclouds'))
    elif res[0] == 'scattered clouds':
        return redirect(url_for('result_scatteredclouds'))
    elif res[0] == 'overcast clouds':
        return redirect(url_for('result_overcastclouds'))
    elif res[0] == 'moderate rain':
        return redirect(url_for('result_moderate_rain'))
    elif res[0] == 'clear sky':
        return redirect(url_for('result_clearsky'))
    elif res[0] == 'few clouds':
        return redirect(url_for('result_fewclouds'))
    elif res[0] == 'light rain':
        return redirect(url_for('result_light_rain'))


def toPDF(html_page):
    render = render_template(html_page)
    pdf = pdfkit.from_string(render, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response

@app.route('/weather/result/brokenclouds', methods = ['GET', 'POST'])
def result_brokenclouds():
    if request.method == 'POST':
        return toPDF('Result.html')
    return render_template('Result.html')
    #     return toPDF('Result-BROKENCLOUDS.html')
    # return render_template('Result-BROKENCLOUDS.html')

@app.route('/weather/result/scatteredclouds', methods = ['GET', 'POST'])
def result_scatteredclouds():
    if request.method == 'POST':
        return toPDF('Result-SCATTEREDCLOUDS.html')
    return render_template('Result-SCATTEREDCLOUDS.html')

@app.route('/weather/result/overcastclouds', methods = ['GET', 'POST'])
def result_overcastclouds():
    if request.method == 'POST':
        return toPDF('Result-OVERCASTCLOUDS.html')
    return render_template('Result-OVERCASTCLOUDS.html')


@app.route('/weather/result/moderaterain', methods = ['GET', 'POST'])
def result_moderate_rain():
    if request.method == 'POST':
        return toPDF('Result-MODERATERAIN.html')
    return render_template('Result-MODERATERAIN.html')

@app.route('/weather/result/clearsky', methods = ['GET', 'POST'])
def result_clearsky():
    if request.method == 'POST':
        return toPDF('Result-CLEARSKY.html')
    return render_template('Result-CLEARSKY.html')


@app.route('/weather/result/fewclouds', methods = ['GET', 'POST'])
def result_fewclouds():
    if request.method == 'POST':
        return toPDF('Result-FEWCLOUDS.html')
    return render_template('Result-FEWCLOUDS.html')

@app.route('/weather/result/lightrain', methods = ['GET', 'POST'])
def result_light_rain():
    if request.method == 'POST':
        return toPDF('Result-LIGHTRAIN.html')
    return render_template('Result-LIGHTRAIN.html')

if __name__== "__main__":
    app.run(debug=True)
