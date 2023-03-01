from prediction import predict, predict_proba
import numpy as np


result = predict(np.array([2, 46, 1, 400, 25]))
proba = predict_proba(np.array([2, 46, 1, 400, 25]))
print(result, proba[1])
