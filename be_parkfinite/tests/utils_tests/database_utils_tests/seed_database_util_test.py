import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from be_parkfinite.models.campsite_models import Base, Campsite, CampsitePhoto, CampsiteCategory, CampsiteContact
from be_parkfinite.models.activity_models import Activity
from be_parkfinite.models.facility_models import Facility
from be_parkfinite.models.review_models import Review
from be_parkfinite.models.user_models import User
from be_parkfinite.utils.database_utils import seed_database
from be_parkfinite.tests.utils_tests.database_utils_tests.seed_database_test_data import get_empty_seed_test_data, get_single_item_seed_test_data, get_single_model_seed_test_data, get_complex_seed_test_data, get_complete_seed_test_data


@pytest.fixture(scope="function")
def util_test_session():
    util_test_engine = create_engine('sqlite:///', echo=True)
    Base.metadata.create_all(bind=util_test_engine)
    Session = sessionmaker(bind=util_test_engine)
    util_test_session = Session()
    yield util_test_session
    util_test_session.close()
    Base.metadata.drop_all(util_test_engine)


def test_seed_database_with_empty_data(util_test_session):
    # Arrange
    empty_data = get_empty_seed_test_data()
    # Act
    seed_database(util_test_session, empty_data)
    # Assert
    all_items = util_test_session.query(Campsite).all()
    assert len(all_items) == 0


def test_seed_database_with_single_item(util_test_session):
    # Arrange
    single_item_data = get_single_item_seed_test_data()
    # Act
    seed_database(util_test_session, single_item_data)
    # Assert
    all_items = util_test_session.query(Campsite).all()
    assert len(all_items) == 1

    seeded_campsite = all_items[0]
    assert seeded_campsite.campsite_id == 1
    assert seeded_campsite.campsite_name == "Sunset Vista"
    assert seeded_campsite.campsite_longitude == -117.123
    assert seeded_campsite.campsite_latitude == 32.715
    assert seeded_campsite.description == "A lovely spot for sunset views"


def test_seed_database_with_multiple_items_single_model(util_test_session):
    # Arrange
    single_model_data = get_single_model_seed_test_data()
    # Act
    seed_database(util_test_session, single_model_data)
    # Assert
    all_items = util_test_session.query(Campsite).all()
    assert len(all_items) == 3

    seeded_campsite_1 = all_items[0]
    assert seeded_campsite_1.campsite_id == 1
    assert seeded_campsite_1.campsite_name == "Blue Horizon"

    seeded_campsite_3 = all_items[2]
    assert seeded_campsite_3.campsite_id == 3
    assert seeded_campsite_3.campsite_name == "Campy 3"


def test_seed_database_with_complex_data(util_test_session):
    # Arrange
    complex_data = get_complex_seed_test_data()
    # Act
    seed_database(util_test_session, complex_data)
    # Assert Campsites
    all_campsites = util_test_session.query(Campsite).all()
    assert len(all_campsites) == 2
    # Assert CampsitePhoto
    all_photos = util_test_session.query(CampsitePhoto).all()
    assert len(all_photos) == 2
    # Assert CampsiteCategories
    all_categories = util_test_session.query(CampsiteCategory).all()
    assert len(all_categories) == 2

def test_seed_database_with_complete_data(util_test_session):
        # Arrange
    complex_data = get_complete_seed_test_data()
    # Act
    seed_database(util_test_session, complex_data)
    # Assert Campsites
    all_campsites = util_test_session.query(Campsite).all()
    assert len(all_campsites) == 3
    # Assert CampsitePhoto
    all_photos = util_test_session.query(CampsitePhoto).all()
    assert len(all_photos) == 3
    # Assert CampsiteCategories
    all_categories = util_test_session.query(CampsiteCategory).all()
    assert len(all_categories) == 3
    all_contacts = util_test_session.query(CampsiteContact).all()
    assert len(all_contacts) == 3
    all_activities = util_test_session.query(Activity).all()
    assert len(all_activities) == 3
    all_facilities = util_test_session.query(Facility).all()
    assert len(all_facilities) == 3
    all_reviews = util_test_session.query(Review).all()
    assert len(all_reviews) == 3
    all_users = util_test_session.query(User).all()
    assert len(all_users) == 3