
from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .service import arbitrage_report
from .logger import logger

app = FastAPI(title="Crypto Arbitrage Web")
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse := templates.TemplateResponse)
async def index(request: Request):
    """
    Возвращает HTML-страницу с формой ввода символов
    """
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@app.get("/api/arbitrage", response_class=JSONResponse)
async def api_arbitrage(
    symbols: str = Query(..., description="Comma-separated, e.g. BTCUSDT,ETHUSDT")
):
    """
    Параметр symbols — "BTCUSDT,ETHUSDT", функция возвращает JSON вида:
    { "BTCUSDT": 1.23, "ETHUSDT": 0.56 }
    """
    syms = [s.strip().upper() for s in symbols.split(",") if s.strip()]
    logger.info(f"Web API call, symbols={syms}")
    report = await arbitrage_report(syms)
    return report
