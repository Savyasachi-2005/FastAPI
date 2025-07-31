import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request: Request, call_next):
        start_time = time.time()
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        duration = time.time() - start_time
        print(f"Response: {response.status_code} in {duration:.2f}s")
        return response