from prediction import predict, predict_proba

result = predict([[2, 46, 1, 400, 25]])
proba = predict_proba([[2, 46, 1, 400, 25]]) * 100

print(result, proba)


