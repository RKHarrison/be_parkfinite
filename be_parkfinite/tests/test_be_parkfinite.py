import pytest
from fastapi.testclient import TestClient
from be_parkfinite.utils.seed_database import seed_database
from be_parkfinite.main import app, get_db

import models
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

TEST_DB_URL = "sqlite:///./test2.db"
test_engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSession = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine)
testData = campsite = models.Campsite(
            campsite_name="TEST XYZ",
            campsite_longitude=-121.885,
            campsite_latitude=37.338
        )


@pytest.fixture()
def test_db():
    seed_database(test_engine, TestSession, testData)
    yield

def override_get_db():
    try:
        db = TestSession()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_main():
    # act
    response = client.get("/")
    # assert
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_campsites(test_db):
    response = client.get("/campsites")
    print(response.json(), "<<<<<<<<<<")
    assert response.status_code == 200
    assert response.json() == [{'campsite_name': 'TEST XYZ', 'campsite_longitude': -
                                121.885, 'campsite_latitude': 37.338, 'campsite_id': 1, 'photos': []}]
