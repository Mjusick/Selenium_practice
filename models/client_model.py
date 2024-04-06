import dataclasses


@dataclasses.dataclass
class Client:
    first_name: str
    last_name: str
    email: str
    password: str
