from fastapi import APIRouter

from app.services.register_service import RegisterService

router = APIRouter()


@router.get("/current")
def get_current_register():

    return RegisterService.current_register()