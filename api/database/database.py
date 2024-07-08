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
    with engine.connect() as connection:
        trans = connection.begin()
        try:
            if 'postgresql' in DATABASE_URL:
                connection.execute(
                    text("DROP TABLE IF EXISTS user_campsite_favourites CASCADE;"))
                connection.execute(
                    text("DROP TABLE IF EXISTS campsites_facilities CASCADE;"))
                connection.execute(
                    text("DROP TABLE IF EXISTS facilities CASCADE;"))
                connection.execute(
                    text("DROP TABLE IF EXISTS campsites CASCADE;"))
                connection.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
            else:
                Base.metadata.drop_all(bind=engine)
            trans.commit()
        except Exception as e:
            trans.rollback()
            raise Exception(f"Error occurred during table drop: {e}")
        finally:
            db_action = "with CASCADE for PostgreSQL" if 'postgresql' in DATABASE_URL else "using SQLAlchemy's drop_all method"
            print(f"Dropped all tables {db_action}")

    print("Dropped database: ", DATABASE_URL)
