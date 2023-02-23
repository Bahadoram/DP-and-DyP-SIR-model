from sklearn.linear_model import LinearRegression
import numpy as np

def ratio_tau_finder(size, prob):
    X = np.log(size[1:])
    X = X.reshape(-1,1)
    Y = np.log(prob[1:])
    model = LinearRegression()
    model.fit(X, Y)
    R_squared     = model.score(X, Y)
    estimated_tau = 2 - model.coef_
    return(estimated_tau, R_squared, model)

def gamma_nu_finder(L, size_list):
    X = np.log(L[:])
    X = X.reshape(-1,1)
    Y = np.log(size_list[:])
    model = LinearRegression()
    model.fit(X, Y)
    R_squared = model.score(X, Y)
    estimated_GammaNu = model.coef_
    return(estimated_GammaNu, R_squared, model)


def beta_finder(L, M):
    X = np.log(L[:])
    X = X.reshape(-1,1)
    Y = np.log(M[:])
    model = LinearRegression()
    model.fit(X, Y)
    R_squared = model.score(X, Y)
    estimated_exp = model.coef_
    return(estimated_exp, R_squared, model)

def theta_finder(t, inf_num):
    X = np.log(t[1:])
    X = X.reshape(-1,1)
    Y = np.log(inf_num[1:])
    model = LinearRegression()
    model.fit(X, Y)
    R_squared = model.score(X, Y)
    estimated_exp = model.coef_
    return(estimated_exp, R_squared, model)









