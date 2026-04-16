from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, users, projects, templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Amore API", version="1.0.0")

@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ DB connected and tables ready")
    except Exception as e:
        print("❌ DB connection failed:", e)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # "http://localhost:3000",
        # "http://localhost:5173",
        # "http://127.0.0.1:3000",
        # "http://127.0.0.1:5173",
        "*"
    ],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(templates.router)

@app.get("/")
def root():
    return {"status": "Amore API running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}