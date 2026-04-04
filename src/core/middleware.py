from starlette.middleware.base import BaseHTTPMiddleware


class PrepopulateUserSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.user = {"name": "jeckonia"}
        response = await call_next(request)
        return response
