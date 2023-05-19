from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from databases import schemas


class GagarinHTTPExceptions:
    @staticmethod
    def gagarinHTTPExceptionType(status_code: int, detail: str = None, headers: dict = None):
        match status_code, detail:
            # 登录 @ 邮箱或密码不正确
            case 400, 'AuthLoginErrorEmailPasswordIncorrect':
                response = jsonable_encoder(schemas.AuthLogin400EmailPasswordIncorrectResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 登录 @ 昵称或密码不正确
            case 400, 'AuthLoginErrorUsernamePasswordIncorrect':
                auth_login_error_username_password_incorrect_response = jsonable_encoder(schemas.AuthLogin400UsernamePasswordIncorrectResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=auth_login_error_username_password_incorrect_response,
                    headers=headers
                )
            # 登录 @ 用户不存在
            case 404, 'AuthLoginErrorUserNotFound':
                response = jsonable_encoder(schemas.AuthLogin404UserNotFoundResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 鉴权 @ Token失效
            case 401, 'AuthErrorUserAccessTokenInvalid':
                auth_error_user_access_token_invalid_response = jsonable_encoder(schemas.Auth401UserAccessTokenInvalidResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=auth_error_user_access_token_invalid_response,
                    headers=headers
                )
            # 鉴权 @ 欺骗性Token
            case 403, 'AuthErrorUserAccessTokenForbidden':
                auth_error_user_access_token_forbidden_response = jsonable_encoder(schemas.Auth403UserAccessTokenForbiddenResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=auth_error_user_access_token_forbidden_response,
                    headers=headers
                )
            # 创建账号 - 验证邮箱 @ 无效Token
            case 400, 'SignupVerifyEmailErrorUnauthorized':
                signup_verify_email_error_unauthorized_response = jsonable_encoder(schemas.SignupVerifyEmail401Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=signup_verify_email_error_unauthorized_response,
                    headers=headers
                )
            # 创建账号 - 验证邮箱 @ 欺骗性请求
            case 400, 'SignupVerifyEmailErrorForbidden':
                signup_verify_email_error_forbidden_response = jsonable_encoder(schemas.SignupVerifyEmail403Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=signup_verify_email_error_forbidden_response,
                    headers=headers
                )
            # 注册 - 预验证  @ 用户名不可用
            case 409, 'SignupAcceptUsernameErrorConflict':
                signup_accept_username_error_conflict_response = jsonable_encoder(schemas.SignupAcceptUsername409Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=signup_accept_username_error_conflict_response,
                    headers=headers
                )
            # 注册 - 预验证 @ 邮箱不可用
            case 409, 'SignupAcceptEmailErrorConflict':
                signup_accept_email_error_conflict_response = jsonable_encoder(schemas.SignupAcceptEmail409Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=signup_accept_email_error_conflict_response,
                    headers=headers
                )
            # 注册 - 二次验证 @ 昵称或邮箱不可用
            case 409, 'SignupErrorConflict':
                response = jsonable_encoder(schemas.Signup409Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 查找账号 @ 找不到账号
            case 400, 'AccountEmailFindErrorNotFound':
                response = jsonable_encoder(schemas.AccountEmailFind400Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 忘记密码 - 发送邮件 @ 找不到账号
            case 400, 'AccountPasswordForgetResetSendemailErrorEmailIncorrect':
                response = jsonable_encoder(schemas.AccountPasswordForgerResetSendemail400Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 忘记密码 - 验证邮件 - 重置密码 @ 无效Token
            case 400, 'AccountPasswordForgetResetVerifyEmailErrorUnauthorized':
                response = jsonable_encoder(schemas.AccountPasswordForgetResetVerifyEmail401Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 忘记密码 - 验证邮件 - 重置密码 @ 欺骗性请求
            case 400, 'AccountPasswordForgetResetVerifyEmailErrorForbidden':
                response = jsonable_encoder(schemas.AccountPasswordForgetResetVerifyEmail403Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 忘记密码 - 验证邮件 - 重置密码 @ 账号不存在
            case 404, 'AccountPasswordForgetResetVerifyEmailErrorUserNotFound':
                response = jsonable_encoder(schemas.AccountPasswordForgetResetVerifyEmail404Response().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 删除账号 @ 无效Token
            case 401, 'AccountDeleteErrorAccountDeleteAccessTokenInvalid':
                response = jsonable_encoder(schemas.AccountDelete401AccountDeleteAccessTokenInvalidResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 删除账号 @ 欺骗性请求
            case 403, 'AccountDeleteErrorAccountDeleteAccessTokenForbidden':
                response = jsonable_encoder(schemas.AccountDelete403AccountDeleteAccessTokenForbiddenResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 账号 - 删除账号 @ 账号不存在
            case 404, 'AccountDeleteErrorUserNotFound':
                response = jsonable_encoder(schemas.AccountDelete404UserNotFoundResponse().dict())
                return JSONResponse(
                    status_code=status_code,
                    content=response,
                    headers=headers
                )
            # 其他错误响应
            case _:
                return JSONResponse(
                    status_code=status_code,
                    content={
                        "status_code": status_code,
                        "status_description": [detail, detail],
                        "data": []
                    },
                    headers=headers
                )
