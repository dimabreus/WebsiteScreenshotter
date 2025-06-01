import httpx
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl, Field
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.screenshot import take_screenshot as take_screen
from ..config import turnstile_secret_key

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
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={"code": 429, "message": "Too many requests"}
    )


class ScreenshotRequest(BaseModel):
    website: HttpUrl
    turnstile_token: str = Field(..., min_length=1, title="Cloudflare Turnstile token")


class ScreenshotResponse(BaseModel):
    code: int = Field(example=200)
    message: str = Field(example="OK")
    data: str = Field(example="base64-encoded-image")


async def verify_turnstile_token(token: str, client_ip: str) -> bool:
    """
    Sends a POST request to the Cloudflare Turnstile API to verify the token.
    If the verification is successful (success == True), returns True; otherwise, returns False.
    """
    url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
    payload = {
        "secret": turnstile_secret_key,
        "response": token,
        "remoteip": client_ip
    }
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            res = await client.post(url, data=payload)

            data = res.json()
        except Exception:
            return False

    return data.get("success", False)


@app.post(
    "/take_screenshot",
    response_model=ScreenshotResponse,
    responses={
        400: {
            "description": "Bad Request: either Turnstile failed or URL invalid",
            "content": {
                "application/json": {
                    "examples": {
                        "turnstile_failed": {
                            "summary": "Turnstile verification failed",
                            "value": {
                                "detail": "Turnstile verification failed"
                            }
                        },
                        "invalid_url": {
                            "summary": "Invalid URL",
                            "value": {
                                "detail": "Invalid URL"
                            }
                        }
                    }
                }
            }
        },
        429: {
            "description": "Rate limit exceeded",
            "content": {
                "application/json": {
                    "example": {
                        "code": 429,
                        "message": "Too many requests"
                    }
                }
            }
        }
    },
    summary="Take Screenshot",
    description="Accepts a JSON payload with a `website` field and a `turnstile_token` field, returns the base64-encoded screenshot."
)
@limiter.limit("12/minute")
async def take_screenshot(request: Request, payload: ScreenshotRequest):
    client_ip = request.client.host

    is_turnstile_valid = await verify_turnstile_token(payload.turnstile_token, client_ip)

    if not is_turnstile_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Turnstile verification failed"
        )

    try:
        result: str = take_screen(str(payload.website))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid URL"
        )

    return ScreenshotResponse(
        code=200,
        message="OK",
        data=result
    )
