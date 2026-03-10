import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# -----------------------
# PARAMETERS
# -----------------------

N_MINES = 3
N_EMPLOYEES = 300
N_BLOCKS = 2000
N_DRILLHOLES = 120
N_EQUIPMENT = 80
N_DAYS = 365

minerals = ["Copper", "Gold", "Iron", "Lithium"]
roles = ["Operator","Engineer","Supervisor","Geologist","Technician","Metallurgist"]

# -----------------------
# MINES
# -----------------------

mine_names = ["Andes Norte","Condor Ridge","Santa Rosa"]

mines = pd.DataFrame({
    "MineID": range(1,N_MINES+1),
    "MineName": mine_names,
    "Mineral": np.random.choice(minerals,N_MINES),
    "Capacity_tpd": np.random.randint(10000,80000,N_MINES)
})

# -----------------------
# EMPLOYEES
# -----------------------

employees = pd.DataFrame({
    "EmployeeID": range(1,N_EMPLOYEES+1),
    "Name":[fake.name() for _ in range(N_EMPLOYEES)],
    "Role":np.random.choice(roles,N_EMPLOYEES),
    "Salary":np.random.randint(1500,9000,N_EMPLOYEES),
    "MineID":np.random.choice(mines.MineID,N_EMPLOYEES)
})

# -----------------------
# EQUIPMENT
# -----------------------

equipment_types = ["Truck","Excavator","Drill","Crusher","Mill"]

equipment = pd.DataFrame({
    "EquipmentID":range(1,N_EQUIPMENT+1),
    "Type":np.random.choice(equipment_types,N_EQUIPMENT),
    "MineID":np.random.choice(mines.MineID,N_EQUIPMENT),
    "PurchaseCost":np.random.randint(200000,5000000,N_EQUIPMENT),
    "Year":np.random.randint(2010,2024,N_EQUIPMENT)
})

# -----------------------
# BLOCK MODEL
# -----------------------

blocks = pd.DataFrame({
    "BlockID":range(1,N_BLOCKS+1),
    "MineID":np.random.choice(mines.MineID,N_BLOCKS),
    "X":np.random.randint(0,1000,N_BLOCKS),
    "Y":np.random.randint(0,1000,N_BLOCKS),
    "Z":np.random.randint(-500,0,N_BLOCKS),
    "Tonnes":np.random.normal(5000,1000,N_BLOCKS).astype(int),
    "Grade":np.round(np.random.uniform(0.3,2.5,N_BLOCKS),2)
})

# -----------------------
# DRILLHOLES
# -----------------------

drillholes = pd.DataFrame({
    "DrillholeID":range(1,N_DRILLHOLES+1),
    "MineID":np.random.choice(mines.MineID,N_DRILLHOLES),
    "Depth_m":np.random.randint(50,600,N_DRILLHOLES),
    "AvgGrade":np.round(np.random.uniform(0.4,2.2,N_DRILLHOLES),2),
    "Year":np.random.randint(2015,2025,N_DRILLHOLES)
})

# -----------------------
# PRODUCTION
# -----------------------

dates = [datetime(2024,1,1) + timedelta(days=i) for i in range(N_DAYS)]

production_rows = []

for d in dates:
    for mine in mines.MineID:

        ore = int(np.random.normal(35000,5000))
        grade = round(np.random.uniform(0.5,1.5),2)
        recovery = round(np.random.uniform(75,92),1)

        metal = ore * grade/100 * recovery/100

        production_rows.append([
            d,mine,ore,grade,recovery,metal
        ])

production = pd.DataFrame(
    production_rows,
    columns=[
        "Date","MineID","OreProcessed_t",
        "Grade_%","Recovery_%","MetalProduced_t"
    ]
)

# -----------------------
# METAL PRICES
# -----------------------

price_rows = []

for d in dates:

    price_rows.append([
        d,
        round(np.random.normal(8500,500),2),   # copper
        round(np.random.normal(65000,2000),2), # gold
        round(np.random.normal(120,10),2),     # iron
        round(np.random.normal(30000,2000),2)  # lithium
    ])

prices = pd.DataFrame(
    price_rows,
    columns=["Date","Copper","Gold","Iron","Lithium"]
)

# -----------------------
# OPEX
# -----------------------

opex = pd.DataFrame({
    "Date":np.random.choice(dates,500),
    "MineID":np.random.choice(mines.MineID,500),
    "Category":np.random.choice(
        ["Energy","Maintenance","Labor","Fuel","Consumables"],
        500
    ),
    "Cost":np.random.randint(5000,120000,500)
})

# -----------------------
# CAPEX
# -----------------------

capex = pd.DataFrame({
    "Year":np.random.randint(2018,2025,60),
    "MineID":np.random.choice(mines.MineID,60),
    "Project":np.random.choice(
        ["Plant Expansion","New Fleet","Tailings","Exploration"],
        60
    ),
    "Cost":np.random.randint(500000,25000000,60)
})

# -----------------------
# STOCKPILES
# -----------------------

stockpiles = pd.DataFrame({
    "StockpileID":range(1,40),
    "MineID":np.random.choice(mines.MineID,39),
    "Tonnes":np.random.randint(20000,400000,39),
    "Grade":np.round(np.random.uniform(0.4,1.8,39),2)
})

# -----------------------
# SALES
# -----------------------

sales_rows=[]

for d in dates:
    for mine in mines.MineID:

        tonnes = abs(np.random.normal(800,200))
        price = abs(np.random.normal(8500,600))

        revenue = tonnes*price

        sales_rows.append([d,mine,tonnes,price,revenue])

sales = pd.DataFrame(
    sales_rows,
    columns=["Date","MineID","MetalSold_t","Price","Revenue"]
)

# -----------------------
# EXPORT
# -----------------------

with pd.ExcelWriter("mining_dataset_powerbi.xlsx") as writer:

    mines.to_excel(writer, sheet_name="Mines", index=False)
    employees.to_excel(writer, sheet_name="Employees", index=False)
    equipment.to_excel(writer, sheet_name="Equipment", index=False)
    blocks.to_excel(writer, sheet_name="Blocks", index=False)
    drillholes.to_excel(writer, sheet_name="Drillholes", index=False)
    production.to_excel(writer, sheet_name="Production", index=False)
    prices.to_excel(writer, sheet_name="MetalPrices", index=False)
    opex.to_excel(writer, sheet_name="OPEX", index=False)
    capex.to_excel(writer, sheet_name="CAPEX", index=False)
    stockpiles.to_excel(writer, sheet_name="Stockpiles", index=False)
    sales.to_excel(writer, sheet_name="Sales", index=False)

print("Dataset generated: mining_dataset_powerbi.xlsx")