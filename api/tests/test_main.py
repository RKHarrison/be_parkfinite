from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

import pytest
from fastapi.testclient import TestClient

from database.database import Base
from api.main import app, get_db
from api.tests.test_data import get_test_data
from api.utils.database_utils import seed_database
from api.utils.test_utils import is_valid_date


client = TestClient(app)

TEST_DB_URL = "sqlite:///"
test_engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSession = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestSession()
    return db


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope='function')
def test_db():
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)
    test_session = override_get_db()

    try:
        test_data = get_test_data()
        seed_database(test_session, test_data)
        yield test_session
    finally:
        Base.metadata.drop_all(test_engine)
        test_session.close()


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_campsites(test_db):
    response = client.get("/campsites")
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data) == 3
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