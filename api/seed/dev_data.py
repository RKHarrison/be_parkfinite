from models.activity_models import Activity
from api.models.campsite_models import CampsiteCategory, Campsite, CampsitePhoto, CampsiteContact
from models.facility_models import Facility
from models.review_models import Review
from models.user_models import User
from datetime import datetime


def get_dev_data():

    return {
        'campsite_category': [
            CampsiteCategory(category_name="In The Wild",
                             category_img_url="https://example.com/category1.jpg"),
            CampsiteCategory(category_name="Car Park",
                             category_img_url="https://example.com/category2.jpg"),
            CampsiteCategory(category_name="Car Park - Daytime Only",
                             category_img_url="https://example.com/category3.jpg"),
            CampsiteCategory(category_name="Campsite",
                             category_img_url="https://example.com/category4.jpg"),
            CampsiteCategory(category_name="Free Motorhome Area",
                             category_img_url="https://example.com/category5.jpg")
        ],
        'facility': [
            Facility(facility_name="Wi-Fi",
                     facility_img_url="https://example.com/facility1.jpg"),
            Facility(facility_name="Shower",
                     facility_img_url="https://example.com/facility2.jpg"),
            Facility(facility_name="Laundry",
                     facility_img_url="https://example.com/facility3.jpg"),
            Facility(facility_name="Swimming Pool",
                     facility_img_url="https://example.com/facility4.jpg"),
            Facility(facility_name="Pet Friendly",
                     facility_img_url="https://example.com/facility5.jpg")
        ],
        'activity': [
            Activity(activity_name="Hiking",
                     activity_img_url="https://example.com/activity1.jpg"),
            Activity(activity_name="Fishing",
                     activity_img_url="https://example.com/activity2.jpg"),
            Activity(activity_name="Canoeing",
                     activity_img_url="https://example.com/activity3.jpg"),
            Activity(activity_name="Bird Watching",
                     activity_img_url="https://example.com/activity4.jpg"),
            Activity(activity_name="Cycling",
                     activity_img_url="https://example.com/activity5.jpg")
        ],
        'campsite': [
            Campsite(campsite_name="Tranquil Trails Campsite", category_id=1, campsite_longitude=-1.54322, campsite_latitude=53.45645, parking_cost=12, facilities_cost=25, description="Tranquil Trails Campsite offers a serene setting amidst lush greenery, ideal for a peaceful retreat.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Heather Heights Campsite", category_id=2, campsite_longitude=-1.87654, campsite_latitude=53.54321, parking_cost=14, facilities_cost=27, description="Nestled on gentle slopes, Heather Heights provides stunning views and vibrant sunsets.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Riverside Retreat Campsite", category_id=3, campsite_longitude=-1.81234, campsite_latitude=53.123456, parking_cost=13, facilities_cost=26, description="Riverside Retreat offers prime access to river adventures in a picturesque setting.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Summit Sanctuary Campsite", category_id=4, campsite_longitude=-1.90013, campsite_latitude=53.289111, parking_cost=15, facilities_cost=29, description="Summit Sanctuary sits atop the peaks, offering breathtaking views and crisp mountain air.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Meadowlands Escape Campsite", category_id=5, campsite_longitude=-1.2345, campsite_latitude=53.323, parking_cost=11, facilities_cost=23, description="Meadowlands Escape is perfect for nature lovers seeking a calm, floral setting.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Peak Paradise", category_id=1, campsite_longitude=-1.8374, campsite_latitude=53.259082, parking_cost=15.00, facilities_cost=25.00, description="A tranquil spot in the heart of the Peak District with beautiful mountain views.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Lake Escape", category_id=2, campsite_longitude=-1.8399, campsite_latitude=53.260082, parking_cost=10.00, facilities_cost=20.00, description="Perfect place next to the lake with plenty of fishing.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Valley View Haven", category_id=3, campsite_longitude=-1.84567, campsite_latitude=53.37201, parking_cost=16, facilities_cost=30, description="Valley View Haven offers panoramic valley views, perfect for those seeking tranquility and natural beauty.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Highland Hideaway", category_id=4, campsite_longitude=-1.89654, campsite_latitude=53.34029, parking_cost=14, facilities_cost=28, description="Highland Hideaway is nestled among highland hills, ideal for explorers and adventurers alike.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Blue Brook Camp", category_id=5, campsite_longitude=-1.93012, campsite_latitude=53.35834, parking_cost=13, facilities_cost=27, description="Blue Brook Camp lies next to a gentle stream, offering a peaceful setting for relaxation and reflection.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Eagle's Crest Campsite", category_id=1, campsite_longitude=-1.87045, campsite_latitude=53.26478, parking_cost=17, facilities_cost=33, description="Eagle's Crest Campsite provides a high elevation camping experience with spectacular mountain vistas.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Misty Meadows Campsite", category_id=2, campsite_longitude=-1.88855, campsite_latitude=53.27563, parking_cost=15, facilities_cost=25, description="Misty Meadows Campsite is surrounded by lush, fog-laden meadows offering a mystical camping experience.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Sunset Ridge Camp", category_id=1, campsite_longitude=-1.90721, campsite_latitude=53.36910, parking_cost=18, facilities_cost=32, description="Sunset Ridge Camp offers unforgettable sunset views from atop a quiet ridge, ideal for photographers and nature lovers.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Starlight Glade Campsite", category_id=2, campsite_longitude=-1.85102, campsite_latitude=53.35476, parking_cost=15, facilities_cost=24, description="Starlight Glade Campsite is tucked away in a secluded glade, perfect for stargazing and quiet nights by the fire.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Clearwater Cove Campsite", category_id=3, campsite_longitude=-1.93933, campsite_latitude=53.36588, parking_cost=16, facilities_cost=29, description="Clearwater Cove Campsite sits beside crystal clear waters, providing ample opportunities for swimming and canoeing.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Old Pine Retreat", category_id=4, campsite_longitude=-1.92378, campsite_latitude=53.37811, parking_cost=14, facilities_cost=27, description="Old Pine Retreat offers a break from the hustle with its ancient pine groves and quiet paths.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Golden Meadow Campsite", category_id=5, campsite_longitude=-1.89210, campsite_latitude=53.36179, parking_cost=13, facilities_cost=26, description="Golden Meadow Campsite features expansive meadows with golden hues, making it a joyful place for families and groups.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Craggy Peak Site", category_id=1, campsite_longitude=-1.88432, campsite_latitude=53.35100, parking_cost=17, facilities_cost=31, description="Craggy Peak Site offers adventurous souls a rugged landscape with spectacular cliffside views.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Forest Whisper Camp", category_id=2, campsite_longitude=-1.85544, campsite_latitude=53.34702, parking_cost=19, facilities_cost=35, description="Forest Whisper Camp is enveloped in a dense forest where the only sound is the rustling of leaves.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Bluebell Woodland Camp", category_id=3, campsite_longitude=-1.87760, campsite_latitude=53.36290, parking_cost=14, facilities_cost=28, description="Bluebell Woodland Camp is blanketed with bluebells in the spring, offering a magical camping experience.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Lakeside Serenity Camp", category_id=4, campsite_longitude=-1.86011, campsite_latitude=53.37333, parking_cost=16, facilities_cost=30, description="Lakeside Serenity Camp is nestled beside a tranquil lake, perfect for peaceful water activities.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Hilltop Haven Campsite", category_id=5, campsite_longitude=-1.84233, campsite_latitude=53.35922, parking_cost=15, facilities_cost=25, description="Hilltop Haven Campsite sits on a gentle hill, offering panoramic views of the valley below.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="River Bend Campsite", category_id=1, campsite_longitude=-1.90044, campsite_latitude=53.36825, parking_cost=18, facilities_cost=34, description="River Bend Campsite is a favorite for those who love fishing and riverside picnics.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Orchard Retreat Camp", category_id=2, campsite_longitude=-1.91977, campsite_latitude=53.37529, parking_cost=17, facilities_cost=32, description="Orchard Retreat Camp is surrounded by historic orchards, offering a sweet and fragrant atmosphere.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Grove Corner Campground", category_id=3, campsite_longitude=-1.86192, campsite_latitude=53.35548, parking_cost=15, facilities_cost=29, description="Grove Corner Campground is ideal for those who seek solitude in a grove of ancient trees.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Falcon Ridge Camp", category_id=4, campsite_longitude=-1.87911, campsite_latitude=53.34419, parking_cost=16, facilities_cost=27, description="Falcon Ridge Camp offers thrilling heights and the chance to see falcons in their natural habitat.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
            Campsite(campsite_name="Whispering Pines Campsite", category_id=5, campsite_longitude=-1.86520, campsite_latitude=53.35077, parking_cost=14, facilities_cost=26, description="Whispering Pines Campsite is where the pines murmur with the breeze, a place for rest and rejuvenation.", date_added=datetime.now().isoformat(), added_by="Admin", approved=True),
        ],
        'campsite_photo': [
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=1, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=2, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=3, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=3, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=3, campsite_photo_url="https://picsum.photos/200/300"),
            CampsitePhoto(campsite_id=4, campsite_photo_url="https://picsum.photos/200/300"),
        ],
        'campsite_contact': [
            CampsiteContact(campsite_contact_id=1, campsite_id=1, campsite_contact_name="John Doe", campsite_contact_phone="123-456-7890"),
            CampsiteContact(campsite_contact_id=2, campsite_id=2, campsite_contact_name="Jane Doe", campsite_contact_phone="987-654-3210"),
            CampsiteContact(campsite_contact_id=3, campsite_id=3, campsite_contact_name="Alice Smith", campsite_contact_phone="111-222-3333", campsite_contact_email="alice.smith@example.com"),
            CampsiteContact(campsite_contact_id=4, campsite_id=4, campsite_contact_name="Bob Johnson", campsite_contact_phone="444-555-6666", campsite_contact_email="bob.johnson@example.com"),
            CampsiteContact(campsite_contact_id=5, campsite_id=5, campsite_contact_name="Charlie Brown", campsite_contact_phone="777-888-9999", campsite_contact_email="charlie.brown@example.com"),
            CampsiteContact(campsite_contact_id=6, campsite_id=6, campsite_contact_name="Diana Prince", campsite_contact_phone="000-111-2222", campsite_contact_email="diana.prince@example.com"),
            CampsiteContact(campsite_contact_id=7, campsite_id=7, campsite_contact_name="Edward King", campsite_contact_phone="333-444-5555", campsite_contact_email="edward.king@example.com"),
            CampsiteContact(campsite_contact_id=8, campsite_id=8, campsite_contact_name="Fiona Queen", campsite_contact_phone="666-777-8888", campsite_contact_email="fiona.queen@example.com"),
            CampsiteContact(campsite_contact_id=9, campsite_id=9, campsite_contact_name="George Knight", campsite_contact_phone="999-000-1111", campsite_contact_email="george.knight@example.com"),
            CampsiteContact(campsite_contact_id=10, campsite_id=10, campsite_contact_name="Hannah White", campsite_contact_phone="222-333-4444", campsite_contact_email="hannah.white@example.com"),
            CampsiteContact(campsite_contact_id=11, campsite_id=11, campsite_contact_name="Ivy Green", campsite_contact_phone="555-666-7777", campsite_contact_email="ivy.green@example.com"),
            CampsiteContact(campsite_contact_id=12, campsite_id=12, campsite_contact_name="Jack Black", campsite_contact_phone="888-999-0000", campsite_contact_email="jack.black@example.com"),
            CampsiteContact(campsite_contact_id=13, campsite_id=13, campsite_contact_name="Karen Blue", campsite_contact_phone="123-321-4567", campsite_contact_email="karen.blue@example.com")
        ],
        'user': [
            User(username="NatureExplorer", user_password="secure123", user_firstname="Alice", user_lastname="Wanderlust", user_email="alice@example.com", xp=500, user_type="NORMAL", camera_permission=True),
            User(username="PeakHiker92", user_password="secure123", user_firstname="Bob", user_lastname="Hills", user_email="bob92@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="ForestFanatic", user_password="secure123", user_firstname="Clara", user_lastname="Greenwood", user_email="clara.fanatic@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="RiverRaider", user_password="secure123", user_firstname="Dan", user_lastname="Rivers", user_email="dan.raider@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="MeadowSinger", user_password="secure123", user_firstname="Eva", user_lastname="Song", user_email="eva.singer@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="CampfireStoryteller", user_password="secure123", user_firstname="Frank", user_lastname="Tales", user_email="frank.tales@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="TrailBlazer", user_password="secure123", user_firstname="Grace", user_lastname="Pathfinder", user_email="grace.blazer@example.com", xp=0, user_type="NORMAL", camera_permission=True),
            User(username="LakesideLounger", user_password="secure123", user_firstname="Harry", user_lastname="Waters", user_email="harry.lounger@example.com", xp=0, user_type="NORMAL", camera_permission=True)
        ],
        'review': [
            Review(rating=5, campsite_id=1, username="NatureExplorer", comment="Stunning location, completely serene. Can't wait to come back."),
            Review(rating=3, campsite_id=1, username="PeakHiker92", comment="Nice area, but quite busy during the weekend. Prefer weekdays for a quieter visit."),
            Review(rating=4, campsite_id=1, username="ForestFanatic", comment="Great escape into nature, though some trails are a bit overused."),
            Review(rating=2, campsite_id=1, username="RiverRaider", comment="Expected more secluded spots along the river, too exposed for my taste."),
            Review(rating=5, campsite_id=1, username="MeadowSinger", comment="The open spaces are fantastic for stargazing and relaxing."),
            
            Review(rating=4, campsite_id=2, username="CampfireStoryteller", comment="Campfire nights were amazing, but daytime activities lacked variety."),
            Review(rating=5, campsite_id=2, username="TrailBlazer", comment="As a hiker, this place is a dream. Trails for all levels are accessible."),
            Review(rating=3, campsite_id=2, username="LakesideLounger", comment="Views are good, but the lake access is not as easy as expected."),
            Review(rating=4, campsite_id=2, username="NatureExplorer", comment="Well maintained and managed, a reliable choice for a quick retreat."),
            Review(rating=2, campsite_id=2, username="PeakHiker92", comment="A bit too commercialized for my taste, misses the rustic charm."),
            
            Review(rating=5, campsite_id=3, username="ForestFanatic", comment="A forest haven. Quiet, peaceful, and beautifully green."),
            Review(rating=4, campsite_id=3, username="RiverRaider", comment="The river sounds at night are soothing. Good fishing spots nearby."),
            Review(rating=3, campsite_id=3, username="MeadowSinger", comment="Nice area but could use more facilities for families."),
            Review(rating=5, campsite_id=3, username="CampfireStoryteller", comment="The folklore and tales about this forest are mesmerizing."),
            Review(rating=4, campsite_id=3, username="TrailBlazer", comment="Good for both short hikes and longer treks. Lots of wildlife to see."),
            
            Review(rating=3, campsite_id=4, username="LakesideLounger", comment="Great views, but the water was too cold for swimming."),
            Review(rating=5, campsite_id=4, username="NatureExplorer", comment="I love the tranquility here, perfect for unwinding and disconnecting."),
            Review(rating=2, campsite_id=4, username="PeakHiker92", comment="The site is nice but the lack of proper signage made it hard to navigate."),
            Review(rating=4, campsite_id=4, username="ForestFanatic", comment="Perfect for those who want to get away from it all and enjoy the silence."),
            Review(rating=5, campsite_id=4, username="RiverRaider", comment="The proximity to the river makes this campsite a gem for water lovers."),
            
            Review(rating=4, campsite_id=5, username="MeadowSinger", comment="The meadows are vibrant with wildflowers and wildlife. Very photogenic."),
            Review(rating=5, campsite_id=5, username="CampfireStoryteller", comment="Every evening feels magical here with the campfire and clear skies."),
            Review(rating=3, campsite_id=5, username="TrailBlazer", comment="A decent place, but more amenities would make it even better."),
            Review(rating=4, campsite_id=5, username="LakesideLounger", comment="Laid back and relaxed atmosphere, great for a weekend of lounging."),
            Review(rating=5, campsite_id=5, username="NatureExplorer", comment="Returning next year for sure, this has become my favorite spot."),
        ]
    }
