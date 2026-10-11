from fastapi import FastAPI

from knowledgeos.config import get_settings
from knowledgeos.logging_config import configure_logging
from knowledgeos.schemas import HealthResponse


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        description="Private document intelligence API for KnowledgeOS.",
    )

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            service=settings.app_name,
            version=settings.api_version,
            environment=settings.environment,
        )

    @app.get("/ready", response_model=HealthResponse)
    def ready() -> HealthResponse:
        return HealthResponse(
            status="ok",
            service=settings.app_name,
            version=settings.api_version,
            environment=settings.environment,
        )

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("knowledgeos.main:app", host="0.0.0.0", port=8000, reload=True)
