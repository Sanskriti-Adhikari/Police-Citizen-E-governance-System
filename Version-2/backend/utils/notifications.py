from database.db import notifications_db, notification_id_counter
from datetime import datetime

def create_notification(case_id: int, message: str, notification_type: str):
    global notification_id_counter
    notification = {
        "id": notification_id_counter,
        "case_id": case_id,
        "citizen_id": None,
        "message": message,
        "notification_type": notification_type,
        "created_at": datetime.now().isoformat(),
        "read": False
    }
    notifications_db.append(notification)
    notification_id_counter += 1
    return notification
