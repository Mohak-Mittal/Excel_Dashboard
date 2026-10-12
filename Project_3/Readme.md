# 🍽️ Zomato Order Performance Analysis 2024

An Excel-based analysis of **445 food-delivery orders** across **10 Indian cities** — covering a messy raw dataset, a documented cleaning log, 8 pivot tables, and a dashboard with charts and slicers.

---

## 📁 Dataset

| | |
|---|---|
| **File** | `Data_3.xlsx` |
| **Period** | 1 Jan 2024 – 5 Dec 2024 |
| **Orders** | 445 (unique `Order_ID` after cleaning) |
| **Restaurants** | 13 (Barbeque Nation, Behrouz Biryani, Bikanervala, Burger King, Chai Point, Dominos Pizza, Faasos, Haldiram's, KFC, Paradise Biryani, Subway, Wow! Momo, plus `Unknown`) |
| **Cities** | Ahmedabad, Bengaluru, Chennai, Delhi, Hyderabad, Jaipur, Kolkata, Lucknow, Mumbai, Pune |
| **Cuisines** | 36 labels, including combinations such as "Italian, Chinese" |
| **Delivery partners** | Dunzo, Grab, In-house, Rapido, Shadowfax, Zomato Valet |
| **Currency** | INR |

### Workbook structure

| Sheet | What's inside |
|---|---|
| `zomato_unclean_dataset_500` | Original raw data, preserved unchanged (445 rows × 15 columns) |
| `Cleaning_Log` | Every cleaning step, the number of rows affected, and notes |
| `Cleaned_Data` | Final analysis-ready table (445 rows × 18 columns, no blank cells) |
| `Pivot Analysis` | 8 pivot tables: city, order status, cuisine, delivery partner, restaurant, payment method, order size, discount basis |
| `Charts` | Dashboard with 5 charts and slicers (City, Order_Status, Cuisine, Restaurant, Payment_Mode) |

### Key columns

| Column | Description |
|---|---|
| `Order_ID`, `Order_Date` | Order identifier and date |
| `Restaurant`, `City`, `Cuisine` | Where the order came from |
| `Customer_Age`, `Rating` | Customer age (18–65) and rating (1–5) |
| `Delivery_Time_Min` | Delivery time in minutes (numeric) |
| `Order_Value_INR`, `Number_of_Items` | Order size |
| `Discount_Input`, `Discount_Basis`, `Discount_Amount_INR`, `Discount_Rate` | Original discount value, how it was interpreted (rate or INR amount), and the resulting amount and rate |
| `Payment_Mode`, `Order_Status`, `Delivery_Partner` | Payment, fulfilment and logistics |
| `Profit_INR` | Profit per order |

---

## 🧹 Data Cleaning

The raw sheet was kept as-is, and every step below was applied to a separate `Cleaned_Data` sheet.

### Standardising

| Area | Action | Rows affected |
|---|---|---|
| Order ID | Rebuilt malformed or blank IDs from the sorted sequence | 34 |
| Restaurant | Fixed casing and character substitutions (`B@rbeque N@ti0n` → `Barbeque Nation`) | 68 |
| City | Standardised case and aliases (`Bangalore` → `Bengaluru`, `Bombay` → `Mumbai`, `Calcutta` → `Kolkata`) | 75 |
| Cuisine | Standardised case and removed repeated labels; compound cuisines kept | 18 |
| Delivery time | Converted text such as `39 mins` into numeric minutes | 99 |
| Discount | Converted fractional inputs (e.g. `0.2`) into INR amounts; original input and basis kept | 137 |
| Payment mode | Standardised aliases (`CC` → `Credit Card`, `COD` → `Cash on Delivery`) | 24 |
| Order status | Fixed spelling and case (`delvrd` → `Delivered`) | 13 |
| Delivery partner | Standardised case and brand labels | 23 |

### Handling missing values

| Type | Fix | Cells filled |
|---|---|---|
| Categorical (restaurant, city, cuisine, payment mode, order status, delivery partner) | Set to `Unknown` | 112 |
| Customer age, delivery time, order value | Median | 74 |
| Order date, rating, number of items | Mode | 56 |
| Discount and profit | Zero | 64 |

---

## 📊 Dashboard

![Dashboard](images/Screenshot.png)

---

## 🔍 Key Findings

- **Total gross order value: ₹571,710** across 445 orders (average order value about **₹1,285**), with total profit of **₹35,145**, a thin margin of about **6.1%**.
- **Mumbai is the top city** by orders (52) and gross value (₹68,340), followed by Kolkata (50 orders) and Jaipur (48). Chennai is the smallest (32 orders).
- **Subway has the highest profit** (₹4,703), ahead of Dominos Pizza (₹3,635) and Paradise Biryani (₹3,270). **Wow! Momo** (₹58,869) and **Subway** (₹58,728) lead on gross order value.
- **Chinese is the biggest single cuisine** (₹64,529), followed by South Indian, Mughlai and Italian at ₹56,000–58,000 each.
- **Dunzo is the fastest delivery partner** (44.0 minutes on average) and Shadowfax the slowest (49.4). The overall average is **46.9 minutes**.
- **Payments are evenly spread**: UPI (80 orders), Credit Card (79) and Wallet (73) lead. Cash on Delivery carries the largest discount total (₹14,226).
- **Order size doesn't drive order value.** Orders with 1 item average ₹1,368, and orders with 10 items average ₹1,207.
- **Average rating is about 3.1 / 5.** Bengaluru has the lowest city rating (2.78) and Pune the highest (3.32).

---

## ⚠️ Things to Know

- **Only 273 of 445 orders (61%) were delivered.** The headline totals also include Cancelled (80), Refunded (71), Failed (5), Pending (4) and Unknown (12) orders. Delivered orders alone account for ₹346,697 in order value and ₹22,032 in profit.
- **96 orders (22%) have negative profit**, totalling −₹3,720.
- **Almost all orders fall between January and July.** August to December has only 17 orders in total, so monthly trends in the second half of the year aren't reliable.
- **Missing values were imputed**, so averages (rating, age, delivery time) are pulled towards the middle. 194 numeric and date cells were filled, and the flag column that marked them was later removed, so imputed rows can't be identified in `Cleaned_Data`.
- **The `Cleaning_Log` contradicts itself.** One row says "No values were imputed", while later rows document imputation. The later rows match the data, so the first row is outdated.
- **34 order IDs are reconstructed**, not original, so they shouldn't be matched to external records.
- **The discount basis is an assumption.** Small fractional inputs were treated as rates and larger numbers as INR amounts (308 orders as INR amounts, 137 as rates). Some rate-based discounts are very high (up to about 89% of the order value).
- **The raw sheet is named `..._500` but contains 445 rows.**
- **The cuisine pivot mixes single and combined labels** (e.g. "Italian" and "Italian, Chinese"), which splits one cuisine across several rows.

---

## 🛠️ Tools

- Microsoft Excel: data cleaning, pivot tables, slicers, dashboard

## 🚀 How to Use

1. Download `Data_3.xlsx`.
2. Open the `Charts` sheet and use the slicers to filter by City, Order Status, Cuisine, Restaurant or Payment Mode.
3. Explore `Pivot Analysis` for the underlying summaries, `Cleaning_Log` for every cleaning step, and compare the raw and `Cleaned_Data` sheets to see the fixes.

## 📂 Repo Structure

```
.
├── Data_3.xlsx
├── README.md
└── images/
    └── Screenshot.png
```
