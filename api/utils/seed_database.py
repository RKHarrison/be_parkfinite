def seed_categories(session, categories):
    for category in categories:
        session.add(category)
    session.commit()

def seed_facilities(session, facilities):
    for facility in facilities:
        session.add(facility)
    session.commit()

def seed_activities(session, activities):
    for activity in activities:
        session.add(activity)
    session.commit()

def seed_campsites(session, campsites):
    for campsite in campsites:
        session.add(campsite)
    session.commit()

def seed_photos(session, photos):
    for photo in photos:
        session.add(photo)
    session.commit()

def seed_contacts(session, contacts):
    for contact in contacts:
        session.add(contact)
    session.commit()

def seed_users(session, users):
    for user in users:
        session.add(user)
    session.commit()

def seed_reviews(session, reviews):
    for review in reviews:
        session.add(review)
    session.commit()

def seed_database(session, data):
    if 'user' in data:
        seed_users(session, data['user'])
    if 'campsite_category' in data:
        seed_categories(session, data['campsite_category'])
    if 'facility' in data:
        seed_facilities(session, data['facility'])
    if 'activity' in data:
        seed_activities(session, data['activity'])
    if 'campsite' in data:
        seed_campsites(session, data['campsite'])
    if 'campsite_photo' in data:
        seed_photos(session, data['campsite_photo'])
    if 'campsite_contact' in data:
        seed_contacts(session, data['campsite_contact'])
    if 'review' in data:
        seed_reviews(session, data['review'])
