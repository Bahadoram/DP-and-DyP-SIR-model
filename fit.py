from sklearn.linear_model import LinearRegression
import numpy as np

def fit(X, Y):
    if 0 in X:
        X = np.log(X[1:])
        X = X.reshape(-1,1)
        Y = np.log(Y[1:])
    else:
        X = np.log(X[:])
        X = X.reshape(-1,1)
        Y = np.log(Y[:])
    model = LinearRegression()
    model.fit(X, Y)
    R_squared     = model.score(X, Y)
    est_param = model.coef_
    return(est_param, R_squared, model)











