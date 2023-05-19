from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from Exceptions.CustomHTTPException import GagarinHTTPExceptions
from routers import client, headers

gagarin = FastAPI(
    title="GAGARIN",
    version="0.1.0",
    contact={
        "name": "GARIN ASSET LLC",
        "url": "https://garinasset.com",
        "email": "root@garinasset.com",
    },
    openapi_url="/v1/openapi.json",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
)


@gagarin.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    return GagarinHTTPExceptions.gagarinHTTPExceptionType(exc.status_code, exc.detail, exc.headers)


origins = [
    "https://developers.garinasset.com",
]

gagarin.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # 指示跨域请求支持 cookies。默认是 False。
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@gagarin.get("/v1")
async def root():
    return {"Hello Gagarin!"}


gagarin.include_router(client.router, prefix='/v1/request', tags=["客户端"])
gagarin.include_router(headers.router, prefix='/v1/request', tags=["HTTP头部"])
