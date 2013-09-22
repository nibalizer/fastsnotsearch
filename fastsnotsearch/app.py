
from flask import Flask
app = Flask(__name__)

import notmuch

db = notmuch.Database()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/nibz")
def nibz():
    query = db.create_query('nibz')
    #return " ".join(list((query.search_messages()))) # doctest:+ELLIPSIS
    output = [ str(i) for i in list(query.search_messages()) ]
    return "\n<p>".join(output)

@app.route("/search/<term>")
def search(term):
    query = db.create_query(term)
    output = [ str(i) for i in list(query.search_messages()) ]
    output.insert(0, "Found <b>{0}</b> messages matching <b>{1}</b>".format(
      len(output), term))
    return "\n<p>".join(output)

