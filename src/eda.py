import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def correlation_analysis(df, target):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if target not in numeric_cols:
        raise ValueError(f"Target column '{target}' must be numeric")

    corr = df[numeric_cols].corr()[target].sort_values(ascending=False)
    print(corr)
    return corr


def random_forest_feature_importance(df, target):
    feature_cols = [col for col in df.select_dtypes(include=np.number).columns if col != target]
    X = df[feature_cols]
    y = df[target]
    model = RandomForestRegressor(n_estimators=100, max_depth=10,random_state=42, n_jobs=-1)
    model.fit(X, y)

    importance = pd.DataFrame({'feature': feature_cols, 'importance': model.feature_importances_}).sort_values(
        'importance', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(importance['feature'], importance['importance'])
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('feature_importance.png')

    return importance
