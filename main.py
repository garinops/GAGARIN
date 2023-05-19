from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from Exceptions.CustomHTTPException import ToosHTTPExceptions
from routers import client, headers

tools = FastAPI(
    title="TOOLS",
    version="0.1.0",
    contact={
        "name": "GARIN ASSET LLC",
        "url": "https://developers.garinasset.com",
        "email": "root@garinasset.com",
    },
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
)


@tools.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    return ToosHTTPExceptions.toolsHTTPExceptionType(exc.status_code, exc.detail, exc.headers)


origins = [
    "https://developers.garinasset.com",
    "http://127.0.0.1:5501",
    "http://172.16.1.5:5501",

]

tools.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # 指示跨域请求支持 cookies。默认是 False。
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@tools.get("/v1")
async def root():
    return {"Hello Tools!"}


tools.include_router(client.router, prefix='/v1/request', tags=["客户端"])
tools.include_router(headers.router, prefix='/v1/request', tags=["HTTP头部"])
