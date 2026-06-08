from dataclasses import dataclass

@dataclass
class ClientRequest:
    product: str
    category: str
    moq: int
    country: str


@dataclass
class Supplier:
    supplier: str
    category: str
    moq: int
    country: str


@dataclass
class Meeting:
    brand: str
    supplier: str
    date: str
    status: str