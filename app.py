import os

from flask import Flask, render_template

app = Flask("BasicApp")


@app.route("/")
def index():
    """Example showing how to return an HTML template with a form, which
    sends data back to this Flask app using a POST request."""

    return render_template("index.html")

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at (https://www.heroku.com/ before the deployment session!)
This is done so that your app is in good shape for deployment ahead of the
next session, where we'll be covering more about what Heroku is.
"""
if 'PORT' in os.environ:
    # app running on Heroku
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    # app running locally (i.e. you can see it by typing "localhost:5000" in browser)
    app.run(debug=True)
