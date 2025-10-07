
---

## Running Locally

### Prerequisites

Make sure you have installed:

- **Python 3.11+**
- **Node.js 18+ & npm**
- **PostgreSQL 14+**

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd <repo-directory>/backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and update values as needed.

4. **Set up the database:**
   - Ensure PostgreSQL is running.
   - Create the database and run migrations:
     ```bash
     createdb <your_db_name>
     python manage.py migrate
     ```

5. **Start the backend server:**
   ```bash
   python manage.py runserver
   ```

---

## Key Features

1. **Quick Simulation** — Enter a few inputs → see savings, ROI, and payback instantly.
2. **Scenario Management (CRUD)** — Save and retrieve simulations by scenario name.
3. **Favorable ROI Logic** — Internal constants ensure automation always looks beneficial.
4. **Email-Gated Reports** — Requires user email before generating downloadable PDF.
5. **Persistent Storage** — Scenarios stored in PostgreSQL.

---

## Sample Inputs & Outputs

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

## Backend Calculation Logic

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

