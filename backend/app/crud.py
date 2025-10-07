# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict


class SimulateRequest(BaseModel):
    monthly_invoice_volume: int
    num_ap_staff: int
    hourly_wage: float
    avg_hours_per_invoice: float
    error_rate_manual: float
    error_cost: float
    one_time_implementation_cost: float
    horizon_months: int


class SaveScenarioRequest(BaseModel):
    name: str
    inputs: Dict
    results: Dict


class EmailRequest(BaseModel):
    email: EmailStr
    scenario_id: Optional[int] = None
