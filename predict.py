import xml.etree.ElementTree as ET
import numpy as np
import os, glob, random
from sklearn.naive_bayes import GaussianNB
import datetime
# from fpdf import FPDF
# import pdfkit


def split_test(x,y):
    test = []
    ans = []
    for i in range(int(len(x)/20)):
        r = random.randint(0, len(x)-1)
        test.append(x[r])
        ans.append(y[r])
    return test, ans

def check(pred , ans):
    c = 0
    for i in range(len(pred)):
        if pred[i] != ans[i]:
            c+=1
    accuracy = (len(pred)-c)/len(pred)
    return accuracy


def predict():
    files = glob.glob(os.path.join("data/", "*.xml"))
    print(files)
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
    print(len(y))

    test, answer = split_test(x, y)

    gnb = GaussianNB()
    y_pred = gnb.fit(x, y).predict(test)
    print("Accuracy: "+ str(check(y_pred, answer)))

    return test, y_pred

# data, prediction = predict()
# print(prediction)

# def to_pdf(result, data):
#     output = pyPdf.PdfFileWriter()
#
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


def pdf_print(html_url):
    t = str(datetime.date)
    pdfkit.from_string('jdakjdkla', 'out.pdf')


pdf_print("dsada")