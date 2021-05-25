import common.database as db

def test_ulid():
    assert db.get_ulid()