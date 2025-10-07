# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List
from sqlmodel import select, Session
from .models import Scenario

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
    
def create_scenario(session: Session, name: str, inputs: dict, results: dict) -> Scenario:
    sc = Scenario(name=name, inputs=inputs, results=results)
    session.add(sc)
    session.commit()
    session.refresh(sc)
    return sc

def list_scenarios(session: Session) -> List[Scenario]:
    return session.exec(select(Scenario).order_by(Scenario.created_at.desc())).all()

def get_scenario(session: Session, scenario_id: int) -> Optional[Scenario]:
    return session.get(Scenario, scenario_id)

def delete_scenario(session: Session, scenario_id: int) -> bool:
    obj = session.get(Scenario, scenario_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False
