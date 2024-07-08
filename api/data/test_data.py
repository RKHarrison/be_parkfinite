from datetime import datetime
from api.models.campsite_models import Campsite, CampsitePhoto, CampsiteContact, CampsiteCategory
from api.models.activity_models import Activity
from api.models.facility_models import Facility
from api.models.review_models import Review
from api.models.user_models import User

def get_test_data():
    return {
        'campsite_category': [
            CampsiteCategory(category_name="In The Wild", category_img_url="https://example.com/category1.jpg"),
            CampsiteCategory(category_name="Car Park", category_img_url="https://example.com/category2.jpg"),
            CampsiteCategory(category_name="Campsite", category_img_url="https://example.com/category4.jpg")
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
            Campsite(campsite_name="CAMPSITE A", category_id=1, campsite_longitude=-1.54322, campsite_latitude=53.45645, parking_cost=None, facilities_cost=None, description="CAMPSITE A offers a serene setting amidst lush greenery, ideal for a peaceful retreat.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True, opening_month="March", closing_month="November"),
            Campsite(campsite_name="CAMPSITE B", category_id=2, campsite_longitude=-1.87654, campsite_latitude=53.54321, parking_cost=14, facilities_cost=27, description="CAMPSITE B provides stunning views and vibrant sunsets nestled on gentle slopes.", date_added=datetime.now().isoformat(), added_by="Admin", approved=False, opening_month=None, closing_month=None),
            Campsite(campsite_name="CAMPSITE C", category_id=3, campsite_longitude=-1.81234, campsite_latitude=53.123456, parking_cost=13, facilities_cost=26, description="CAMPSITE C offers prime access to river adventures in a picturesque setting.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True)
        ],
        'campsite_photo': [
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://example.com/photo1.jpg"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://example.com/photo2.jpg")
        ],
        'campsite_contact': [
            CampsiteContact(campsite_contact_id=1, campsite_id=1, campsite_contact_name="John Doe", campsite_contact_phone="123-456-7890"),
            CampsiteContact(campsite_contact_id=3, campsite_id=3, campsite_contact_name="Jack Doe", campsite_contact_phone="321-654-9870", campsite_contact_email="abc@xyz.com")
        ],
        'review': [
            Review(rating=5, campsite_id=1, username="NatureExplorer", comment="Stunning location, completely serene. Can't wait to come back."),
            Review(rating=5, campsite_id=1, username="PeakHiker92", comment="As a hiker, this place is a dream. Trails for all levels are accessible."),
            Review(rating=5, campsite_id=1, username="ForestFanatic"),
            Review(rating=2, campsite_id=2, username="ForestFanatic")
        ],
        'user': [
            User(username="NatureExplorer", user_password="secure123", user_firstname="Alice", user_lastname="Wanderlust", user_email="alice@example.com", xp=500, user_type="NORMAL", camera_permission=True),
            User(username="PeakHiker92", user_password="secure123", user_firstname="Bob", user_lastname="Hills", user_email="bob92@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="ForestFanatic", user_password="secure123", user_firstname="Clara", user_lastname="Greenwood", user_email="clara.fanatic@example.com")
        ],
        'user_campsite_favourites': [
            ("NatureExplorer", [1, 3])
            ]
    }