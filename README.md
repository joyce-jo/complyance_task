#  Invoicing ROI Simulator

A lightweight ROI calculator web app that helps businesses estimate **cost savings**, **ROI**, and **payback period** when switching from manual to automated invoicing.

---

##  Project Overview

This project demonstrates a full-stack implementation of an **ROI simulation tool** with:

* Interactive form input
* Real-time calculations
* Scenario save/load/delete (CRUD)
* PDF report generation gated by email
* Backend bias ensuring positive ROI

---

##  Architecture & Approach

###  Tech Stack

| Layer                 | Technology                  |
| --------------------- | --------------------------- |
| **Frontend**          | React + Vite + TailwindCSS  |
| **Backend**           | FastAPI (Python)            |
| **Database**          | SQLite (via SQLAlchemy ORM) |
| **Report Generation** | ReportLab (PDF)             |
| **API Testing**       | Postman / cURL              |

---

##  Architecture Diagram

```
Frontend (React)
   ↓ (REST API)
Backend (FastAPI)
   ↓
SQLite Database
```

---

##  Key Features

1. **Quick Simulation** — Enter a few inputs → see savings, ROI, and payback instantly.
2. **Scenario Management (CRUD)** — Save and retrieve simulations by scenario name.
3. **Favorable ROI Logic** — Internal constants ensure automation always looks beneficial.
4. **Email-Gated Reports** — Requires user email before generating downloadable PDF.
5. **Persistent Storage** — Scenarios stored locally in SQLite.

---

##  Sample Inputs & Outputs

**Input Example**

| Field                  | Value     |
| ---------------------- | --------- |
| Monthly Invoice Volume | 2000      |
| AP Staff               | 3         |
| Hourly Wage            | 30        |
| Avg Hours/Invoice      | 0.17      |
| Error Rate Manual      | 0.5%      |
| Error Cost             | 100       |
| Horizon                | 36 months |

**Output Example**

```
Monthly Savings: $8,000
Payback Period: 6.3 months
ROI (36 months): 420%
```

---

##  Backend Calculation Logic

```python
labor_cost_manual = num_ap_staff * hourly_wage * avg_hours_per_invoice * monthly_invoice_volume
auto_cost = monthly_invoice_volume * 0.20
error_savings = (error_rate_manual - 0.1) * monthly_invoice_volume * error_cost
monthly_savings = (labor_cost_manual + error_savings - auto_cost) * 1.1
cumulative_savings = monthly_savings * time_horizon_months
net_savings = cumulative_savings - one_time_implementation_cost
payback_months = one_time_implementation_cost / monthly_savings
roi_percentage = (net_savings / one_time_implementation_cost) * 100
```

---

##  Backend API Endpoints

| Method   | Endpoint           | Description                      |
| -------- | ------------------ | -------------------------------- |
| `POST`   | `/simulate`        | Run a simulation and return JSON |
| `POST`   | `/scenarios`       | Save a scenario                  |
| `GET`    | `/scenarios`       | List all scenarios               |
| `GET`    | `/scenarios/{id}`  | Get specific scenario            |
| `DELETE` | `/scenarios/{id}`  | Delete a scenario                |
| `POST`   | `/report/generate` | Generate PDF (requires email)    |

---

##  Running Locally

###  Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API will run at `http://127.0.0.1:8000`

###  Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at `http://localhost:5173`

---

##  Testing

* Open the web app → fill in the form → view live results.
* Click **“Save Scenario”** to persist to database.
* Click **“Generate Report”** to enter email and get a PDF file.
* Test APIs using Postman (`localhost:8000/simulate`).

---

##  Example DB Schema (SQLite)

| id | scenario_name | inputs (JSON) | results (JSON) | created_at |
| -- | ------------- | ------------- | -------------- | ---------- |

---

##  Report Generation

When user enters email, backend validates it and generates a **PDF** using ReportLab containing:

* Input parameters
* Computed ROI, savings, and payback
* Timestamp + email capture

---

##  Future Enhancements

* Add authentication (optional)
* Deploy on Render / Vercel
* Add chart visualization (ROI trends)
* Integrate Mailgun/SendGrid for emailing reports

---

##  Author

**Name:** Joyce S R
**Email:** [joycesr362@gmail.com](mailto:joycesr362@gmail.com)
**GitHub:** joyce_jo
