from database.database import SessionLocal, init_db, drop_db
from utils.database_utils import seed_database
from seed.dev_data import get_dev_data

dev_data = get_dev_data()

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
