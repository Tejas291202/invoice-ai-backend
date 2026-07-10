from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.upload_service import UploadService
from app.services.ocr_service import OCRService
from app.repositories.invoice_repository import InvoiceRepository

router = APIRouter()

upload_service = UploadService()
ocr_service = OCRService()
invoice_repository = InvoiceRepository()


@router.post("/")
async def upload_invoices(
    register_id: str,
    files: list[UploadFile] = File(...)
):
    """
    Upload one or more invoice files,
    process them through OCR,
    and return structured invoice data.
    """

    uploaded_files = []

    for file in files:

        try:

            upload_result = await upload_service.save_file(file)

            invoice_data = await ocr_service.extract_invoice(
                upload_result["temp_path"]
            )
            invoice_repository.create(
                 register_id,
                 invoice_data,
            )

            uploaded_files.append(
                {
                    "upload": {
                        "upload_id": upload_result["upload_id"],
                        "filename": upload_result["filename"],
                        "status": upload_result["status"],
                    },
                    "invoice": invoice_data,
                }
            )

        except ValueError as e:

            raise HTTPException(
                status_code=400,
                detail=str(e)
            )

    return {
        "uploaded": uploaded_files,
        "count": len(uploaded_files),
        "status": "success",
    }