from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ DB connected")
    except Exception as e:
        print("❌ DB connection failed:", e)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
