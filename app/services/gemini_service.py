import json

from google import genai

from app.config.settings import settings


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def extract_invoice(self, file_path: str):

        uploaded_file = self.client.files.upload(
            file=file_path
        )

        prompt = """
You are an expert Chartered Accountant.

Extract ONLY the following fields from the invoice.

Return ONLY valid JSON.

Do NOT explain anything.

Do NOT return markdown.

If a field is unavailable return "" for text fields and 0 for numeric fields.

Return EXACTLY this JSON:

{
    "date": "",
    "invoice_no": "",
    "name": "",
    "gstin_no": "",
    "taxable": 0,
    "cgst": 0,
    "sgst": 0,
    "invoice_value": 0
}

Rules:

1. DATE should be in DD/MM/YYYY format.

2. NAME means Supplier Name.

3. GSTIN NO. means Supplier GST Number.

4. TAXABLE means Taxable Amount before GST.

5. CGST should be ONLY CGST amount.

6. SGST should be ONLY SGST amount.

7. INVOICE VALUE means Final Invoice Total.

Return ONLY JSON.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                uploaded_file,
                prompt
            ]
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return json.loads(text)