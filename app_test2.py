from prediction import predict, predict_proba
import numpy as np 

data = np.array([[2, 46, 1, 400, 25]])
np.save('data.npy', data, allow_pickle=True)
data = np.load('data.npy', allow_pickle=True)

result = predict(data)
proba = predict_proba(data) * 100

print(result, proba)
