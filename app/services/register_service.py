from app.repositories.register_repository import RegisterRepository
from app.repositories.invoice_repository import InvoiceRepository


class RegisterService:

    def __init__(self):
        self.repository = RegisterRepository()
        self.invoice_repository = InvoiceRepository()

    async def create_register(
        self,
        name: str,
    ):
        return self.repository.create(name)

    async def get_invoices(
        self,
        register_id: str,
    ):
        return self.invoice_repository.get_by_register(
            register_id
        )
    async def update_invoice(
        self,
        invoice_id: str,
        invoice: dict,
    ):
        return self.invoice_repository.update(
            invoice_id,
            invoice,
        )
    async def get_registers(self):

        return self.repository.get_all()