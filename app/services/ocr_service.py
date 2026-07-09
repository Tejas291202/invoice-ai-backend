from pathlib import Path


class OCRService:

    async def extract_invoice(self, file_path: str):

        """
        Mock OCR extraction.

        Gemini Vision will replace this implementation
        in the next sprint.
        """

        filename = Path(file_path).name

        return {
            "supplier": "OM DISHA ENTERPRISES",
            "invoice_number": "P262700351",
            "invoice_date": "02 Apr 2026",
            "gst": "27AQOPB5164A1Z4",
            "amount": 1062.00,
            "currency": "INR",
            "filename": filename,
            "confidence": 0.99,
            "status": "review_pending"
        }