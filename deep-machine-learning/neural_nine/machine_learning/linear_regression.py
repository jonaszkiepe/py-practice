import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

time_studied = np.array([14, 20, 35, 44, 80]).reshape(-1, 1)
scores = np.array([18, 29, 34, 35, 50]).reshape(-1, 1)

time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.8)

model = LinearRegression()
model.fit(time_studied, scores)

print(model.score(time_test, score_test))
