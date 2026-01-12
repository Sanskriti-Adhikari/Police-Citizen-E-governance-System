from database.db import officers_db, officer_id_counter
from models.officer import OfficerCreate, OfficerUpdate

def get_all_officers():
    return officers_db

def get_officer(officer_id: int):
    return next((o for o in officers_db if o["id"] == officer_id), None)

def create_officer(officer: OfficerCreate):
    global officer_id_counter
    new_officer = officer.dict()
    new_officer["id"] = officer_id_counter
    officers_db.append(new_officer)
    officer_id_counter += 1
    return new_officer

def update_officer(officer_id: int, officer_update: OfficerUpdate):
    officer = get_officer(officer_id)
    if not officer:
        return None
    update_data = officer_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        officer[key] = value
    return officer

def delete_officer(officer_id: int):
    global officers_db
    officers_db = [o for o in officers_db if o["id"] != officer_id]
