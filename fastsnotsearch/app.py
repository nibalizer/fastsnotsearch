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



@app.route("/v3/search/snot")
def searchv3():
    term = request.args.get('term', '')
    t1 = datetime.datetime.now()
    query = db.create_query(term)
    msgs = []
    for i in list(query.search_messages()):
        msg = {}
        msg['id'] = i.get_message_id()
        msg['subject'] = i.get_header('subject').encode('utf-8')
        try:
          msg['summary'] = str(i).encode('utf-8')
        except UnicodeDecodeError:
          print i
          msg['summary'] = 'unable to get summary'
        msg['xtts'] = i.get_header('X-xtts').encode('utf-8')
        msgs.append(msg)


    t2 = datetime.datetime.now()
    delta_t = (t2 - t1).microseconds / 1000.


    return render_template('search.html', msgs=msgs, num_msgs=len(msgs), term=term, delta_t=delta_t)
