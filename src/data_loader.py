import pandas as pd
import numpy as np

def load_and_preprocess_data(path):
    df = pd.read_csv(
        path,
        sep=';',
        parse_dates={'datetime': ['Date', 'Time']},
        dayfirst=True,
        na_values='?',
        low_memory=False
    )

    df = df.ffill()

    z_scores = np.abs((df['Global_active_power'] - df['Global_active_power'].mean()) / df['Global_active_power'].std())
    df = df[z_scores < 3]

    df['hour'] = df['datetime'].dt.hour
    df['day_of_week'] = df['datetime'].dt.dayofweek
    df['month'] = df['datetime'].dt.month
    df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
    df['season'] = df['month'] % 12 // 3 + 1

    df['time_of_day'] = df['hour'].apply(
        lambda h: 1 if 6 <= h < 12 else 2 if 12 <= h < 18 else 3 if 18 <= h < 22 else 4
    )


    df['power_lag_1'] = df['Global_active_power'].shift(1)
    df['power_lag_24'] = df['Global_active_power'].shift(24)
    df['power_lag_168'] = df['Global_active_power'].shift(168)
    df['power_rolling_mean_24'] = df['Global_active_power'].rolling(24).mean()
    df['power_rolling_std_24'] = df['Global_active_power'].rolling(24).std()

    df = df.dropna()
    return df
