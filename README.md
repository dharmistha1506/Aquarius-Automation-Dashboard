# Aquarius Automation Project
  
 End-to-end automation project that extracts employee timesheet data from **PostgreSQL**, transforms it with **Python**, stores it in 
 **OneDrive**, and delivers interactive **Power BI dashboards** with auto-refresh. The solution ensures accurate and up-to-date reporting without 
 manual intervention.

---
## Note on Privacy & Security

This project was developed for a real company use case. Due to privacy and security policies, the original dataset and some scripts cannot be shared or executed publicly.

  ### Instead, this repository includes:
   - Documentation of the end-to-end workflow.
   - Sample scripts (with sensitive details removed).
   - Screenshots of Dashboard structure & KPIs explained.
    The objective is to demonstrate my technical skills in Python, SQL, and Power BI while keeping company data secure.

##  Project Overview
  - Automates exporting employee timesheet data from PostgreSQL.
  - Converts data into CSV format via Python.
  - Uploads CSV automatically to OneDrive.
  - Power BI connects to OneDrive CSV with **auto-refresh** enabled.
  - Dashboards deliver **real-time insights** on employee productivity and timesheet approvals.

---

##  End-to-End Workflow
  1. **PostgreSQL** – SQL script fetches employee timesheet data.
  2. **Python (VS Code)** – Script exports data to CSV.
  3. **Python Script** – Uploads CSV file to OneDrive.
  4. **Power BI** – Connects to OneDrive CSV with scheduled refresh.
  5. **Power Query** – Cleans & validates data:
     - Removes invalid/missing hours  
     - Standardizes date formats  
     - Renames columns for clarity  
  6. **DAX & Calculated Columns** – Create KPIs & anomaly detection.
  7. **Power BI Dashboards** – Visualize KPIs and insights.

---

##  Power BI Features
  ### Data Cleaning & Validation
  - Remove rows with invalid/missing data.
  - Standardize all date formats.
  - Apply meaningful column renaming.
  
  ### DAX Measures & KPIs
  - **Average weekly hours per employee**  
  - **Weekly anomaly detection** (<5 hours/week for >1 week)  
  - **Pending hours tracker** (by department & work type)  
  
  ### Dashboard Visuals
  - **KPI Cards**: Avg weekly hours, anomalies, pending hours  
  - **Pie Chart**: Timesheet approval summary (Pending, Approved, Rejected)  
  - **Bar Chart**: Active vs Total employees (by department)  
  - **Funnel Chart**: Employees exceeding 420 hrs (with drill-through table)  
  - **Slicers**: Month, Quarter, Department  
  - **Drill-through, Tooltip Pages, Bookmarks**  

---

## ⚙️ Automation with Task Scheduler
  - Windows Task Scheduler executes the Python script at scheduled intervals.
  - Fully automated process ensures **no manual intervention**.
  - VS Code is used only for development/testing; production runs use the `.py` file.

---

##  Final Data Flow

PostgreSQL (SQL Script)
↓
Python Script (Export CSV → Upload to OneDrive)
↓
Power BI (Power Query + DAX → Dashboard KPIs & Visuals)
↓
Automation (Windows Task Scheduler → Auto-run Python script)


##  Tech Stack
  - **Database**: PostgreSQL  
  - **Programming**: Python  
  - **Visualization**: Power BI (Power Query, DAX)  
  - **Automation**: Windows Task Scheduler  
  - **Storage**: OneDrive  
---

##  Key Highlights
  - Automated ETL workflow from database → storage → visualization.  
  - Real-time **Power BI dashboards** with automated refresh.  
  - Data cleaning, anomaly detection, and KPI tracking.  
  - Zero manual effort with **Windows Task Scheduler automation**.  
  

