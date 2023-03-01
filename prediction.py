import joblib


def predict(data):
    clf = joblib.load('ML Models/full_model.joblib')
    return clf.predict(data)

def predict_proba(data):
    clf = joblib.load('ML Models/full_model.joblib')
    return clf.predict_proba(data)