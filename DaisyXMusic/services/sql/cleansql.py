from sqlalchemy import BigInteger, Boolean, Column, String, UnicodeText

from DaisyXMusic.services.sql import BASE, SESSION



class Clean(BASE):
    __tablename__ = "clean"
    chat_id = Column(String(14), primary_key=True)
    should_clean = Column(Boolean, default=False)
    previous_ = Column(BigInteger)

    def __init__(
        self,
        chat_id,
        should_clean,
        previous_,
    ):
        self.chat_id = chat_id
        self.should_clean = should_clean
        self.previous_ = previous_



Clean.__table__.create(checkfirst=True)





def get_current_clean_settings(chat_id):
    try:
        return SESSION.query(Clean).filter(Clean.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def add_clean_setting(
    chat_id,
    should_clean,
    previous_,
):
    # adder = SESSION.query(Clean).get(chat_id)
    adder = Clean(
        chat_id,
        should_clean,
        previous_,
    )
    SESSION.add(adder)
    SESSION.commit()


def rm_clean_setting(chat_id):
    rem = SESSION.query(Clean).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def update_previous_msg(chat_id, previous_goodbye):
    row = SESSION.query(Clean).get(str(chat_id))
    row.previous_ = previous_
    # commit the changes to the DB
    SESSION.commit()
