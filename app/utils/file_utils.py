import os
import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads")


def ensure_upload_folder():
    UPLOAD_DIR.mkdir(exist_ok=True)


def generate_upload_id():
    return str(uuid.uuid4())


def get_file_extension(filename: str):
    return os.path.splitext(filename)[1].lower()