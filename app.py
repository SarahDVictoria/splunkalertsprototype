from flask import Flask, request, make_response
import pymongo


app = Flask('splunk alerts')


def makejsonresponse(data):
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/splunkalerts', methods = ['GET', 'POST'])
def splunkalerts()
    mongoclient = pymongo.MongoClient('localhost', 27017)

    if request.method == 'GET':
        alertlist = []
        for alert in mongoclient.splunk.alerts.find():
            alertlist.append(alert)
        mongoclient.close()
        return makejsonresponse(alertlist)

    elif request.method == 'POST':
        # verify the ip at the least because this assumes you trust request.json
        mongoclient.splunk.alerts.insert_one(request.json())
        mongoclient.close()
        return makejsonresponse('Thankies')


@app.route('/', methods = ['GET'])
def root():
    return render_template('alerts.html')
