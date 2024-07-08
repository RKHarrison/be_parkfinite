from sqlalchemy.sql import func


def update_campsite_average_rating(db, campsite_id, campsite_sql_model, review_sql_model):
    campsite = db.query(campsite_sql_model).filter(
        campsite_sql_model.campsite_id == campsite_id).first()
    new_avg_rating = db.query(func.avg(review_sql_model.rating)).filter(
        review_sql_model.campsite_id == campsite_id).scalar()
    campsite.average_rating = new_avg_rating
    db.commit()
    db.refresh(campsite)
