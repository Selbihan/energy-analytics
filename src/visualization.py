import matplotlib.pyplot as plt
import pandas as pd

def plot_predictions(y_test, y_pred_test, sample_size=500):
    sample_size = min(sample_size, len(y_test))
    indices = range(sample_size)

    plt.figure(figsize=(15,5))
    plt.plot(indices, y_test.iloc[:sample_size].values, label='Gerçek', alpha=0.7)
    plt.plot(indices, y_pred_test[:sample_size], label='Tahmin', alpha=0.7)
    plt.title('Gerçek ve Tahmin Edilen Enerji Tüketimi (Test Seti)')
    plt.xlabel('Zaman (Saat)')
    plt.ylabel('Enerji Tüketimi (kW)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('predictions_visualization.png')


def plot_hourly_consumption(df):
    hourly = df.groupby('hour')['Global_active_power'].mean()
    plt.figure(figsize=(12,6))
    plt.plot(hourly.index, hourly.values, marker='o')
    plt.title('Saatlik Ortalama Enerji Tüketimi')
    plt.xlabel('Saat')
    plt.ylabel('Ortalama Tüketim (kW)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('hourly_consumption.png')
    return hourly
