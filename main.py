from src.data_loader import load_and_preprocess_data
from src.eda import correlation_analysis, random_forest_feature_importance
from src.model import train_random_forest
from src.visualization import plot_predictions, plot_hourly_consumption
from src.recommendations import generate_energy_recommendations
from src.future_prediction import predict_future_consumption

df = load_and_preprocess_data('data/raw/household_power_consumption.txt')

corr = correlation_analysis(df, 'Global_active_power')
importance = random_forest_feature_importance(df, 'Global_active_power')
selected_features = importance[importance['importance'] > 0.02]['feature'].tolist()

model, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test = train_random_forest(df, 'Global_active_power', selected_features)

plot_predictions(y_test, y_pred_test)
hourly = plot_hourly_consumption(df)

recommendations = generate_energy_recommendations(df, hourly)
print(recommendations)

predict_future_consumption(model, X_test.iloc[[-1]], hours_ahead=24)
