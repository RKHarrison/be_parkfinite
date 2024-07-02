from be_parkfinite.models import Campsite, CampsitePhoto

def seed_db(session):
    initial_campsite = Campsite(
        campsite_name="Campsite A",
        campsite_longitude=-120.123,
        campsite_latitude=36.123
    )
    session.add(initial_campsite)
    session.commit()

    initial_photo = CampsitePhoto(
        campsite_photo_url="http://example.com/photo1.jpg",
        campsite_id=initial_campsite.campsite_id
    )
    session.add(initial_photo)
    session.commit()