from fastapi import status, APIRouter, Request

from databases import schemas
from utils.utils import Utils

router = APIRouter()


@router.get(
    "/headers",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Headers200Response,
    summary="获取Headers信息")
async def get_headers(request: Request):
    headers = schemas.Headers
    print(request.headers)
    headers.host = Utils.getRequestHeadersValue(request, 'host')
    headers.connection = Utils.getRequestHeadersValue(request, 'connection')
    headers.sec_ch_ua = Utils.getRequestHeadersValue(request, 'sec-ch-ua')
    headers.accept = Utils.getRequestHeadersValue(request, 'accept')
    headers.sec_ch_ua_mobile = Utils.getRequestHeadersValue(request, 'sec-ch-ua-mobile')
    headers.user_agent = Utils.getRequestHeadersValue(request, 'user-agent')
    headers.sec_ch_ua_platform = Utils.getRequestHeadersValue(request, 'sec-ch-ua-platform')
    headers.sec_fetch_site = Utils.getRequestHeadersValue(request, 'sec-fetch-site')
    headers.sec_fetch_mode = Utils.getRequestHeadersValue(request, 'sec-fetch-mode')
    headers.sec_fetch_dest = Utils.getRequestHeadersValue(request, 'sec-fetch-dest')
    headers.referer = Utils.getRequestHeadersValue(request, 'referer')
    headers.accept_encoding = Utils.getRequestHeadersValue(request, 'accept-encoding')
    headers.accept_language = Utils.getRequestHeadersValue(request, 'accept-language')
    headers.cookie = Utils.getRequestHeadersValue(request, 'cookie')
    headers_response = schemas.Headers200Response
    headers_response.data = headers
    return headers_response
