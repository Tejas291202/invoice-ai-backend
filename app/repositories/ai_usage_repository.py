from datetime import date

from app.database.supabase import supabase


class AIUsageRepository:

    def get_today(self):

        today = str(date.today())

        response = (
            supabase
            .table("ai_usage")
            .select("*")
            .eq("usage_date", today)
            .execute()
        )

        if response.data:

            return response.data[0]

        response = (
            supabase
            .table("ai_usage")
            .insert({
                "usage_date": today,
                "calls_used": 0,
            })
            .execute()
        )

        return response.data[0]

    def increment(self):

        today = self.get_today()

        (
            supabase
            .table("ai_usage")
            .update({
                "calls_used":
                today["calls_used"] + 1
            })
            .eq("id", today["id"])
            .execute()
        )