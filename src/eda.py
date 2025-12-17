import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


def correlation_analysis(df, target):
    feature_cols = [c for c in df.columns if c != target and c != 'datetime']
    corr = df[feature_cols + [target]].corr()[target].sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    corr[1:].plot(kind='barh')
    plt.title('Feature Correlation with Target')
    plt.tight_layout()
    plt.savefig('feature_correlation.png')
    return corr


def random_forest_feature_importance(df, target):
    feature_cols = [c for c in df.columns if c != target and c != 'datetime']
    X = df[feature_cols]
    y = df[target]
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X, y)

    importance = pd.DataFrame({'feature': feature_cols, 'importance': model.feature_importances_}).sort_values(
        'importance', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(importance['feature'], importance['importance'])
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('feature_importance.png')

    return importance
