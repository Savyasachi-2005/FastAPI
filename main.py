from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from db import engine,get_db,base
from routers import blog,user,login,refresh,admin
from repo import user as user_repo
import schemas,models
app=FastAPI()

base.metadata.create_all(bind=engine)

def create_default_users():
    db=Session(bind=engine)
    try:
        user_count = db.query(models.User).count()
        if user_count == 0:
            user_repo.create_user(
                schemas.users(
                    username="Admin User",
                    email="admin@example.com",
                    password="password",
                    role="admin"
                ),
                db
            )
            user_repo.create_user(
                schemas.users(
                    username="Test User",
                    email="test@example.com",
                    password="password",
                    role="user"
                ),
                db
            )
            print("✅ Default users created successfully")
    except Exception as e:
        print(f"Error creating default users: {e}")
        db.rollback()
    finally:
        db.close()
create_default_users()

app.include_router(admin.apirouter)
app.include_router(refresh.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.apirouter)

