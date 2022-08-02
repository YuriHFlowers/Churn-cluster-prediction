import pandas as pd
import numpy as np


def preprocess(df):

    df.gender = df.gender.replace({"Male": 0, "Female": 1})
    df.education = df.education.replace(
        {
            "Unknown": 0,
            "Uneducated": 1,
            "High School": 2,
            "College": 3,
            "Graduate": 4,
            "Post-Graduate": 5,
            "Doctorate": 6,
        }
    )
    df.income = df.income.replace(
        {
            "Unknown": 0,
            "Less than $40K": 30,
            "$40K - $60K": 50,
            "$60K - $80K": 70,
            "$80K - $120K": 90,
            "$120K or more": 120,
        }
    )
    df.card = df.card.apply(lambda x: 1 if x == "Blue" else 0)

    df.products = df.products.replace(
        {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six or more": 6,}
    )

    df.inactive = df.inactive.replace(
        {
            "Always active": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six or more": 6,
        }
    )

    df.contacts = df.contacts.replace(
        {
            "No contact": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six or more": 6,
        }
    )

    X = df.iloc[:, :].values

    return X
