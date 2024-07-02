import pytest
from pydantic import BaseModel
from typing import List
from be_parkfinite.tests.test_data import test_data
from fastapi.testclient import TestClient
from be_parkfinite.utils.seed_database import seed_database
from be_parkfinite.main import app, get_db

import models
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

TEST_DB_URL = "sqlite:///./test.db"
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
            campsite_latitude=37.338,
            parking_cost=10.1
        )


@pytest.fixture(scope='function')
def test_db():
    seed_database(test_engine, TestSession, test_data)
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


class ExpectedCampsite(BaseModel):
    campsite_name: str
    campsite_longitude: float
    campsite_latitude: float
    parking_cost: float
    facilities_cost: float
    description: str
    campsite_id: int
    category_id: int
    photos: List
    date_added: str
    added_by: str

def test_read_campsites(test_db):
    response = client.get("/campsites")
    print(response.json(), "<<<<<<<<<<")
    assert response.status_code == 200

