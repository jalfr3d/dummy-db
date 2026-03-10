import pandas as pd
import numpy as np
from faker import Faker
import sqlite3
import random

fake = Faker()

# -----------------------
# Parameters
# -----------------------
n_employees = 200
n_mines = 5
n_production = 1000

minerals = ["Copper", "Gold", "Iron", "Lithium"]
roles = ["Operator", "Engineer", "Supervisor", "Geologist", "Technician"]
mine_names = ["Andes Norte", "El Condor", "Santa Rosa", "Altiplano", "Los Pumas"]

# -----------------------
# Mines table
# -----------------------
mines = pd.DataFrame({
    "MineID": range(1, n_mines+1),
    "MineName": mine_names,
    "Mineral": np.random.choice(minerals, n_mines),
    "Capacity_tpd": np.random.randint(5000, 50000, n_mines)
})

# -----------------------
# Employees table
# -----------------------
employees = pd.DataFrame({
    "EmployeeID": range(1, n_employees+1),
    "Name": [fake.name() for _ in range(n_employees)],
    "Role": np.random.choice(roles, n_employees),
    "Salary": np.random.randint(1200, 7000, n_employees),
    "MineID": np.random.choice(mines["MineID"], n_employees)
})

# -----------------------
# Production table
# -----------------------
production = pd.DataFrame({
    "ProductionID": range(1, n_production+1),
    "MineID": np.random.choice(mines["MineID"], n_production),
    "Date": pd.date_range("2024-01-01", periods=n_production, freq="D"),
    "OreProcessed_t": np.random.normal(20000, 4000, n_production).astype(int),
    "Grade_%": np.round(np.random.uniform(0.4, 2.0, n_production), 2),
    "Recovery_%": np.round(np.random.uniform(70, 95, n_production), 1)
})

# -----------------------
# Revenue table
# -----------------------
price = {
    "Copper": 8500,
    "Gold": 65000,
    "Iron": 120,
    "Lithium": 30000
}

production["MetalProduced_t"] = production["OreProcessed_t"] * production["Grade_%"]/100 * production["Recovery_%"]/100

production["Revenue"] = production["MetalProduced_t"] * np.random.choice(list(price.values()), n_production)

# -----------------------
# Save SQLite database
# -----------------------
conn = sqlite3.connect("mining_company.db")

mines.to_sql("Mines", conn, if_exists="replace", index=False)
employees.to_sql("Employees", conn, if_exists="replace", index=False)
production.to_sql("Production", conn, if_exists="replace", index=False)

conn.close()

print("Database created: mining_company.db")