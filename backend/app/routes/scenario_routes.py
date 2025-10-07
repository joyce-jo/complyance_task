# backend/app/routes/scenario_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..database import get_session
from ..crud import create_scenario, list_scenarios, get_scenario, delete_scenario
from ..schemas import SaveScenarioRequest
from typing import List

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.post("", status_code=201)
def create(payload: SaveScenarioRequest, session: Session = Depends(get_session)):
    sc = create_scenario(session, payload.name, payload.inputs, payload.results)
    return sc


@router.get("", response_model=List[dict])
def get_all(session: Session = Depends(get_session)):
    return list_scenarios(session)


@router.get("/{scenario_id}")
def get_one(scenario_id: int, session: Session = Depends(get_session)):
    sc = get_scenario(session, scenario_id)
    if not sc:
        raise HTTPException(status_code=404, detail="Not found")
    return sc


@router.delete("/{scenario_id}")
def remove(scenario_id: int, session: Session = Depends(get_session)):
    ok = delete_scenario(session, scenario_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
