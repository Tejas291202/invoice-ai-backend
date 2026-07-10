from app.database.supabase import supabase

response = (
    supabase
    .table("registers")
    .select("*")
    .limit(1)
    .execute()
)

print(response.data)