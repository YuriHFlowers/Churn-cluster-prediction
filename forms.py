from unittest import result
from flask import (
    Flask,
    render_template,
    session,
    url_for,
    redirect,
    request,
    flash,
    jsonify,
)
from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, FloatField, DecimalField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired, length
import pandas as pd
import numpy as np
import os

# Create a WTForm Class
class PredictForm(FlaskForm):

    gender = RadioField(
        label="Select Gender:",
        choices=["Male", "Female"],
        validators=[InputRequired(message="The gender is required")],
    )

    education = RadioField(
        label="Select Education Level:",
        choices=[
            "Unknown",
            "Uneducated",
            "High School",
            "College",
            "Graduate",
            "Post-Graduate",
            "Doctorate",
        ],
        validators=[InputRequired(message="This field is required")],
    )
    income = RadioField(
        "Select Income range:",
        choices=[
            "Unknown",
            "Less than $40K",
            "$40K - $60K",
            "$60K - $80K",
            "$80K - $120K",
            "$120K or more",
        ],
        validators=[InputRequired(message="This field is required")],
    )
    card = RadioField(
        label="Select Bank card:",
        choices=["Blue", "Silver", "Gold", "Platinum"],
        validators=[InputRequired(message="This field is required")],
    )
    products = RadioField(
        label="Select Number of products:",
        choices=["One", "Two", "Three", "Four", "Five", "Six or more"],
        validators=[InputRequired(message="This field is required")],
    )
    inactive = RadioField(
        label="Select Number of months inactive in the last year:",
        choices=["Always active", "One", "Two", "Three", "Four", "Five", "Six or more"],
        validators=[InputRequired(message="This field is required")],
    )
    contacts = RadioField(
        label="Select Number of contacts with the customer in the last year:",
        choices=["No contact", "One", "Two", "Three", "Four", "Five", "Six or more"],
        validators=[InputRequired(message="This field is required")],
    )

    credit = FloatField(
        label="Enter Credit limit:",
        validators=[InputRequired(message="This field is numeric")],
    )
    revolving = FloatField(
        label="Enter Total revolving balance:",
        validators=[InputRequired(message="This field is required")],
    )
    transactions = IntegerField(
        label="Enter Total number of transaction count:",
        validators=[InputRequired(message="This field is required")],
    )
    ratio = DecimalField(
        label="Select Average card utilization ratio:",
        validators=[InputRequired(message="This field is required")],
    )

    submit = SubmitField("Predict")

