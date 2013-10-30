# -*- coding: utf-8 -*-
import datetime

import simplejson as json

from flask import Flask

from flask import render_template, abort, request

from flask import redirect, url_for

app = Flask(__name__)

import notmuch

db = notmuch.Database()

@app.route("/")
def hello():
    return redirect(url_for('searchroot'))


@app.route("/v2/search")
def searchroot():
    return render_template('searchroot.html')



@app.route("/v2/message/<msgid>")
def messagev2(msgid):
    msg = db.find_message(msgid).format_message_as_text()
    ppmsg = msg.split('\n')
    return render_template('msg.html', msg=ppmsg)


@app.route("/search/<term>")
def search(term):
    t1 = datetime.datetime.now()
    query = db.create_query(term)
    output = [ str(i) for i in list(query.search_messages()) ]
    t2 = datetime.datetime.now()
    delta_t = (t2 - t1).microseconds / 1000.
    output.insert(0, "Found <b>{0}</b> messages matching <b>{1}</b> in <b>{2}</b> milliseconds".format(
      len(output), term, delta_t))
    return "\n<p>".join(output)



@app.route("/v2/search/<term>")
def searchv2(term):
    t1 = datetime.datetime.now()
    query = db.create_query(term)
    msgs = []
    for i in list(query.search_messages()):
        msg = {}
        msg['id'] = i.get_message_id()
        msg['subject'] = i.get_header('subject')
        msg['summary'] = str(i)
        msgs.append(msg)


    t2 = datetime.datetime.now()
    delta_t = (t2 - t1).microseconds / 1000.


    return render_template('search.html', msgs=msgs, num_msgs=len(msgs), term=term, delta_t=delta_t)



@app.route("/v3/search/snot")
def searchv3():
    term = request.args.get('term', '')
    t1 = datetime.datetime.now()
    query = db.create_query(term)
    msgs = []
    for i in list(query.search_messages()):
        msg = {}
        msg['id'] = i.get_message_id()
        msg['subject'] = i.get_header('subject')
        try:
          msg['summary'] = str(i).encode('ascii')
        except UnicodeDecodeError:
          print i
          msg['summary'] = 'unable to get summary'
        msgs.append(msg)


    t2 = datetime.datetime.now()
    delta_t = (t2 - t1).microseconds / 1000.


    return render_template('search.html', msgs=msgs, num_msgs=len(msgs), term=term, delta_t=delta_t)
