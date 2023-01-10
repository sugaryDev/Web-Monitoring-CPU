from functools import cache
from sqlite3 import Connection, connect


@cache
def acquire_connection() -> Connection:
    return connect("test.db", check_same_thread=False)
