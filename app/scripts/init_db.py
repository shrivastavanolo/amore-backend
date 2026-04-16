from app.database import engine
from app.models.user import User
from app.models.project import Project

def init_db():
    print("Creating tables...")
    User.__table__.create(bind=engine, checkfirst=True)
    Project.__table__.create(bind=engine, checkfirst=True)
    print("Done.")

if __name__ == "__main__":
    init_db()
