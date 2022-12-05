from flask import Request


class AuthRequest:
    id: str
    username: str
    password: str

    def __init__(self, schema: Request) -> None:
        self.id = schema.form['id']
        self.username = schema.form['username']
        self.password = schema.form['password']
