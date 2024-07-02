import pytest
from pydantic import BaseModel
from typing import List
from be_parkfinite.tests.test_data import test_data
from fastapi.testclient import TestClient
from be_parkfinite.utils.databse_utils import seed_database
from be_parkfinite.utils.test_utils import is_valid_date
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

def test_read_campsites(test_db):
    response = client.get("/campsites")
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data) == 1
    for campsite in response_data:
        assert isinstance(campsite['campsite_name'], str)
        assert isinstance(campsite['description'], str)
        assert isinstance(campsite['added_by'], str)
        assert isinstance(campsite['campsite_longitude'], float)
        assert isinstance(campsite['campsite_latitude'], float)
        assert isinstance(campsite['campsite_id'], int)
        assert isinstance(campsite['category_id'], int)
        assert isinstance(campsite['photos'], list)
        assert isinstance(campsite['date_added'], str)
        assert is_valid_date(campsite['date_added'])


