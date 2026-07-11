from fastapi import APIRouter
from app.models.invoice import InvoiceUpdateRequest
from app.models.register import RegisterRequest
from app.services.register_service import RegisterService

router = APIRouter()

service = RegisterService()


@router.post("/")
async def create_register(
    request: RegisterRequest,
):

    return await service.create_register(
        request.name
    )

@router.get("/{register_id}/invoices")
async def get_register_invoices(
    register_id: str,
):

    return await service.get_invoices(
        register_id
    )
@router.put("/invoice/{invoice_id}")
async def update_invoice(
    invoice_id: str,
    request: InvoiceUpdateRequest,
):

    return await service.update_invoice(
        invoice_id,
        request.model_dump(),
    )