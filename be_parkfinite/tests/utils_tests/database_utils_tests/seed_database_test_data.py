from datetime import datetime
from models import Campsite, CampsitePhoto, CampsiteCategories

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
            CampsiteCategories(
                category_id=1,
                category_name="Mountain",
                category_image_url="https://example.com/category1.jpg"
            ),
            CampsiteCategories(
                category_id=2,
                category_name="Beach",
                category_image_url="https://example.com/category2.jpg"
            )
        ]
    }