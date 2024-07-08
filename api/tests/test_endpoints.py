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

from os import environ
environ['ENV'] = 'development'

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

        posted_contact = posted_campsite['contacts'][0]
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
                {"campsite_contact_name": "Bobby B", "campsite_contact_phone": "0987654321",
                    "campsite_contact_email": "bobby@contact.com"},
                {"campsite_contact_name": "Cathy C", "campsite_contact_phone": "0987654321",
                    "campsite_contact_email": "cathy@contact.com"}
            ]
        }
        response = client.post("/campsites", json=request_body)
        assert response.status_code == 201

        posted_campsite = response.json()
        assert len(posted_campsite['contacts']) == 2
        assert posted_campsite['contacts'] == [
            {'campsite_contact_email': 'bobby@contact.com', 'campsite_contact_id': 4,
                'campsite_contact_name': 'Bobby B', 'campsite_contact_phone': '0987654321', 'campsite_id': 4},
            {'campsite_contact_email': 'cathy@contact.com', 'campsite_contact_id': 5,
                'campsite_contact_name': 'Cathy C', 'campsite_contact_phone': '0987654321', 'campsite_id': 4}
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
            # PHOTO URL SHOULD BE A STRING!!
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
            # CONTACT NUMBER SHOULD BE A STRING!!
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
            assert isinstance(campsite['average_rating'], float | None)

            for photo in campsite['photos']:
                assert isinstance(photo['campsite_photo_url'], str)
                assert isinstance(photo['campsite_photo_id'], int)
                assert isinstance(photo['campsite_id'], int)

            for detail in campsite['contacts']:
                assert isinstance(detail['campsite_contact_name'], str)
                assert isinstance(detail['campsite_contact_phone'], str)
                assert isinstance(
                    detail['campsite_contact_email'], (str, type(None)))
                assert isinstance(detail['campsite_contact_id'], int)
                assert isinstance(detail['campsite_id'], int)
        assert campsites[1]["average_rating"] != 0.0
        assert campsites[1]["average_rating"] == 2.0


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
class TestPostReviewByCampsiteId:
    def test_post_review(self, test_db):
        request_body = {
            "rating": 5,
            "campsite_id": 3,
            "username": "NatureExplorer",
            "comment": "Really great spot"
        }
        response = client.post("/campsites/1/reviews", json=request_body)
        print(response.json())
        assert response.status_code == 201

        posted_review = response.json()
        assert posted_review['review_id'] == 5
        assert posted_review['rating'] == 5
        assert posted_review['campsite_id'] == 1
        assert posted_review['username'] == 'NatureExplorer'
        assert posted_review['comment'] == 'Really great spot'

    def test_422_rating_outside_range_1_5(self):
        request_body = {
            "rating": 6,
            "username": "NatureExplorer",
            "comment": "Really great spot"
        }
        response = client.post("/campsites/3/reviews", json=request_body)
        assert response.status_code == 422
        assert "rating" in response.json()['detail'][0]['loc']

    def test_422_comment_outside_range_350_chars(self):
        request_body = {
            "rating": 5,
            "username": "NatureExplorer",
            "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget commodo orci. Integer varius nibh eu mattis porta. Duis tempus ex sed leo dapibus, sit amet facilisis est tincidunt. Aenean auctor, mauris nec laoreet convallis, urna ex egestas ante, id viverra eros libero at ipsum. Sed finibus libero quam, vel sollicitudin odio volutpat nec. Suspendisse potenti.+1"
        }
        response = client.post("/campsites/3/reviews", json=request_body)
        assert response.status_code == 422
        error = response.json()
        print(error)
        assert "comment" in error['detail'][0]['loc']
        assert error['detail'][0]['msg'] == 'String should have at most 350 characters'

    def test_422_field_missing_from_request_body(self, test_db):
        request_body = {
            "username": "NatureExplorer",
            "comment": "Really great spot"

        }
        response = client.post(f"/campsites/3/reviews", json=request_body)
        assert response.status_code == 422
        error = response.json()
        assert "rating" in error['detail'][0]['loc']

    def test_422_non_existent_username(self, test_db):
        request_body = {
            "rating": 5,
            "username": "NONEXISTENT",
            "comment": "Really great spot"
        }
        response = client.post(f"/campsites/3/reviews", json=request_body)
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == "404 - User Not Found!"

    def test_404_campsite_not_found(self, test_db):
        request_body = {
            "rating": 5,
            "username": "NatureExplorer",
            "comment": "Really great spot"
        }
        response = client.post("/campsites/999999/reviews", json=request_body)
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == "404 - Campsite Not Found!"


@pytest.mark.main
class TestGetReviewsByCampsiteId:
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
class TestPatchReviewsByCampsiteId:
    def test_patch_review_by_campsite_id(self, test_db):
        request_body = {
            "username": "ForestFanatic",
            "rating": 1,
            "comment": "Actually I changed my mind, its awful!"
        }
        response = client.patch("/campsites/2/reviews/4", json=request_body)
        assert response.status_code == 200
        review = response.json()
        assert review['rating'] == 1
        assert review['comment'] == "Actually I changed my mind, its awful!"

    def test_patch_review_missing_optional_fields(self, test_db):
        request_body = {
            "username": "ForestFanatic",
            "comment": ""
        }
        response = client.patch("/campsites/2/reviews/4", json=request_body)
        assert response.status_code == 200
        review = response.json()
        assert review['rating'] == 2
        assert review['comment'] == "Its ok I guess"

    def test_422_rating_outside_range_1_5(self):
        request_body = {
            "username": "ForestFanatic",
            "rating": 0,
        }
        response = client.patch("/campsites/2/reviews/4", json=request_body)
        assert response.status_code == 422
        assert "rating" in response.json()['detail'][0]['loc']

    def test_422_comment_outside_range_350_chars(self):
        request_body = {
            "username": "ForestFanatic",
            "comment": "Lorem ipsumor piscing elit. ABCDJSDPellentesque eget commodo orci. Integer varius nibh eu mattis porta. Duis tempus ex sed leo dapibus, sit amet facilisis est tincidunt. Aenean auctor, mauris nec laoreet convallis, urna ex egestas ante, id viverra eros libero at ipsum. Sed finibus libero quam, vel sollicitudin odio volutpat nec. Suspendisse potenti.+1"
        }
        response = client.patch("/campsites/2/reviews/4", json=request_body)
        assert response.status_code == 422
        error = response.json()
        assert "comment" in error['detail'][0]['loc']
        assert error['detail'][0]['msg'] == 'String should have at most 350 characters'

    def test_422_field_missing_from_request_body(self, test_db):
        request_body = {
            # NO USERNAME
        }
        response = client.patch("/campsites/2/reviews/4", json=request_body)
        assert response.status_code == 422
        error = response.json()
        assert "username" in error['detail'][0]['loc']

    def test_404_review_not_found(self, test_db):
        request_body = {
            "username": "ForestFanatic"
        }
        response = client.patch(
            "/campsites/2/reviews/987654321", json=request_body)
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == "404 - Review Not Found!"

    def test_404_review_not_found(self, test_db):
        request_body = {
            "username": "ForestFanatic"
        }
        response = client.patch(
            "/campsites/987654321/reviews/4", json=request_body)
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == "404 - Campsite Not Found!"


@pytest.mark.main
class TestGetUsers:
    def test_read_users(self, test_db):
        response = client.get("/users")
        assert response.status_code == 200
        users = response.json()
        assert len(users) == 3


@pytest.mark.main
class TestGetUserByUsername:
    def test_read_user_by_username(self, test_db):
        response = client.get('/users/NatureExplorer')
        assert response.status_code == 200
        user = response.json()
        assert user["username"] == "NatureExplorer"

    def test_404_non_existing_username(self, test_db):
        response = client.get('/users/NONEXISTING')
        assert response.status_code == 404
        error = response.json()
        assert error["detail"] == "404 - User Not Found!"


@pytest.mark.main
class TestUpdateUserXP:
    def test_patch_user_xp(self, test_db):
        response1 = client.patch('/users/NatureExplorer/25')
        update1 = response1.json()
        assert response1.status_code == 200

        response2 = client.patch('/users/NatureExplorer/100')
        update2 = response2.json()
        assert response2.status_code == 200

        response3 = client.patch('/users/NatureExplorer/-325')
        update3 = response3.json()
        assert response3.status_code == 200

        assert update1['xp'] == 525
        assert update2['xp'] == 625
        assert update3['xp'] == 300

    def test_400_invalid_patch_request(self, test_db):
        response = client.patch('/users/NatureExplorer/INVALID')
        error = response.json()
        assert response.status_code == 400
        assert error['detail'] == "400 - Invalid XP Value"

    def test_404_non_existing_user(self, test_db):
        response = client.patch('/users/INVALID/50')
        error = response.json()
        assert response.status_code == 404
        assert error['detail'] == "404 - User Not Found!"


@pytest.mark.main
class TestPostUserFavouriteCampsite:
    def test_create_user_favourite_campsite(self, test_db):
        response = client.post("/users/PeakHiker92/favourites/2")
        assert response.status_code == 201

    def test_409_user_favourite_campsite_already_exists(self, test_db):
        response = client.post("/users/NatureExplorer/favourites/1")
        assert response.status_code == 409

    def test_404_user_not_found(self, test_db):
        response = client.post("/users/NONEXISTENT/favourites/1")
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == '404 - User Not Found!'

    def test_404_campsite_not_found(self, test_db):
        response = client.post("/users/PeakHiker92/favourites/987654321")
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == '404 - Campsite Not Found!'


@pytest.mark.main
class TestGetUserCampsiteFavourites:
    def test_read_favourites(self, test_db):
        response = client.get('/users/NatureExplorer/favourites')
        assert response.status_code == 200
        favourites = response.json()
        assert len(favourites) == 2
        assert favourites[0]['campsite_name'] == 'CAMPSITE A'
        assert favourites[1]['campsite_name'] == 'CAMPSITE C'

    def test_user_with_no_favourited_campsites(self, test_db):
        response = client.get('/users/ForestFanatic/favourites')
        assert response.status_code == 200
        favourites = response.json()
        assert len(favourites) == 0
        assert favourites == []

    def test_404_invalid_user(self, test_db):
        response = client.get('/users/INVALID/favourites')
        assert response.status_code == 404
        error = response.json()

        assert error['detail'] == "404 - User Not Found!"


@pytest.mark.main
class TestDeleteUserFavouriteCampsite:
    def test_delete_user_favourite_campsite(self, test_db):
        response = client.delete("/users/NatureExplorer/favourites/3")
        assert response.status_code == 204

    def test_404_user_not_found(self, test_db):
        response = client.delete("/users/NONEXISTENT/favourites/1")
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == '404 - User Not Found!'

    def test_404_campsite_not_found(self, test_db):
        response = client.delete("/users/PeakHiker92/favourites/987654321")
        assert response.status_code == 404
        error = response.json()
        assert error['detail'] == '404 - Campsite Not Found!'


@pytest.mark.db_utils
class TestUpdateCampsiteAverageRatingUtility:
    def test_updates_average_rating(self, test_db):
        request_body_1 = {
            "rating": 1,
            "campsite_id": 3,
            "username": "NatureExplorer",
            "comment": "Really great spot"
        }
        request_body_2 = {
            "rating": 5,
            "campsite_id": 3,
            "username": "NatureExplorer",
            "comment": "Really great spot"
        }

        response = client.post("/campsites/1/reviews", json=request_body_1)
        campsite_after_first_review = client.get("campsites/1").json()
        response = client.post("/campsites/1/reviews", json=request_body_2)
        campsite_after_second_review = client.get("campsites/1").json()

        assert response.status_code == 201
        assert campsite_after_first_review['average_rating'] != campsite_after_second_review["average_rating"]
