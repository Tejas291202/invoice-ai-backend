from app.config.settings import settings

print("URL:", settings.SUPABASE_URL)
print("KEY STARTS WITH:", settings.SUPABASE_SERVICE_ROLE_KEY[:20])