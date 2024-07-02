from database import Base

def seed_database(engine, session, data):
    db = session()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        db.add(data)
        db.commit()
    finally:
        db.close()
