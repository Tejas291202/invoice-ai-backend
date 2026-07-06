from pydantic import BaseModel


class RegisterSummary(BaseModel):

    id: str

    name: str

    invoiceCount: int

    ready: int

    attention: int

    failed: int

    total: float

    status: str