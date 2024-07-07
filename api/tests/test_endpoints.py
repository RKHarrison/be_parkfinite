from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

import pytest
from fastapi.testclient import TestClient

from database.database import Base
from api.main import app, get_db
from api.data.test_data import get_test_data
from api.utils.seed_database import seed_database
from api.utils.test_utils import is_valid_date

import os
os.environ['ENV'] = 'development'

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
        assert response.json() == {"Server": "Healthy and happy!"}


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
            assert isinstance(campsite['contacts'], list)

            for photo in campsite['photos']:
                assert isinstance(photo['campsite_photo_url'], str)
                assert isinstance(photo['campsite_photo_id'], int)
                assert isinstance(photo['campsite_id'], int)

            for detail in campsite['contacts']:
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
        assert posted_campsite['contacts'] == []
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

    def test_campsite_with_contact(self, test_db):
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
            "closing_month": "May",
            "contacts": [{"campsite_contact_name": "Bobby B", "campsite_contact_phone": "0987654321", "campsite_contact_email": "bobby@contact.com"}]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201

        posted_campsite = response.json()
        assert len(posted_campsite['contacts']) == 1

        posted_contact=posted_campsite['contacts'][0]
        assert posted_contact["campsite_id"] == 4
        assert posted_contact["campsite_contact_id"] == 4
        assert posted_contact["campsite_contact_name"] == "Bobby B"
        assert posted_contact["campsite_contact_phone"] == "0987654321"
        assert posted_contact["campsite_contact_email"] == "bobby@contact.com"

    def test_campsite_multiple_contacts(self, test_db):
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
            "closing_month": "May",
            "contacts": [
                {"campsite_contact_name": "Bobby B", "campsite_contact_phone": "0987654321", "campsite_contact_email": "bobby@contact.com"},
                {"campsite_contact_name": "Cathy C", "campsite_contact_phone": "0987654321", "campsite_contact_email": "cathy@contact.com"}
                ]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201

        posted_campsite = response.json()
        assert len(posted_campsite['contacts']) == 2
        assert posted_campsite['contacts'] ==  [
        {'campsite_contact_email': 'bobby@contact.com','campsite_contact_id': 4,'campsite_contact_name': 'Bobby B','campsite_contact_phone': '0987654321','campsite_id': 4},
        {'campsite_contact_email': 'cathy@contact.com','campsite_contact_id': 5,'campsite_contact_name': 'Cathy C','campsite_contact_phone': '0987654321','campsite_id': 4}
        ]

    def test_404_category_not_found(self, test_db):
        request_body = {
            "category_id": 987654321,
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "photos": []
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        error = response.json()
        assert error['detail'] == "Category ID does not exist!"

    def test_422_field_missing_from_request_body(self, test_db):
        request_body = {
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3,
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "campsite_name" in response.json()['detail'][0]['loc']

    def test_422_invalid_data_in_basic_campsite_request_body(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": "INVALID",
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "campsite_longitude" in response.json()['detail'][0]['loc']
    
    def test_422_invalid_PHOTO_info(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3,
            #PHOTO URL SHOULD BE A STRING!!
            "photos": [{"campsite_photo_url": 00000000}]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "campsite_photo_url" in response.json()['detail'][0]['loc']

    def test_invalid_PHOTOS_data_structure(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3,
            "photos": "SHOULD BE A LIST"
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "photos" in response.json()['detail'][0]['loc']

    def test_422_invalid_CONTACT_info(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3,
            #CONTACT NUMBER SHOULD BE A STRING!!
            "contacts": [{"campsite_contact_name": "Bobby B", "campsite_contact_phone": 000000000000}]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "campsite_contact_phone" in response.json()['detail'][0]['loc']

    def test_invalid_CONTACTS_data_structure(self, test_db):
        request_body = {
            "campsite_name": "TEST NAME",
            "campsite_longitude": 1.23,
            "campsite_latitude": 4.56,
            "added_by": "PeakHiker92",
            "category_id": 3,
            "contacts": "SHOULD BE A LIST"
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 422
        assert "contacts" in response.json()['detail'][0]['loc']
