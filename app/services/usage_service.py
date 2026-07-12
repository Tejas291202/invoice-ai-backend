from app.config import MAX_AI_CALLS_PER_DAY

from app.repositories.ai_usage_repository import (
    AIUsageRepository,
)


class UsageService:

    def __init__(self):

        self.repository = AIUsageRepository()

    def can_call_ai(self):

        today = self.repository.get_today()

        return (
            today["calls_used"]
            < MAX_AI_CALLS_PER_DAY
        )

    def increment(self):

        self.repository.increment()

    def remaining(self):

        today = self.repository.get_today()

        return (
            MAX_AI_CALLS_PER_DAY
            - today["calls_used"]
        )