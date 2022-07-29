from dataclasses import dataclass, field
from typing import Optional

import marshmallow.validate


@dataclass
class PayerData:
    FirstName: str
    LastName: str
    MiddleName: str
    Birth: str
    Street: str
    Address: str
    City: str
    Country: str
    Phone: str
    Postcode: str


@dataclass
class Charge:
    Amount: float = field(metadata={"validate": marshmallow.validate.Range(min=0.01)})
    IpAddress: str
    CardCryptogramPacket: str
    PublicId: Optional[str]
    Currency: Optional[str]
    Name: Optional[str]
    PaymentUrl: Optional[str]
    InvoiceId: Optional[str]
    Description: Optional[str]
    AccountId: Optional[str]
    Email: Optional[str]
    JsonData: Optional[dict]
    Payer: Optional[PayerData]
    Token: Optional[str]
