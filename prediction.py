import pickle
import pandas as pd
import json

def predict_mpg(config):
    ##loading the model from the saved file
    try:
       # pkl_filename = "hello.py"
       # with open(pkl_filename, 'rb') as f_in:
       #      model = pickle.load(f_in)
       
        if type(config) == dict:
            df = pd.DataFrame(config)
        else:
            df = config
        
        y_pred = 0 #model.predict(df)
        
        if y_pred == 0:
            return 'Extremely Weak'
        elif y_pred == 1:
            return 'Weak'
        elif y_pred == 2:
            return 'Normal'
        elif y_pred == 3:
            return 'Overweight'
        elif y_pred == 4:
            return 'Obesity'
        elif y_pred == 5:
            return 'Extreme Obesity'
    except Exception as error:
            return {'error': error}        
