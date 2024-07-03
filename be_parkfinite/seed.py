from database import SessionLocal, init_db, drop_db
from utils.database_utils import seed_database
from datetime import datetime
from models import Campsite

dev_data = {
    'campsite': [
        Campsite(
            campsite_name="Campy McCampsface",
            campsite_longitude=-117.123,
            campsite_latitude=32.715,
            parking_cost=15.00,
            facilities_cost=5.00,
            description="A lovely spot for sunset views",
            date_added=datetime.now().isoformat(),
            added_by="Us",
            category_id=1
        )
    ]
}


def run_seed():
    drop_db()
    init_db()
    session = SessionLocal()

    try:
        seed_database(session, dev_data)
    except Exception as e:
        session.rollback()
        print(f"Seeding failed: {e}")
    finally:
        session.close()
        print("database seeded")


if __name__ == "__main__":
    run_seed()
