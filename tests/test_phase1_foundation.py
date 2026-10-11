from fastapi.testclient import TestClient

from knowledgeos.config import Settings
from knowledgeos.main import create_app


def test_settings_defaults(monkeypatch):
    monkeypatch.delenv("KNOWLEDGEOS_ENV", raising=False)
    monkeypatch.delenv("KNOWLEDGEOS_APP_NAME", raising=False)
    monkeypatch.delenv("KNOWLEDGEOS_DATABASE_URL", raising=False)

    settings = Settings()

    assert settings.app_name == "KnowledgeOS"
    assert settings.api_version == "v1"
    assert settings.database_url.startswith("sqlite://")


def test_health_endpoint():
    app = create_app()
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "KnowledgeOS"
    assert body["status"] == "ok"
