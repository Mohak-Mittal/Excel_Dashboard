
# 🚴 Bike Sales Analysis — December 2021

An Excel-based sales analysis of **89 bike sales records** across **6 countries** — covering raw data, a cleaned table, pivot summaries, and a dashboard with KPIs, charts and slicers.

---

## 📁 Dataset

| | |
|---|---|
| **File** | `Data_2.xlsx` |
| **Period** | 1 Dec 2021 – 24 Dec 2021 |
| **Records** | 89 rows (87 unique `Sales_Order #`) |
| **Product category** | Bikes (all Mountain Bikes) |
| **Product variants** | 19 (Mountain-200, Mountain-400-W, Mountain-500 models in different colours and sizes) |
| **Countries** | Australia, Canada, France, Germany, United Kingdom, United States |
| **Customer age range** | 17 – 63 (average ≈ 34) |

### Workbook structure

| Sheet | What's inside |
|---|---|
| `Bike Sales` | Original raw data, 89 rows × 19 columns |
| `Table1` | Cleaned, analysis-ready table |
| `Sales Pivot` | 3 pivot tables: sales by country, age group and gender |
| `Charts` | Dashboard with 6 KPI cards, 3 charts and slicers (Country, Age_Group, Customer_Gender) |

### Key columns

| Column | Description |
|---|---|
| `Sales_Order #`, `Date`, `Day`, `Month`, `Year` | Order identifier and date |
| `Customer_Age`, `Age_Group`, `Customer_Gender` | Customer demographics |
| `Country`, `State` | Where the order was placed |
| `Product_Category`, `Sub_Category`, `Product_Description` | What was sold |
| `Order_Quantity`, `Unit_Cost`, `Unit_Price` | Order inputs |
| `Cost`, `Revenue`, `Profit` | Totals per row (`Revenue − Cost = Profit`) |

---

## 🧹 Data Cleaning

The raw sheet was kept as-is, and cleaning was done in a separate `Table1` sheet.

| Issue in raw data | Fix in `Table1` |
|---|---|
| `Customer_Gender` stored as `F` / `M` | Standardised to `Female` / `Male` |
| 3 `Country` values with stray spaces (e.g. `United  States`) | Trimmed to `United States` |
| 1 misspelled month (`Decmber`) | Corrected to `December` |
| Missing `Day` (1 row) | Filled from the date (5) |
| Missing `Age_Group` (1 row) | Filled from the customer's age (`Adults (35-64)`) |
| Missing `Order_Quantity` (1 row) | Filled with 1 |
| Missing `Product_Description` (1 row) | Set to `Unknown (source missing)` |
| Zero `Unit_Cost` / `Unit_Price` and zero `Cost` / `Revenue` (1–2 rows) | Recalculated so that `Revenue = Quantity × Unit_Price` and `Revenue − Cost = Profit` for every row |
| Column headers with extra spaces (` Unit_Cost `, ` Profit `) | Trimmed |

After cleaning there are no blank cells and no zero revenue or cost values.

---

## 📊 Dashboard

![Dashboard](images/Screenshot.png)

---

## 🔍 Key Findings

- **Total revenue: 363,527** with **profit of 164,551**, an overall margin of about **45.3%** (cost: 198,976).
- **188 units sold** across 89 sales records.
- **United States leads** with 135,784 in revenue (about 37%), followed by **Australia** with 111,506 (about 31%). France (46,175) and Germany (30,010) come next, and Canada and the UK are smallest at about 20,000 each.
- **California** is the top state (75,004), ahead of New South Wales (43,467) and Queensland (39,140).
- **Adults (35–64) generate the most revenue**: 208,551, about 57% of the total. Young Adults (25–34) contribute 119,646 and Youth (<25) 35,330.
- **Female customers account for about 59% of revenue** (216,049 vs 147,478 for male customers).
- **Best-selling variant:** Mountain-200 Black, size 46 (73,440 in revenue, 32 units). The Mountain-200 models make up the top five variants.

---

## ⚠️ Things to Know

- **The data covers only 24 days of December 2021**, so there are no monthly or yearly trends to read from it.
- **All products are Mountain Bikes**, so category and sub-category comparisons aren't possible.
- **The "Order KPIs" card (188) shows units sold**, not the number of orders (87 unique orders).
- **The "Total Unit Price" KPI (173,513) is a sum of unit prices** across rows, which is not the same as revenue. Use the Revenue card for sales totals.
- **One exact duplicate row is kept in `Table1`** (order `261701`, two identical lines). It could be a genuine repeat order or a data-entry duplicate; removing it would reduce revenue by 2,295.
- **Currency isn't stated in the file**, so amounts are shown as plain numbers.

---

## 🛠️ Tools

- Microsoft Excel: data cleaning, pivot tables, slicers, dashboard

## 🚀 How to Use

1. Download `Data_2.xlsx`.
2. Open the `Charts` sheet for the dashboard and use the slicers to filter by Country, Age Group or Gender.
3. Explore `Sales Pivot` for the underlying summaries, and compare `Bike Sales` (raw) with `Table1` (cleaned) to see the fixes.

## 📂 Repo Structure

```
.
├── Data_2.xlsx
├── README.md
└── images/
    └── Screenshot.png
```
