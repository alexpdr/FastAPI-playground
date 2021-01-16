"""
Main file for the application/server
"""
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from api.http.routers import ROUTERS
from api.settings import SETTINGS

# Initialize application with settings
app = FastAPI(**SETTINGS['API'])

# Add routes to our application
[app.include_router(router) for router in ROUTERS]


# Root/Index response
@app.get(
    path='/',
    operation_id="api.index",
    response_class=RedirectResponse,
    response_description="Redirects to docs",
    status_code=307,
    tags=["System"])
async def api_index() -> Response:
    """Redirects inbound users to docs"""
    return RedirectResponse('/docs')
