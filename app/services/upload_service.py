import tempfile
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


class UploadService:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png",
    }

    async def save_file(self, file: UploadFile):

        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"{extension} files are not supported."
            )

        upload_id = str(uuid4())

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        )

        contents = await file.read()

        temp_file.write(contents)
        temp_file.close()

        return {
            "upload_id": upload_id,
            "filename": file.filename,
            "temp_path": temp_file.name,
            "status": "uploaded"
        }