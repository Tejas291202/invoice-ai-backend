from app.database.supabase import supabase


class RegisterRepository:

    def create(self, name: str):

        response = (
            supabase
            .table("registers")
            .insert({
                "name": name
            })
            .execute()
        )

        return response.data[0]