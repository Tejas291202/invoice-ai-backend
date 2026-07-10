from app.database.supabase import supabase


class InvoiceRepository:

    def create(
        self,
        register_id: str,
        invoice: dict,
    ):

        response = (
            supabase
            .table("invoices")
            .insert(
                {
                    "register_id": register_id,
                    "date": invoice["date"],
                    "invoice_no": invoice["invoice_no"],
                    "name": invoice["name"],
                    "gstin_no": invoice["gstin_no"],
                    "taxable": invoice["taxable"],
                    "cgst": invoice["cgst"],
                    "sgst": invoice["sgst"],
                    "invoice_value": invoice["invoice_value"],
                }
            )
            .execute()
        )

        print("===== SUPABASE INSERT =====")
        print(response.data)
        print("===========================")

        return response.data

    def get_by_register(
        self,
        register_id: str,
    ):

        response = (
            supabase
            .table("invoices")
            .select("*")
            .eq("register_id", register_id)
            .execute()
        )

        return response.data