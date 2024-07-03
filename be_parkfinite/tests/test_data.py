from datetime import datetime
from models import Campsite, CampsitePhoto, CampsiteContacts, CampsiteCategories

def get_test_data():

    test_campsite_photo_data = [CampsitePhoto(
        campsite_photo_id=1,
        campsite_id=1,
        campsite_photo_url="https://example.com/photo1.jpg"
    )]

    test_campsite_contact_data = [CampsiteContacts(
        campsite_contact_id=1,
        campsite_id=1,
        campsite_contact_name="John Doe",
        campsite_contact_phone="123-456-7890"
    )]

    test_campsite_data = [Campsite(
        campsite_id=1,
        campsite_name="McCampface",
        campsite_longitude=-121.885,
        campsite_latitude=37.338,
        parking_cost=10.1,
        facilities_cost=20.0,
        description="A beautiful campsite.",
        category_id=1,
        # photos=[test_campsite_photo],
        date_added=datetime.now().isoformat(),
        added_by="Admin"
    )]

    test_campsite_category_data = [CampsiteCategories(
        category_id=1,
        category_name="Mountain",
        category_image_url="https://example.com/category1.jpg"
    )]

    return {
        "campsite": test_campsite_data,
        "campsite_photo": test_campsite_photo_data,
        "campsite_contact": test_campsite_contact_data,
        "campsite_category": test_campsite_category_data
    }
