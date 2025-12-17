def generate_energy_recommendations(df, hourly_consumption=None):
    recommendations = []
    if hourly_consumption is None:
        hourly_consumption = df.groupby('hour')['Global_active_power'].mean()

    top_hours = hourly_consumption.nlargest(3)
    recommendations.append("🔴 YÜKSEK TÜKETİM SAATLERİ:")
    for hour, val in top_hours.items():
        recommendations.append(f"• Saat {hour}:00: {val:.2f} kW")
    recommendations.append("➜ Bu saatlerde büyük cihazları kullanmayın!")

    bottom_hours = hourly_consumption.nsmallest(3)
    recommendations.append("\n🟢 DÜŞÜK TÜKETİM SAATLERİ:")
    for hour, val in bottom_hours.items():
        recommendations.append(f"• Saat {hour}:00: {val:.2f} kW")
    recommendations.append("➜ Büyük cihazları bu saatlerde çalıştırabilirsiniz.")

    weekday_avg = df[df['is_weekend'] == 0]['Global_active_power'].mean()
    weekend_avg = df[df['is_weekend'] == 1]['Global_active_power'].mean()
    recommendations.append(f"\nHafta içi ortalama: {weekday_avg:.2f} kW")
    recommendations.append(f"Hafta sonu ortalama: {weekend_avg:.2f} kW")

    season_avg = df.groupby('season')['Global_active_power'].mean()
    season_names = {1: 'Kış', 2: 'İlkbahar', 3: 'Yaz', 4: 'Sonbahar'}
    for season, val in season_avg.items():
        recommendations.append(f"{season_names[season]}: {val:.2f} kW")

    total = df['Global_active_power'].sum()
    savings = total * 0.15
    recommendations.append(f"\nPotansiyel tasarruf: {savings:.2f} kWh (%15)")

    with open('energy_recommendations.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(recommendations))

    return "\n".join(recommendations)
