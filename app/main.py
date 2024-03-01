# fastapi
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.modules import init_routers, make_middleware
from app.models import user
from app.core.database import engine

user.Base.metadata.create_all(bind=engine)



def create_app() -> FastAPI:
    app_ = FastAPI(
        root_path="/tattoo/app",
        docs_url="/docs",
        title="Tattoo Salon",
        description="BackEnd for FastAPI Tattoo Salon",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.route('/error')
async def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})
    
@app.get("/home")
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})