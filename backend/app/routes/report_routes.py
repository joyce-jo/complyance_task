# backend/app/routes/report_routes.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session

from app.database import get_session
from app.schemas import EmailRequest
from app.report import build_report_pdf
from app.crud import get_scenario

router = APIRouter(prefix="/report", tags=["report"])


@router.post("/generate")
def generate_report(payload: EmailRequest, session: Session = Depends(get_session)):
    inputs = {}
    results = {}
    if payload.scenario_id:
        sc = get_scenario(session, payload.scenario_id)
        if not sc:
            raise HTTPException(status_code=404, detail="Scenario not found")
        inputs = sc.inputs
        results = sc.results

    pdf_buf = build_report_pdf(inputs, results, payload.email)
    return StreamingResponse(pdf_buf, media_type="application/pdf")
