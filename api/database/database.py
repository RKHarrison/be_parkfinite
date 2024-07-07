from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base
from config.config import DATABASE_URL


Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    print("connected to: ", DATABASE_URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def drop_db():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            connection.execute(text("DROP TABLE IF EXISTS campsites_facilities CASCADE;"))
            connection.execute(text("DROP TABLE IF EXISTS facilities CASCADE;"))
            connection.execute(text("DROP TABLE IF EXISTS campsites CASCADE;"))
            trans.commit()
        except Exception as e:
            trans.rollback()
            print("Error occurred:", e)
            raise e
        finally:
            print("Dropped all tables with CASCADE")

    print("Dropped database: ", DATABASE_URL)
