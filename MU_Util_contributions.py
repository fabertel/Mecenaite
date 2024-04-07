import pandas as pd

# Assumed Data
time_commitment_hours = {"Fabio": 160, "Riccardo": 160, "Andrea": 160}  # Monthly
capital_investment = {"Fabio": 20000, "Riccardo": 15000, "Andrea": 10000}
# Assuming equal results points for simplification, in practice, this should be based on agreed targets.
results_points = {"Fabio": 100, "Riccardo": 100, "Andrea": 100}

# Calculations
time_points = {name: hours for name, hours in time_commitment_hours.items()}  # 1 point/hour
capital_points = {name: capital // 1000 for name, capital in capital_investment.items()}  # 1 point/€1000
total_points = {name: time_points[name] + capital_points[name] + results_points[name] for name in time_points}

total_points_sum = sum(total_points.values())
equity_percentage = {name: (points / total_points_sum) * 100 for name, points in total_points.items()}

# Creating DataFrame for display
founders_data = pd.DataFrame({
    "Founder": total_points.keys(),
    "Time Points": time_points.values(),
    "Capital Points": capital_points.values(),
    "Results Points": results_points.values(),
    "Total Points": total_points.values(),
    "Equity & Decision Power (%)": equity_percentage.values()
})

print(founders_data)
