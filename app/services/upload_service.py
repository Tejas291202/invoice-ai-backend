
import tempfile
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.config import MAX_FILE_SIZE_MB


class UploadService:
    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png",
    }

    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
    CHUNK_SIZE = 1024 * 1024  # Read 1 MB at a time

    async def save_file(self, file: UploadFile):
        filename = file.filename or "invoice"
        extension = Path(filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"{extension or 'Unknown file type'} files are not supported."
            )

        upload_id = str(uuid4())
        temp_path = None
        total_size = 0

        try:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=extension,
            ) as temp_file:
                temp_path = temp_file.name

                while True:
                    chunk = await file.read(self.CHUNK_SIZE)

                    if not chunk:
                        break

                    total_size += len(chunk)

                    if total_size > self.MAX_FILE_SIZE_BYTES:
                        raise ValueError(
                            f"{filename} exceeds the "
                            f"{MAX_FILE_SIZE_MB} MB limit. "
                            "Please choose a smaller file."
                        )

                    temp_file.write(chunk)

            return {
                "upload_id": upload_id,
                "filename": filename,
                "temp_path": temp_path,
                "status": "uploaded",
            }

        except Exception:
            if temp_path:
                Path(temp_path).unlink(missing_ok=True)
            raise
