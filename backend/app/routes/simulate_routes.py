# scenario_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.crud import create_scenario, list_scenarios, get_scenario, delete_scenario
from app.schemas import SaveScenarioRequest

# simulate_routes.py
from fastapi import APIRouter
from app.schemas import SimulateRequest

from typing import Dict

router = APIRouter()


def calculate_roi(data: SimulateRequest) -> Dict:
    monthly_invoice_volume = data.monthly_invoice_volume
    num_ap_staff = data.num_ap_staff
    hourly_wage = data.hourly_wage
    avg_hours_per_invoice = data.avg_hours_per_invoice
    error_rate_manual = data.error_rate_manual
    error_cost = data.error_cost
    one_time_cost = data.one_time_implementation_cost
    horizon = data.horizon_months

    # labor cost if done fully manually per month
    labor_cost_manual = num_ap_staff * hourly_wage * avg_hours_per_invoice * monthly_invoice_volume

    # rough automated processing cost estimate (example formula)
    auto_cost = monthly_invoice_volume * 0.20  # placeholder per-invoice monthly cost

    # error savings: assume automation reduces error rate to 10%
    error_savings = (max(error_rate_manual - 0.1, 0.0)) * monthly_invoice_volume * error_cost

    # monthly savings = (reduced labor + error savings) - automation cost
    monthly_savings = (labor_cost_manual + error_savings - auto_cost) * 1.0

    cumulative_savings = monthly_savings * horizon
    net_savings = cumulative_savings - one_time_cost
    payback_months = one_time_cost / monthly_savings if monthly_savings and monthly_savings != 0 else None
    roi_percentage = (net_savings / one_time_cost) * 100 if one_time_cost and one_time_cost != 0 else None

    results = {
        "labor_cost_manual": round(labor_cost_manual, 2),
        "auto_cost": round(auto_cost, 2),
        "error_savings": round(error_savings, 2),
        "monthly_savings": round(monthly_savings, 2),
        "cumulative_savings": round(cumulative_savings, 2),
        "net_savings": round(net_savings, 2),
        "payback_months": round(payback_months, 2) if payback_months is not None else None,
        "roi_percentage": round(roi_percentage, 2) if roi_percentage is not None else None,
    }
    return results


@router.post("/simulate")
def simulate(payload: SimulateRequest):
    results = calculate_roi(payload)
    return {"inputs": payload.dict(), "results": results}
