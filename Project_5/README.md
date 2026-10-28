# 📣 Marketing Campaign Performance Analysis (2024–2026)

An Excel-based analysis of **50,000 marketing campaign records** across **6 channels** and **6 campaign types** — covering a data dictionary, quality checks, 4 pivot tables, and a dashboard with KPI cards, charts, slicers and written insights.

> ⚠️ **This is a modeled (synthetic) practice dataset**, not real customers or real campaign results. The workbook itself says so, so treat the findings as an exercise in analysis rather than as business facts.

---

## 📁 Dataset

| | |
|---|---|
| **File** | `Data_5.xlsx` |
| **Period** | 1 Jan 2024 – 30 Sep 2026 |
| **Records** | 50,000 rows × 20 columns |
| **Campaigns** | 240 `Campaign_ID`s, each shared by many customer records |
| **Customers** | 18,000 unique `Customer_ID`s (the same customer appears in several rows) |
| **Channels** | Affiliate, Display, Email, Paid Search, SMS, Social Media |
| **Campaign types** | Acquisition, Brand Awareness, Loyalty, Product Launch, Retargeting, Seasonal Promotion |
| **Regions** | Central, East, North, South, West |
| **Customer segments** | Active, At Risk, Dormant, High Value, Loyal, New |
| **Currency** | USD |

### Workbook structure

| Sheet | What's inside |
|---|---|
| `Campaign Summary` | Dataset note, 9 headline KPIs, and a channel table (records, impressions, clicks, conversions, spend, revenue, CTR, ROAS) |
| `Data Dictionary` | Description and data type for all 20 fields |
| `Campaign Data` | The 50,000-row table |
| `Pivot Analysis` | 4 pivot tables: channel performance, campaign type performance, revenue by region and device, customer segment outcomes |
| `Charts` | Dashboard with 6 KPI cards, 4 charts, 6 slicers (Customer_Segment, Device, Channel, Campaign_Type, Region, Gender) and written insights and recommendations |

### Key columns

| Column | Description |
|---|---|
| `Campaign_ID`, `Customer_ID`, `Campaign_Date` | Campaign and customer identifiers, and the activity date |
| `Channel`, `Campaign_Type`, `Device` | How the campaign was delivered |
| `Region`, `Age`, `Gender`, `Income_USD`, `Customer_Segment` | Customer attributes (age 18–75, estimated annual income $37,000–$210,500) |
| `Impressions`, `Clicks`, `Conversions` | Engagement funnel |
| `Spend_USD`, `Revenue_USD` | Cost allocated to the record and revenue attributed to its conversions |
| `CTR` | Clicks ÷ impressions |
| `Click_to_Conversion` | Conversions ÷ clicks |
| `ROAS` | Revenue ÷ spend |
| `Outcome` | `Converted` when conversions are above zero, otherwise `No Conversion` |

---

## ✅ Data Quality Checks

This dataset needed no cleaning. It is analysis-ready, and the checks below were run on the `Campaign Data` sheet.

| Check | Result |
|---|---|
| Blank cells | 0 |
| Duplicate rows | 0 |
| Clicks greater than impressions | 0 rows |
| Conversions greater than clicks | 0 rows |
| `CTR`, `Click_to_Conversion` and `ROAS` match their formulas | All 50,000 rows |
| `Outcome` matches `Conversions > 0` | All 50,000 rows |
| Dates after the dataset's end (30 Sep 2026) | 0 |

---

## 📊 Dashboard

![Dashboard](images/Screenshot.png)

---

## 🔍 Key Findings

- **Total spend: $15.32M. Attributed revenue: $158.81M.** That is an overall **ROAS of 10.36x**, or about $143.48M in revenue after marketing spend.
- **Funnel:** 399.8M impressions, 19.5M clicks (4.87% CTR) and 1.70M conversions (8.73% of clicks).
- **SMS is the standout channel.** It brings in **$53.8M (34%) of revenue** from only **4.4% of spend**, with an 80.2x ROAS and a 7.7% CTR.
- **Email is the second most efficient channel**, with a 36.1x ROAS from just $614K in spend.
- **Paid Search takes the biggest share of budget** (46.6% of spend, $7.13M) and returns 24% of revenue, a 5.4x ROAS.
- **Display is the weakest channel**: 3.5x ROAS, a 1.2% CTR, and only 1.6% of revenue.
- **Cost per conversion explains the gap.** Revenue per conversion is almost the same in every channel (about $93), but a conversion costs $1.17 via SMS, $2.60 via Email, $17.27 via Paid Search and $26.90 via Display.
- **Loyalty campaigns return the most** (14.6x ROAS, $37.6M revenue). Brand Awareness returns the least (6.5x).
- **Mobile is the top device** with $56.9M (35.8% of revenue), about $5.5M ahead of Desktop.
- **Regions are very balanced.** West leads with $32.06M, only about $164K ahead of South, and every region sits between $31.3M and $32.1M.
- **High Value customers produce the most conversions** (352,170) and Dormant customers the fewest (206,277), even though each segment has about 8,300 records.
- **Revenue is steady year to year:** $57.6M in 2024, $57.5M in 2025, and $43.7M for January to September 2026.

---

## ⚠️ Things to Know

- **The data is synthetic.** Results such as an 80x ROAS are a product of how the data was modeled, so don't read them as realistic benchmarks.
- **2026 is a partial year** (data ends 30 Sep 2026), so its totals aren't comparable with 2024 and 2025.
- **Don't average the `ROAS` column.** The average of per-record ROAS is 23.2x and the median is 7.1x, while the true overall ROAS (total revenue ÷ total spend) is 10.36x. Over 2,000 records have a ROAS above 100x.
- **The "Total Income" KPI card ($5.44B) is not a meaningful business metric.** It adds up estimated annual income across repeated customer records, so it counts the same customers several times.
- **`Outcome` has almost no variation.** 49,875 of 50,000 records (99.75%) are `Converted` and only 125 are `No Conversion`, so it doesn't separate good and bad records.
- **Spend is "allocated to the record", not real media cost,** so channel efficiency comparisons depend on how that allocation was modeled.
- **The dashboard shows numbers in Indian digit grouping** (e.g. `39,97,96,691`). The values are the same as those in this README, just grouped differently.
- **Gender is split almost exactly in thirds** (Non-binary 16,742, Male 16,670, Female 16,588), which is another sign the data is modeled.

---

## 🛠️ Tools

- Microsoft Excel: pivot tables, slicers, dashboard

## 🚀 How to Use

1. Download `Data_5.xlsx`.
2. Open the `Charts` sheet and use the slicers to filter by Channel, Campaign Type, Region, Device, Customer Segment or Gender.
3. Explore `Pivot Analysis` for the underlying summaries, `Data Dictionary` for field definitions, and `Campaign Summary` for the headline KPIs.

## 📂 Repo Structure

```
.
├── Data_5.xlsx
├── README.md
└── images/
    └── Screenshot.png
```
