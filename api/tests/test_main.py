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


@pytest.mark.main
class TestServerHealth:
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}


@pytest.mark.main
class TestGetCampsites:
    def test_read_campsites(self, test_db):
        response = client.get("/campsites")
        assert response.status_code == 200
        campsites = response.json()

        assert len(campsites) == 3
        for campsite in campsites:
            assert isinstance(campsite['campsite_name'], str)
            assert isinstance(campsite['campsite_id'], int)
            assert is_valid_date(campsite['date_added'])
            assert isinstance(campsite['added_by'], str)
            assert isinstance(campsite['campsite_longitude'], float)
            assert isinstance(campsite['campsite_latitude'], float)
            assert isinstance(campsite['category']['category_name'], str)
            assert isinstance(campsite['category']['category_img_url'], str)
            assert isinstance(campsite['photos'], list)
            assert isinstance(campsite['parking_cost'], (float, type(None)))
            assert isinstance(campsite['facilities_cost'], (float, type(None)))
            assert isinstance(campsite['description'], str)
            assert isinstance(campsite['approved'], bool)
            assert isinstance(campsite['contact'], list)

            for photo in campsite['photos']:
                assert isinstance(photo['campsite_photo_url'], str)
                assert isinstance(photo['campsite_photo_id'], int)
                assert isinstance(photo['campsite_id'], int)

            for detail in campsite['contact']:
                assert isinstance(detail['campsite_contact_name'], str)
                assert isinstance(detail['campsite_contact_phone'], str)
                assert isinstance(detail['campsite_contact_email'], (str, type(None)))
                assert isinstance(detail['campsite_contact_id'], int)
                assert isinstance(detail['campsite_id'], int)


@pytest.mark.main
class TestGetCampsiteById:
    def test_read_campsites_by_campsite_id(self, test_db):
        response = client.get("/campsites/1")
        assert response.status_code == 200
        assert response.json()['campsite_id'] == 1

    def test_404_campsite_not_found(self, test_db):
        response = client.get("/campsites/987654321")
        assert response.status_code == 404
        assert response.json()["detail"] == "404 - Campsite Not Found!"


@pytest.mark.main
class TestGetUsers:
    def test_read_users(self, test_db):
        response = client.get("/users")
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 3


@pytest.mark.main
class TestGetReviews:
    def test_read_reviews_by_campsite_id(self, test_db):
        response = client.get("/campsites/1/reviews")
        assert response.status_code == 200
        reviews = response.json()
        assert len(reviews) == 3

    def test_read_reviews_by_different_campsite_id(self, test_db):
        response = client.get("/campsites/2/reviews")
        assert response.status_code == 200

    def test_404_reviews_not_found(self, test_db):
        response = client.get("/campsites/987654321/reviews")
        assert response.status_code == 404
        assert response.json()["detail"] == "404 - Reviews Not Found!"


@pytest.mark.current
class TestPostCampsite:
    def test_basic_campsite_with_category(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "photos": [],
            "parking_cost": 10.30,
            "facilities_cost": 2.50,
            "added_by": "PeakHiker92",
            "category_id": 3,
            "opening_month": "April",
            "closing_month": "May"
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201
        posted_campsite = response.json()

        assert posted_campsite['campsite_id'] == 4
        assert is_valid_date(posted_campsite['date_added'])
        assert posted_campsite['campsite_name'] == "TEST NAME"
        assert posted_campsite["campsite_longitude"] == 1.23
        assert posted_campsite["campsite_latitude"] == 4.56
        assert posted_campsite['parking_cost'] == 10.30
        assert posted_campsite['facilities_cost'] == 2.50
        assert posted_campsite['added_by'] == "PeakHiker92"
        assert posted_campsite['category']['category_id'] == 3
        assert posted_campsite['category']['category_name'] == "Campsite"
        assert posted_campsite['category']['category_img_url'] == "https://example.com/category4.jpg"
        assert posted_campsite['opening_month'] == "April"
        assert posted_campsite['closing_month'] == "May"
        assert posted_campsite['photos'] == []
        assert posted_campsite['approved'] == False
        assert posted_campsite['contact'] == []
        assert posted_campsite['activities'] is None
        assert posted_campsite['facilities'] is None
        assert posted_campsite['description'] is None

    def test_campsite_with_photo(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "added_by": "PeakHiker92",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "category_id": 3,
            "photos": [{"campsite_photo_url": "https://testphoto1.com/p1.jpg"}],
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201

        posted_campsite = response.json()
        assert len(posted_campsite['photos']) == 1

        posted_photo = posted_campsite['photos'][0]
        assert posted_photo['campsite_photo_id'] == 3
        assert posted_photo['campsite_photo_url'] == "https://testphoto1.com/p1.jpg"
        assert posted_photo['campsite_id'] == posted_campsite['campsite_id']

    def test_campsite_multiple_photos(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "added_by": "PeakHiker92",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "category_id": 3,
            "photos": [
                {"campsite_photo_url": "https://testphoto.com/p1.jpg"}, 
                {"campsite_photo_url": "https://testphoto.com/p2.jpg"}, 
                {"campsite_photo_url": "https://testphoto.com/p3.jpg"}
                ]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201

        posted_campsite = response.json()
        assert len(posted_campsite['photos']) == 3
        assert posted_campsite['photos'] == [
            {
            "campsite_photo_url": "https://testphoto.com/p1.jpg",
            "campsite_photo_id": 3,
            "campsite_id": 4
            },
            {
            "campsite_photo_url": "https://testphoto.com/p2.jpg",
            "campsite_photo_id": 4,
            "campsite_id": 4
            },
            {
            "campsite_photo_url": "https://testphoto.com/p3.jpg",
            "campsite_photo_id": 5,
            "campsite_id": 4
            }
        ]