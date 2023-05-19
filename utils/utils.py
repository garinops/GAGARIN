from fastapi import Request


class Utils(object):
    @staticmethod
    def getRequestHeadersValue(request: Request, key: str):
        if key in request.headers:
            return request.headers[key].replace('\"', '')
