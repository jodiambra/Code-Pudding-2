from fastapi import FastAPI
import pickle

app = FastAPI()

# Loading up the trained model
model = pickle.load(open('ML Models/full_model.pkl', 'rb'))

# Defining the model input types
class Candidate(BaseModel):
    usage: float
    university: float
    answer: float
    matches: float
    percentage: float


# Setting up the home route
@app.get("/")
def read_root():
    return {"data": "Welcome to the Tinder relationship prediction model"}


# Setting up the prediction route
@app.post("/prediction/")
async def get_predict(data: Candidate):
    sample = [[
        data.usage,
        data.university,
        data.answer,
        data.matches,
        data.percentage
    ]]
    relationship = model.predict(sample).tolist()[0]
    probability = model.predict_proba(sample).tolist()[0]
    prob = probability[1]*100 
    return {
        "data": {
            'prediction': relationship,
            'probability': prob,
            'interpretation': 'You will find a relationship.' if relationship == 1 else 'You will not find a relationship.',
            'probability interpretation': 'probability of relationship'
        }
    }