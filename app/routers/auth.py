from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session
import requests

from app.database import get_db
from app.models.user import User
from app.config import settings
from app.services.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/google/login")
def google_login():
    return {
        "url": (
            "https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={settings.GOOGLE_CLIENT_ID}"
            "&response_type=code"
            "&scope=openid%20email%20profile"
            "&redirect_uri=http://localhost:8000/auth/google/callback"
        )
    }


@router.get("/google/callback")
def google_callback(code: str, db: Session = Depends(get_db)):
    token_res = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": "http://localhost:8000/auth/google/callback",
        },
    ).json()

    user_info = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {token_res['access_token']}"},
    ).json()

    user = db.query(User).filter(User.email == user_info["email"]).first()

    if not user:
        user = User(
            email=user_info["email"],
            name=user_info["name"],
            provider="google",
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    access_token = create_access_token({"sub": str(user.id)})

    return RedirectResponse(
        url=f"http://localhost:3000/auth/callback?token={access_token}"
    )
