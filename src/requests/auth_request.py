from uuid import uuid4

from bcrypt import gensalt, hashpw
from flask import Request


class AuthRequest:
    id: str
    username: str
    password: str
    status: bool

    def __init__(self, schema: Request) -> None:
        self.id = schema.form['id'] if schema.form['id'] else uuid4()
        self.username = schema.form['username']
        self.password = hashpw(
            schema.form['password'].encode('utf8'), gensalt()
        )
        self.status = False
