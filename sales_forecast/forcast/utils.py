# forecast/utils.py
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def forcast_sales(historical_data,steps=7):
    """
    Predicts next 3 periods of sales using ARIMA(1,1,1)

    Alright haqq: ARIMA is a time series forecasting model that uses past data to predict future values.
    In this case,
    - historical_data: A list of past sales values
    - forecast_sales: A list of forecasted sales values (3 periods ahead)

    it's simple configuration(AutoRegressive, Integrated, Moving Average) is (1,1,1)
    1. AR(1): Autoregressive term of order 1
    2. I(1): Integrated term of order 1
    3. MA(1): Moving Average term of order 1

    Args:
        historical_data (list): List of past sales values
    Returns:
        list: Forecasted values (3 periods ahead)
    """
    if len(historical_data) < 5:
        return [0] * steps  # Return array matching forecast period
    
    try:
        model = ARIMA(historical_data, order=(1,1,1))
        model_fit = model.fit()
        return [round(val, 2) for val in model_fit.forecast(steps=steps)]
    except:
        return [0] * steps  