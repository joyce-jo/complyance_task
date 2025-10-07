# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict
# backend/app/report.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def build_report_pdf(inputs: dict, results: dict, email: str) -> BytesIO:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    y = height - 80

    c.setFont("Helvetica-Bold", 16)
    c.drawString(60, y, "ROI Simulation Report")
    y -= 30

    c.setFont("Helvetica", 11)
    c.drawString(60, y, f"Email (requested by): {email}")
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, y, "Inputs:")
    y -= 18
    c.setFont("Helvetica", 10)
    for k, v in (inputs or {}).items():
        c.drawString(80, y, f"{k}: {v}")
        y -= 14
        if y < 100:
            c.showPage()
            y = height - 80

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, y, "Results:")
    y -= 18
    c.setFont("Helvetica", 10)
    for k, v in (results or {}).items():
        c.drawString(80, y, f"{k}: {v}")
        y -= 14
        if y < 100:
            c.showPage()
            y = height - 80

    c.showPage()
    c.save()
    buf.seek(0)
    return buf


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
