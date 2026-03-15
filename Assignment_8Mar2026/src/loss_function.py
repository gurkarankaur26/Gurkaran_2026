import numpy as np
pred = [10.4, 7.4, 3.6]
act= [8, 3, 10]
def loss_function(predicted=pred,actual=act):    
    a = np.array(predicted)
    b = np.array(actual)
    mae = sum(abs(a-b))/len(predicted)
    mse = sum((a-b)**2)/len(predicted)
    rmse = ((sum((a-b)**2)/len(predicted))**0.5)
    print(f"Error=> MAE:{mae} MSE: {mse} RMSE: {rmse}")
    return mae,mse,rmse


loss_function()