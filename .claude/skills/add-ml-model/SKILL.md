---
name: add-ml-model
description: Add a new prediction model (ARIMA, LSTM, ensemble, etc.) to apps/prediction/predictor.py following the project's inference pattern.
---

# Skill: Add ML Model

Extend `apps/prediction/predictor.py` with a new model while keeping `predict_next_price` as the single public entry point.

## Steps

1. **Install the dependency** (if new) and add it to `requirements.txt`:
   ```
   statsmodels==0.14.2   # already present — for ARIMA
   tensorflow==2.16.1    # add if using LSTM
   ```

2. **Implement a private predictor function** in `apps/prediction/predictor.py`:
   ```python
   def _predict_arima(prices: list[float], steps: int) -> float:
       from statsmodels.tsa.arima.model import ARIMA
       model = ARIMA(prices, order=(5, 1, 0))
       fit = model.fit()
       forecast = fit.forecast(steps=steps)
       return float(forecast.iloc[-1])
   ```
   - Keep training + inference together for stateless, request-time prediction
   - For heavy models, accept a pre-trained artifact path and load with `joblib.load()`

3. **Update `predict_next_price` to route by model name**:
   ```python
   def predict_next_price(prices: list[float], horizon: str = '1h', model: str = 'linear') -> float:
       steps = {'1h': 1, '24h': 24, '7d': 168}.get(horizon, 1)
       if model == 'arima':
           return _predict_arima(prices, steps)
       # default: linear regression
       return _predict_linear(prices, steps)
   ```

4. **Pass `model` from the view** in `apps/prediction/views.py`:
   ```python
   model_name = request.query_params.get('model', 'linear')
   predicted = predict_next_price(prices, horizon=horizon, model=model_name)
   ```

5. **Store the model name** in `PricePrediction.model_name` (already a field on the model).

6. **Update the API docs** comment in `apps/prediction/urls.py` or README if the `model=` param is new.

7. **Write a test** in `apps/prediction/tests/test_predictor.py`:
   ```python
   def test_arima_returns_float():
       prices = [float(i) for i in range(50, 100)]
       result = predict_next_price(prices, horizon='1h', model='arima')
       assert isinstance(result, float)
       assert result > 0
   ```

## Checklist
- [ ] New predictor is a private `_predict_<name>` function
- [ ] `predict_next_price` routes to it via `model` parameter
- [ ] Model artifacts (`.pkl`, `.joblib`) are NOT committed
- [ ] `PricePrediction.model_name` records which model was used
- [ ] At least one pytest test added
- [ ] Heavy models use Celery for async training, not synchronous view calls
