
import threading
from . import SESSION, BASE
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)
from sqlalchemy.sql.sqltypes import BigInteger

class Report_Users(BASE):
    __tablename__ = "report_user" #new
    report_user_id = Column(BigInteger, primary_key=True)
    user_id = Column(UnicodeText)
    def __init__(self, report_user_id, user_id):
        self.report_user_id = report_user_id
        self.user_id = user_id

    def __repr__(self):
        return "<{} reported by {}>".format(self.report_user_id, self.user_id)

Report_Users.__table__.create(checkfirst=True)

ILOCK = threading.RLock()


def report_user(report_user_id, user_id):
    fuk = SESSION.query(Report_Users).get(report_user_id)
    if not fuk:
        hm = Report_Users(report_user_id, user_id)
        SESSION.add(hm)
        SESSION.commit()

def rm_report(user_id):
    with ILOCK:
        fuk = SESSION.query(Report_Users).get(user_id)
        if fuk:
            SESSION.delete(fuk)
            SESSION.commit()
        else:
            SESSION.close()

def check_report(user_id):
    try:
        return SESSION.query(Report_Users).filter(Report_Users.report_user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

def get_all_reports():
    try:
        return SESSION.query(Report_Users).all()
    finally:
        SESSION.close()

def report_count():
    try:
        return SESSION.query(Report_Users).count()
    finally:
        SESSION.close()
