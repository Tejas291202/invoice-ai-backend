from pydantic import BaseModel


class InvoiceUpdateRequest(BaseModel):
    date: str
    invoice_no: str
    name: str
    gstin_no: str
    taxable: float
    cgst: float
    sgst: float
    invoice_value: float