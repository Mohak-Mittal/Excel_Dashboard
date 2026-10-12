# 🏥 Hospital Patient Data Analysis 2025

An Excel-based analysis of **500 hospital patient records** across **10 Indian cities** — covering a messy raw dataset, a cleaned table, 6 pivot summaries, and a dashboard with charts and slicers.

---

## 📁 Dataset

| | |
|---|---|
| **File** | `Data_4.xlsx` |
| **Admissions** | 1 Jan 2025 – 27 Dec 2025 (last discharge date: 12 Jan 2026) |
| **Patients** | 500 records (unique `Patient_ID` after cleaning) |
| **Departments** | 7 (Cardiology, Gastroenterology, General Medicine, Neurology, Oncology, Orthopedics, Pediatrics) |
| **Doctors** | 21 named doctors |
| **Diagnoses / treatments** | 29 each |
| **Insurers** | 6 (Bajaj Allianz, Care Health, HDFC ERGO, ICICI Lombard, Max Bupa, Star Health), plus `None / Self Pay` |
| **Cities** | Ahmedabad, Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Jaipur, Kolkata, Mumbai, Pune |
| **Currency** | INR |

### Workbook structure

| Sheet | What's inside |
|---|---|
| `hospitalpatientunclean` | Original raw data, preserved unchanged (500 rows × 15 columns) |
| `hospital_patient_data` | Cleaned table (500 rows × 16 columns, no blank cells) |
| `Pivot Summary` | 6 pivot tables: age group, gender, city billings, doctor, insurance, payment status |
| `Chart` | Hospital Patient Dashboard with 6 charts and slicers (City, Age_Group, Doctor, Payment_Status, Gender, Insurance) |

### Key columns

| Column | Description |
|---|---|
| `Patient_ID`, `Patient_Name` | Patient identifier and name |
| `Age`, `Age_Group`, `Gender`, `City` | Demographics (`Age_Group` was added during cleaning: 0-17, 18-35, 36-50, 51-65, 66+) |
| `Department`, `Doctor` | Where and by whom the patient was treated |
| `Diagnosis`, `Treatment` | Medical details |
| `Admission_Date`, `Discharge_Date` | Stay dates |
| `Bill_Amount` | Bill in INR |
| `Insurance`, `Payment_Status` | Coverage and payment state |
| `Patient_Status` | Admitted, Discharged, Discharged Against Medical Advice, Transferred or Expired |

---

## 🧹 Data Cleaning

The raw sheet was kept as-is, and cleaning was done in a separate sheet. The raw sheet has an extra placeholder header row (`Column1`…`Column15`) above the real headers. All 500 rows were kept.

### Standardising

| Column | Issue in raw data | Fix |
|---|---|---|
| `Patient_ID` | 36 malformed (e.g. `PAT-135`) or blank IDs | Replaced with sequential IDs (`HOSP-10001` to `HOSP-10500`) |
| `Gender` | `M`, `F`, `male`, `female` (42 rows) | Standardised to `Male` / `Female` |
| `City` | 29 lowercase values | Standardised case |
| `Department` | 28 variants (`Gen. Med`, `Cardio`, `Paediatrics`, `ONCOLOGY`) | Mapped to the 7 department names |
| `Doctor` | Mixed formats (`dr. anoop misra`, `Anoop Misra`) | Standardised to `Dr. Anoop Misra` |
| `Admission_Date`, `Discharge_Date` | Mixed formats (`2025-05-11`, `05-18-2025 00:00`, `27/03/2025`, `11 Oct 2025`) | Converted to proper dates |
| `Bill_Amount` | 63 text values with `₹` and commas (`₹51,199.60`) | Converted to numbers |
| `Insurance` | `none` in lowercase (22 rows) | Standardised to `None / Self Pay` |
| `Payment_Status` | Variants such as `CLAIM_PENDING`, `pending`, `PAID` | Standardised (`CLAIM_PENDING` → `Claim Processing`) |
| `Patient_Status` | `DAMA`, `in-patient`, `deceased`, uppercase variants | Standardised (`DAMA` → `Discharged Against Medical Advice`, `in-patient` → `Admitted`, `deceased` → `Expired`) |
| `Diagnosis`, `Treatment` | Mixed casing (`THROMBOLYSIS`) | Standardised to title case |

### Invalid and missing values

| Column | Issue | Fix |
|---|---|---|
| `Age` | 22 values like `56 yrs` | Converted to numbers |
| `Age` | 22 impossible values (negative, or above 120 such as 160 and 999) and 20 blanks | All 42 replaced with the median age (44) |
| `Bill_Amount` | 20 invalid values (negative amounts and a 99,999,999 placeholder) | Replaced with the median bill (₹192,719.37) |
| `Bill_Amount` | 21 blanks | Set to 0 |
| `Discharge_Date` | 122 blanks | Filled (62 were set equal to the admission date) |
| `Admission_Date` | 24 blanks | Filled |
| `Insurance` | 32 blanks | 11 set to `None / Self Pay`, 21 set to `Unknown` |
| Other text columns (name, gender, city, department, doctor, diagnosis, payment status, patient status) | Blanks | Set to `Unknown` |

---

## 📊 Dashboard

![Dashboard](images/Screenshot.png)

---

## 🔍 Key Findings

- **Total billing: ₹91,950,692** across 500 patients, an average of about **₹183,900** per patient.
- **Hyderabad has the highest billing** (₹10.73M), followed by Pune (₹9.72M) and Chandigarh (₹9.40M).
- **Oncology is the largest department** (82 patients, ₹14.79M in bills). **Pediatrics has the highest average bill** (₹211,082).
- **Dr. Suresh Advani treated the most patients** (32), followed by Dr. SKS Marya (30) and Dr. P. N. Renjen (28).
- **Age mix:** 66+ is the largest group (121 patients), then 36–50 (120), 18–35 (99), 0-17 (82) and 51–65 (78).
- **Gender split is even:** 243 male and 235 female patients, plus 22 unknown or unspecified.
- **Only 111 patients (22%) have fully paid.** The rest are Disputed (102), Pending (93), Claim Processing (89), Partially Paid (82), Unknown (21) or Unpaid (2).
- **Self-pay is the largest insurance group** (104 patients, 21%). Each of the 6 insurers covers 56–68 patients.
- **Patient outcomes:** 110 Admitted, 104 Discharged Against Medical Advice, 100 Discharged, 93 Expired (18.6%), 78 Transferred and 15 Unknown.

---

## ⚠️ Things to Know

- **City names aren't fully merged.** `Bangalore` (32) and `Bengaluru` (1), `Mumbai` and `Bombay` (2), and `Kolkata` and `Calcutta` (2) are still counted separately in the pivots and the billing chart. Combined, Mumbai would have 57 patients, which makes it the largest city.
- **42 ages (8%) were replaced with the median of 44**, which all fall in the 36–50 group. Without them that group would have about 78 patients instead of 120.
- **Bill totals include 41 estimated or zero values:** 20 set to the median and 21 set to 0. Totals and averages are approximate.
- **Every patient has a discharge date, including the 110 still marked `Admitted`.** Filled discharge dates make stay lengths unreliable: the average is 47 days for filled rows versus 13 days for original ones, and the longest stay is 298 days.
- **Some date formats are ambiguous** (e.g. `10/06/2025` could be 10 June or 6 October). `Admission_Date` and `Discharge_Date` may contain swapped day and month values.
- **The "Operations by Doctor" chart counts patient records**, not operations performed, and it includes 23 `Unknown` records.
- **11 blank insurance values were assumed to be self-pay.** This is an assumption, not a recorded fact.
- **Diagnosis casing has a small bug:** `Parkinson's Disease` became `Parkinson'S Disease`.
- **The workbook has no cleaning log.** The cleaning steps above were reconstructed by comparing the raw and cleaned sheets.

---

## 🛠️ Tools

- Microsoft Excel: data cleaning, pivot tables, slicers, dashboard

## 🚀 How to Use

1. Download `Data_4.xlsx`.
2. Open the `Chart` sheet and use the slicers to filter by City, Age Group, Doctor, Payment Status, Gender or Insurance.
3. Explore `Pivot Summary` for the underlying numbers, and compare `hospitalpatientunclean` with `hospital_patient_data` to see the fixes.

## 📂 Repo Structure

```
.
├── Data_4.xlsx
├── README.md
└── images/
    └── Screenshot.png
```
