# forecast/utils.py
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def forecast_sales(historical_data):
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
    try:
        if len(historical_data) < 5:  # Minimum data check
            return [sum(historical_data)/len(historical_data)]*3 if historical_data else [0]*3
        
        model = ARIMA(historical_data, order=(1,1,1))
        model_fit = model.fit()
        forcast = model_fit.forcast(steps=3)
        return [round(val, 2) for val in forcast]
    
    except Exception as e:
        print(f"Forecast error: {e}")
        return [0]*3  # Fallback