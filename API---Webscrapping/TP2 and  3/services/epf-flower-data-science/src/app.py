from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from src.api.router import router

def get_application() -> FastAPI:
    application = FastAPI(
        title="epf-flower-data-science",
        description="API documentation for predicting Iris species",
        version="1.0.0",
        docs_url="/docs",  # Swagger UI
        redoc_url="/redoc",  # Optional Redoc UI
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update to your specific origins if needed
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)

    # Root endpoint redirection
    @application.get("/", include_in_schema=False)
    async def root():
        """Redirect root endpoint to Swagger documentation."""
        return RedirectResponse(url="/docs")

    return application


