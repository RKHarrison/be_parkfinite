from database import Base, SessionLocal, engine
from utils.seed_database import seed_database
import sys
import models

dev_data = models.Campsite(
            campsite_name="McCampface",
            campsite_longitude=-121.885,
            campsite_latitude=37.338
        )

seed_database(engine, SessionLocal, dev_data)
print("dev database seeded")








#CONDITIONAL SEEDING FOR MIGRATING TOM PRODUCTION DATABSE
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python seed.py [dev|test]")
#     else:
#         env = sys.argv[1]
#         if env == 'dev':
#             print("seeding " + env)
#             seed_database(engine, SessionLocal, dev_data)
#         # elif env == 'prod':
#         #     print("seeding " + env)
#         #     seed_database("postgresql://user:password@postgresserver/db")