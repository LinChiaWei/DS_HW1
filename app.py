
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    args = parser.parse_args()
    
    import numpy as np
    import pandas as pd
    import pandas_datareader as pdr
    import matplotlib.pyplot as plt
    import datetime as datetime
    from fbprophet import Prophet
    from sklearn import metrics
    from pandas import to_datetime
    from math import sqrt
    from sklearn.metrics import mean_squared_error


    dataset_total = pd.read_csv(args.training)
    train = dataset_total[:]


    model = Prophet()
    model.fit(train)

    future = model.make_future_dataframe(periods=14)
    forecast = model.predict(future)


    predict = pd.DataFrame()
    df = pd.DataFrame()
    list = [i for i in range(20220401,20220413)]
    predict.insert(0,column='date',value=['20220330','20220331'])
    df.insert(0,column='date',value=list)
    predict = predict.append(df, ignore_index=True)
    list2 = forecast['yhat'][431:]
    list2.reset_index(inplace=True, drop=True)
    predict.insert(1,column='operating_reserve(MW)',value=list2)
    predict.to_csv(args.output,index=False)