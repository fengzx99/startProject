# -*- coding: utf-8 -*-
# __author__="ZJL"
from threading import Timer
from wsgiref.simple_server import make_server, WSGIServer
import timer
from flask import Flask, render_template
from flask import request
from flask import Response
import numpy as np
import webbrowser
from Visualization import*
app = Flask(__name__)


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
def running():
    return render_template("index.html")


@app.route('/trainSet')
def trainData():
    return render_template("TrainAnalyze.html")


@app.route('/shows')
def get_show():
    return render_template('DataView.html')


@app.route('/test')
def get_te():
    return  render_template("TestResult.html")




@app.route('/testData')
def get_test():
    file = request.args.get('datas')
    if str(file) in [ '0','3','5','14','18','2','4','11','17','19']:
        datas = {
            'Ztopo': TZtopo(file),
            'SankyD': SankitData(file, 'test')
        }
    else:
        datas = {
            'Ztopo': TZtopo(file),
            'Jtopo': TJtopo(file),
            'SankyD': SankitData(file,'test')
        }

    # print(datas)
    content = json.dumps(datas, cls=NpEncoder)
    resp = Response_headers(content)
    return resp


@app.route('/trainData')
def get_train():
    file = request.args.get('datas')
    timeB, timeN = get_node_count(file)
    Sdata = getSundata(file)
    TriggerPieDf = get_trigger_data(file)
    line_df = move_Line(file)

    datas = {
        'TimeBar': timeB,
        'Sdata': Sdata,
        'NodePieDf': timeN,
        'TriggerPieDf': TriggerPieDf,
        'Line_df': line_df,
        'triggerCloud': TriggerPieDf,
        'nodeCloud': timeN,
        'Ztopo': Ztopo(file),
        'Jtopo': Jtopo(file),
        'SankyD': SankitData(file)
    }

    #print(SankitData(file))
    content = json.dumps(datas, cls=NpEncoder)
    resp = Response_headers(content)
    return resp


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


def start_browser(url):
    #server_ready_event.wait()
    print(url)
    webbrowser.open_new(url)


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/"
    Timer(2, start_browser(url))
    
    app.run(port=5000)


