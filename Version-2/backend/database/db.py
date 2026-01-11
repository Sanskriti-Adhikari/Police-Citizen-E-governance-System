from typing import List, Dict

# In-memory DB
criminal_records_db: List[Dict] = []
officers_db: List[Dict] = []
notifications_db: List[Dict] = []
holiday_requests_db: List[Dict] = []

# ID Counters
record_id_counter = 1
officer_id_counter = 1
notification_id_counter = 1
holiday_id_counter = 1
