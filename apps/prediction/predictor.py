"""ML 예측 로직. LinearRegression 기반 베이스라인."""

import numpy as np
from sklearn.linear_model import LinearRegression


def predict_next_price(prices: list[float], steps_ahead: int = 1) -> float:
    """과거 가격 리스트로 steps_ahead 뒤 가격 예측 (선형회귀 베이스라인)."""
    if len(prices) < 5:
        raise ValueError("최소 5개 이상의 가격 데이터가 필요합니다.")

    x = np.arange(len(prices)).reshape(-1, 1)
    y = np.array(prices)
    model = LinearRegression().fit(x, y)
    next_x = np.array([[len(prices) - 1 + steps_ahead]])
    return float(model.predict(next_x)[0])
