from tinydb import TinyDB
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils.database import DatabaseManeger

db = DatabaseManeger()
FIELD = "transaction_date"  # اسم فیلد تاریخ تو دیتابیس

now = datetime.now()
start = now - relativedelta(months=1)  # یک ماه دقیق تقویمی قبل

def parse_dt(s: str) -> datetime:
    # این فرمت: "YYYY-MM-DD HH:MM:SS.ffffff"
    # datetime.fromisoformat همین رو می‌فهمه ✅
    return datetime.fromisoformat(s)

def in_last_calendar_month(doc) -> bool:
    s = doc.get(FIELD)
    if not s:
        return False
    try:
        dt = parse_dt(s)
    except ValueError:
        return False  # اگر یه رکورد فرمتش خراب بود، ردش کن
    return start <= dt <= now

results = list(filter(in_last_calendar_month, db.get_all(db.transaction)))
results
