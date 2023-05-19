from fastapi import status, APIRouter, Request

from databases import schemas

router = APIRouter()


@router.get(
    "/client",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Client200Response,
    summary="获取Client信息")
async def get_client(request: Request):
    client = schemas.Client
    client.host = request.client.host
    client.port = request.client.port
    client_response = schemas.Client200Response
    client_response.data = client
    return client_response
