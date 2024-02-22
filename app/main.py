# fastapi
from fastapi import FastAPI
from app.core.modules import init_routers, make_middleware
from app.models import user
from app.core.database import engine

user.Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Tattoo Salon",
        description="BackEnd for FastAPI Tattoo Salon",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()
