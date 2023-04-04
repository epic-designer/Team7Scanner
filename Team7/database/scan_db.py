from sqlalchemy import Column, String
from . import BASE, SESSION


class GBan(BASE):
    __tablename__ = "team7_gban"
    user_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, user_id, reason):
        self.user_id = user_id
        self.reason = reason


GBan.__table__.create(checkfirst=True)

def check_scan(user_id):
    try:
        return SESSION.query(GBan).filter(GBan.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_scanuser(user_id):
    try:
        return SESSION.query(GBan).get(str(user_id))
    finally:
        SESSION.close()


def scan_user(user_id, reason):
    adder = GBan(str(user_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def revert_user(user_id):
    if rem := SESSION.query(GBan).get(str(user_id)):
        SESSION.delete(rem)
        SESSION.commit()


def get_all_scanned():
    rem = SESSION.query(GBan).all()
    SESSION.close()
    return rem


def scan_count():
    try:
        return SESSION.query(GBan).count()
    finally:
        SESSION.close()

