def seed_database(db, data):
        for table_model in data.values():
            for row in table_model:
                db.add(row)
        db.commit()
