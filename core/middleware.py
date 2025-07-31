import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp

# class LoggingMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self,request: Request, call_next):
#         start_time = time.time()
#         print(f"Request: {request.method} {request.url}")
#         response = await call_next(request)
#         duration = time.time() - start_time
#         print(f"Response: {response.status_code} in {duration:.2f}s")
#         return response
    
class HeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['prototype-developer'] = 'Abhishek Hiremath'
        response.headers['prototype-version'] = 'v0.1.0'
        response.headers['prototype-name'] = 'Project Sparsha'
        
        
        return response
    
class CustomASGIMiddleware:
    def __init__(self,app : ASGIApp):
        self.app = app
    async def __call__(self, scope,receive,send):
        if scope['type'] == 'http':
            method = scope['method']
            path=scope["path"]
            print(f"[ASGI] --> {method} {path}")
        await self.app(scope,receive,send)
        
        if scope['type'] == 'http':
            print(f"[ASGI] <-- {method} {path} Completed")
        