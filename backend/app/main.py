# backend/app/main.py
from fastapi import FastAPI
from .database import init_db
from .routes import simulate_routes, scenario_routes, report_routes

app = FastAPI(title="Invoicing ROI Simulator")

# include routers
app.include_router(simulate_routes.router)
app.include_router(scenario_routes.router)
app.include_router(report_routes.router)

@app.on_event("startup")
def on_startup():
    init_db()
