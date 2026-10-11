from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(default="ok")
    service: str = Field(default="KnowledgeOS")
    version: str = Field(default="v1")
    environment: str = Field(default="local")


class ReadyResponse(HealthResponse):
    pass
