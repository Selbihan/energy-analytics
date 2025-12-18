import numpy as np
import matplotlib.pyplot as plt

def predict_future_consumption(model, last_features, hours_ahead=24):


    future_preds = []


    current_data = last_features.reshape(1, -1)

    for _ in range(hours_ahead):
        pred = model.predict(current_data)[0]
        future_preds.append(pred)



    future_preds = np.array(future_preds)

    plt.figure(figsize=(14, 6))
    plt.plot(range(1, hours_ahead + 1), future_preds, marker='o')
    plt.title('Gelecek 24 Saat Enerji Tüketim Tahmini')
    plt.xlabel('Saat')
    plt.ylabel('Tahmini Tüketim (kW)')
    plt.grid(True, alpha=0.3)
    plt.axhline(
        future_preds.mean(),
        linestyle='--',
        label=f'Ortalama: {future_preds.mean():.2f} kW'
    )
    plt.legend()
    plt.tight_layout()
    plt.savefig('future_prediction.png')

    return future_preds
