# ⛏️ Dummy Database Generator for Mining

A Python-based toolkit for generating **realistic dummy datasets** for mining operations, designed for **data analysis, SQL practice, and Power BI dashboards**.

This repository includes two main scripts:

* `main.py` → lightweight generator (SQLite `.db`)
* `more_tables_db.py` → full-scale dataset (Excel, multi-table)

The data model is inspired by real mining workflows but remains fully synthetic and customizable.

---

# 📦 Features

## 1. `main.py` — Simple Database Generator

Creates a **SQLite database (`.db`)** with core tables:

* `Mines`
* `Employees`
* `Production`

### Use cases

* SQL learning and practice
* Testing queries and joins
* Lightweight BI dashboards

---

## 2. `more_tables_db.py` — Full Mining Dataset

Generates a **multi-table Excel dataset** with a richer structure:

### Tables included

* Mines
* Employees
* Equipment
* Blocks (block model)
* Drillholes
* Production
* MetalPrices
* OPEX
* CAPEX
* Stockpiles
* Sales

### Use cases

* Power BI dashboards
* Data modeling (star schema)
* Mining analytics simulations
* Portfolio projects

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jalfr3d/dummy-db.git
```

Install dependencies:

```bash
pip install pandas numpy faker openpyxl
```

---

# 🚀 Usage

## Run simple database generator

```bash
python main.py
```

Output:

```
mining_company.db
```

---

## Run full dataset generator

```bash
python more_tables_db.py
```

Output:

```
mining_dataset.xlsx
```

---

# 🧠 Data Model Overview

### Core relationships

* `Mines` is the central table
* All operational tables reference `MineID`
* Time-series tables use `Date`

Example:

```
Mines
 ├── Employees
 ├── Equipment
 ├── Production
 ├── OPEX
 ├── CAPEX
 ├── Sales
```

---

# 📊 Power BI Integration

## Recommended workflow

1. Open Power BI
2. Click **Get Data → Excel**
3. Load `mining_dataset.xlsx`
4. Create relationships using `MineID` and `Date`

### Suggested relationships

```
Mines[MineID] → Employees[MineID]
Mines[MineID] → Production[MineID]
Mines[MineID] → Sales[MineID]
Production[Date] → MetalPrices[Date]
```

---

# 🛠️ Customization

This project is designed to be **fully customizable**.

You can easily tweak:

* Number of mines, employees, or records
* Mineral types (copper, gold, lithium, etc.)
* Grade distributions
* Metal prices
* Cost structures (OPEX / CAPEX)

Example:

```python
N_MINES = 5
N_EMPLOYEES = 1000
minerals = ["Copper", "Gold", "Silver"]
```

---

# ⚠️ Notes

* All data is **synthetic** (not real mining data)
* Values are generated using random distributions
* Some relationships are simplified for usability

---

# 💡 Tips

* Use the Excel dataset for **Power BI dashboards**
* Use the SQLite database for **SQL queries and joins**
* Combine both for end-to-end analytics workflows

---

# 📈 Example Applications

* Production vs Revenue dashboards
* Grade distribution analysis
* Equipment utilization tracking
* Financial analysis (OPEX / CAPEX / EBITDA)

---

# 🤝 Contributing

Feel free to:

* Add new tables (e.g., pit phases, scheduling)
* Improve realism (correlations, constraints)
* Extend financial modeling (NPV, cut-off grade logic)

---

# 📄 License

This project is open-source and free to use for educational and portfolio purposes.

---

# ⚒️ Final Note

Although the dataset is mining-focused, the structure can be adapted to:

* Manufacturing
* Energy
* Logistics
* Any asset-heavy industry

Just modify the entities and distributions to fit your use case.
