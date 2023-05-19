from typing import Optional

from pydantic import BaseModel


# 全局schema响应
class Response(BaseModel):
    status_code: Optional[int] = None
    status_description: Optional[list] = []


class ErrorResponse(Response):
    data: Optional[list] = []


# 全局schema元素
class Client(BaseModel):
    host: Optional[str]
    port: Optional[int]

    # orm_mode将告诉 Pydantic以 "ORM模型"读取数据
    class Config:
        orm_mode = True


class Headers(BaseModel):
    host: Optional[str]
    connection: Optional[str]
    content_length: Optional[str]
    sec_ch_ua: Optional[str]
    accept: Optional[str]
    sec_ch_ua_mobile: Optional[str]
    user_agent: Optional[str]
    sec_ch_ua_platform: Optional[str]
    origin: Optional[str]
    sec_fetch_site: Optional[str]
    sec_fetch_mode: Optional[str]
    sec_fetch_dest: Optional[str]
    referer: Optional[str]
    accept_encoding: Optional[str]
    accept_language: Optional[str]
    cookie: Optional[str]

    # orm_mode将告诉 Pydantic以 "ORM模型"读取数据
    class Config:
        orm_mode = True


# signup路由 #################
class Client200Response(Response):
    status_code = 200
    status_description = []
    data: Client = None

    class Config:
        orm_mode = True


class Headers200Response(Response):
    status_code = 200
    status_description = []
    data: Headers = None

    class Config:
        orm_mode = True
