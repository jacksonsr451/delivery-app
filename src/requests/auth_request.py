from uuid import uuid4

from bcrypt import gensalt, hashpw
from flask import Request


class AuthRequest:
    id: str
    username: str
    password: str
    status: bool

    def __init__(self, schema: Request) -> None:
        self.id = uuid4().__str__()
        self.username = schema.form['username']
        self.password = hashpw(
            schema.form['password'].encode('utf8'), gensalt()
        ).decode('utf8')
        self.status = False
