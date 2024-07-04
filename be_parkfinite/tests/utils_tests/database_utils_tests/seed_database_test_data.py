from datetime import datetime
from be_parkfinite.models.campsite_models import Campsite, CampsiteContact, CampsitePhoto, CampsiteCategory
from be_parkfinite.models.activity_models import Activity
from be_parkfinite.models.facility_models import Facility
from be_parkfinite.models.review_models import Review
from be_parkfinite.models.user_models import User

def get_empty_seed_test_data(): 
    return {
        'campsite': []
    }

def get_single_item_seed_test_data(): 
    return {
        'campsite': [
            Campsite(
                campsite_name="Sunset Vista",
                campsite_longitude=-117.123,
                campsite_latitude=32.715,
                parking_cost=15.00,
                facilities_cost=5.00,
                description="A lovely spot for sunset views",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            )
        ]
    }

def get_single_model_seed_test_data(): 
    return {
        'campsite': [
            Campsite(
                campsite_name="Blue Horizon",
                campsite_longitude=-197.123,
                campsite_latitude=39.715,
                parking_cost=15.00,
                facilities_cost=5.00,
                description="A lovely spot for sunset views",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            ),
                Campsite(
                campsite_name="Campy 2",
                campsite_longitude=-107.123,
                campsite_latitude=32.715,
                parking_cost=15.00,
                facilities_cost=5.00,
                description="A lovely spot for sunrise views",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            ),
                Campsite(
                campsite_name="Campy 3",
                campsite_longitude=-217.123,
                campsite_latitude=32.715,
                parking_cost=15.00,
                facilities_cost=5.00,
                description="A lovely spot for views",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            )
        ]
    }


def get_complex_seed_test_data():
    return {
        'campsite': [
            Campsite(
                campsite_name="Sunset Vista",
                campsite_longitude=-117.123,
                campsite_latitude=32.715,
                parking_cost=15.00,
                facilities_cost=5.00,
                description="A lovely spot for sunset views",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            ),
            Campsite(
                campsite_name="Mountain Retreat",
                campsite_longitude=-115.143,
                campsite_latitude=33.684,
                parking_cost=20.00,
                facilities_cost=10.00,
                description="Escape into the mountains",
                date_added=datetime.now().isoformat(),
                added_by="Test Seeder",
                category_id=1
            )
        ],
        'campsite_photo': [
            CampsitePhoto(
                campsite_photo_id=1,
                campsite_id=1,
                campsite_photo_url="https://example.com/photo1.jpg"
            ),
            CampsitePhoto(
                campsite_photo_id=2,
                campsite_id=2,
                campsite_photo_url="https://example.com/photo2.jpg"
            )
        ],
        'campsite_category': [
            CampsiteCategory(
                category_id=1,
                category_name="Mountain",
                category_image_url="https://example.com/category1.jpg"
            ),
            CampsiteCategory(
                category_id=2,
                category_name="Beach",
                category_image_url="https://example.com/category2.jpg"
            )
        ]
    }

def get_complete_seed_test_data():
    return {
        'campsite_category': [
            CampsiteCategory(category_name="In The Wild", category_image_url="https://example.com/category1.jpg"),
            CampsiteCategory(category_name="Car Park", category_image_url="https://example.com/category2.jpg"),
            CampsiteCategory(category_name="Campsite", category_image_url="https://example.com/category4.jpg")
        ],
        'facility': [
            Facility(facility_name="Wi-Fi", facility_img_url="https://example.com/facility1.jpg"),
            Facility(facility_name="Shower", facility_img_url="https://example.com/facility2.jpg"),
            Facility(facility_name="Pet Friendly", facility_img_url="https://example.com/facility5.jpg")
        ],
        'activity': [
            Activity(activity_name="Hiking", activity_img_url="https://example.com/activity1.jpg"),
            Activity(activity_name="Fishing", activity_img_url="https://example.com/activity2.jpg"),
            Activity(activity_name="Bird Watching", activity_img_url="https://example.com/activity4.jpg")
        ],
        'campsite': [
            Campsite(campsite_name="CAMPSITE A", category_id=1, campsite_longitude=-1.54322, campsite_latitude=53.45645, parking_cost=12, facilities_cost=25, description="CAMPSITE A offers a serene setting amidst lush greenery, ideal for a peaceful retreat.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="CAMPSITE B", category_id=2, campsite_longitude=-1.87654, campsite_latitude=53.54321, parking_cost=14, facilities_cost=27, description="CAMPSITE B provides stunning views and vibrant sunsets nestled on gentle slopes.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="CAMPSITE C", category_id=3, campsite_longitude=-1.81234, campsite_latitude=53.123456, parking_cost=13, facilities_cost=26, description="CAMPSITE C offers prime access to river adventures in a picturesque setting.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True)
        ],
        'campsite_photo': [
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://example.com/photo1.jpg"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://example.com/photo2.jpg"),
            CampsitePhoto(campsite_id=3, campsite_photo_url="https://example.com/photo3.jpg")
        ],
        'campsite_contact': [
            CampsiteContact(campsite_contact_id=1, campsite_id=1, campsite_contact_name="John Doe", campsite_contact_phone="123-456-7890"),
            CampsiteContact(campsite_contact_id=2, campsite_id=2, campsite_contact_name="Jane Doe", campsite_contact_phone="987-654-3210"),
            CampsiteContact(campsite_contact_id=3, campsite_id=3, campsite_contact_name="Jack Doe", campsite_contact_phone="321-654-9870")
        ],
        'review': [
            Review(rating=5, campsite_id=1, username="NatureExplorer", comment="Stunning location, completely serene. Can't wait to come back."),
            Review(rating=5, campsite_id=2, username="PeakHiker92", comment="As a hiker, this place is a dream. Trails for all levels are accessible."),
            Review(rating=5, campsite_id=3, username="ForestFanatic", comment="A forest haven. Quiet, peaceful, and beautifully green.")
        ],
        'user': [
            User(username="NatureExplorer", user_password="secure123", user_firstname="Alice", user_lastname="Wanderlust", user_email="alice@example.com", xp=500, user_type="NORMAL", camera_permission=True),
            User(username="PeakHiker92", user_password="secure123", user_firstname="Bob", user_lastname="Hills", user_email="bob92@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="ForestFanatic", user_password="secure123", user_firstname="Clara", user_lastname="Greenwood", user_email="clara.fanatic@example.com", xp=0, user_type="NORMAL", camera_permission=True)
        ]
    }
