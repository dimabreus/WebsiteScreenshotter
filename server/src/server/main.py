from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.screenshot import take_screenshot as take_screen

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter  # type: ignore[attr-defined]


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"code": 429, "message": "Too many requests"}
    )


class ScreenshotRequest(BaseModel):
    website: HttpUrl


@app.post("/take_screenshot")
@limiter.limit("12/minute")
async def take_screenshot(request: Request, payload: ScreenshotRequest):
    data = take_screen(str(payload.website))
    return {
        "code": 200,
        "message": "OK",
        "data": data
    }
