import os

from app.services.gemini_service import GeminiService
from app.services.usage_service import UsageService

usage = UsageService()

class OCRService:

    def __init__(self):

        self.gemini = GeminiService()

    async def extract_invoice(self, file_path: str):

        try:

            invoice = await self.gemini.extract_invoice(
                file_path
            )

            return invoice

        finally:

            if os.path.exists(file_path):
                os.remove(file_path)