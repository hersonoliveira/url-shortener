from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urlshortener.main import app, get_db
import urlshortener.models


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./instance/test_app.db"

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

urlshortener.models.Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_main_shorten():
    response = client.post(
        "/shorten",
        json={"url": "www.website.com/resource/user?id=31"}
    )

    assert response.status_code == 200
    data = response.json()

    assert "tier.app" in data
    
    short_url_hash = data[data.index("/") + 1:]
    assert len(short_url_hash) == 7
