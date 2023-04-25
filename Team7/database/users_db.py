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


class Owners(BASE):
    __tablename__ = "owners"
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<Owner {}>".format(self.user_id)

class Devs(BASE):
    __tablename__ = "devs"
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<Dev {}>".format(self.user_id)


class Users(BASE):
    __tablename__ = "tsudo"
    user_id = Column(BigInteger, primary_key=True)
    username = Column(UnicodeText)

    def __init__(self, user_id, username=None):
        self.user_id = user_id
        self.username = username

    def __repr__(self):
        return "<User: {}, bot: {}>".format(self.user_id, self.username)


class Bots(BASE):
    __tablename__ = "bots"
    user_id = Column(BigInteger, primary_key=True)
    username = Column(UnicodeText)

    def __init__(self, user_id, username=None):
        self.user_id = user_id
        self.username = username

    def __repr__(self):
        return "<Bot {} ({})>".format(self.username, self.user_id)


Owners.__table__.create(checkfirst=True)
Devs.__table__.create(checkfirst=True)
Users.__table__.create(checkfirst=True)
Bots.__table__.create(checkfirst=True)

ILOCK = threading.RLock()

def add_owner(user_id):
    fuk = SESSION.query(Owners).get(user_id)
    if not fuk:
        user = Owners(user_id)
        SESSION.add(user)
        SESSION.commit()

def add_dev(user_id):
    fuk = SESSION.query(Devs).get(user_id)
    if not fuk:
        user = Devs(user_id)
        SESSION.add(user)
        SESSION.commit()

def add_sudo(user_id, bot_username):
    fuk = SESSION.query(Users).get(user_id)
    if not fuk:
        user = Users(user_id, bot_username)
        SESSION.add(user)
        SESSION.commit()

def add_bot(user_id, username):
    fuk = SESSION.query(Bots).get(user_id)
    if not fuk:
        bot = Bots(user_id, username)
        SESSION.add(bot)
        SESSION.commit()


def get_all_owners():
    try:
        return SESSION.query(Owners).all()
    finally:
        SESSION.close()


def get_all_devs():
    try:
        return SESSION.query(Devs).all()
    finally:
        SESSION.close()


def get_all_sudos():
    try:
        return SESSION.query(Users).all()
    finally:
        SESSION.close()


def get_all_bots():
    try:
        return SESSION.query(Bots).all()
    finally:
        SESSION.close()


def rm_dev(user_id):
    with ILOCK:
        user = SESSION.query(Devs).get(user_id)
        if user:
            SESSION.delete(user)
            SESSION.commit()
        else:
            SESSION.close()

def rm_sudo(user_id):
    with ILOCK:
        user = SESSION.query(Users).get(user_id)
        if user:
            SESSION.delete(user)
            SESSION.commit()
        else:
            SESSION.close()

def rm_bot(user_id):
    with ILOCK:
        bot = SESSION.query(Bots).get(user_id)
        if bot:
            SESSION.delete(bot)
            SESSION.commit()
        else:
            SESSION.close()


def check_owner(user_id):
    try:
        return SESSION.query(Owners).filter(Owners.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

def check_dev(user_id):
    try:
        return SESSION.query(Devs).filter(Devs.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

def check_sudo(user_id):
    try:
        return SESSION.query(Users).filter(Users.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

def check_bot(user_id):
    try:
        return SESSION.query(Bots).filter(Bots.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


# Extraa

def dev_count():
    try:
        return SESSION.query(Devs).count()
    finally:
        SESSION.close()

def sudo_count():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()

def bot_count():
    try:
        return SESSION.query(Bots).count()
    finally:
        SESSION.close()
