from unittest import result
from flask import (
    Flask,
    render_template,
    session,
    url_for,
    redirect,
    request,
    flash,
)
from flask_wtf import FlaskForm

# from sklearn import model_selection
from wtforms import RadioField, IntegerField, FloatField, DecimalField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired
import joblib
import pandas as pd
import numpy as np
import os
from forms import PredictForm
from preprocessing.cleaning_data import preprocess
from predict.prediction import predic_pres

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn_extra.cluster import KMedoids


# Create an instance of the Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = "asecretkey"


# Set up the home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Create instance of the form
    form = PredictForm()

    # Validate the form
    if form.validate_on_submit():
        session["gender"] = form.gender.data
        session["education"] = form.education.data
        session["income"] = form.income.data
        session["card"] = form.card.data
        session["products"] = form.products.data
        session["inactive"] = form.inactive.data
        session["contacts"] = form.contacts.data
        session["credit"] = form.credit.data
        session["revolving"] = form.revolving.data
        session["transactions"] = form.transactions.data
        session["ratio"] = form.ratio.data

        return redirect(url_for("prediction"))

    return render_template("home.html", form=form)


# 7. define a new "prediction" route that processes form input and returns a model prediction
@app.route("/prediction")
def prediction():

    """ Selected features """
    content = {}
    content["gender"] = session["gender"]
    content["education"] = session["education"]
    content["income"] = session["income"]
    content["card"] = session["card"]
    content["products"] = session["products"]
    content["inactive"] = session["inactive"]
    content["contacts"] = session["contacts"]
    content["credit"] = session["credit"]
    content["revolving"] = session["revolving"]
    content["transactions"] = session["transactions"]
    content["ratio"] = session["ratio"]

    df = pd.DataFrame([content.values()], columns=content.keys())

    # processing the input
    X = preprocess(df)

    # Load the model
    model = joblib.load("K_Medoids.joblib")

    # Prediction
    results = model.predict(X)

    # Presentation results
    op1, op2, img = predic_pres(results)

    return render_template("prediction.html", op1=op1, op2=op2, url_1=img)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

