from app.schemas.register import RegisterSummary


class RegisterService:

    @staticmethod
    def current_register():

        return RegisterSummary(

            id="reg_001",

            name="Purchase Register - July 2026",

            invoiceCount=8,

            ready=6,

            attention=2,

            failed=0,

            total=248000,

            status="ACTIVE"

        )