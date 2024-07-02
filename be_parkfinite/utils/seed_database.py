from database import Base

def seed_database(engine, session, data):
    db = session()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        for item in data.values():
            db.add(item)
        db.commit()
    finally:
        db.close()
