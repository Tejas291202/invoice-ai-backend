"""
Application configuration.

These values protect the free-tier AI usage.
When we move to a paid plan, only this file needs updating.
"""

# AI Provider
AI_PROVIDER = "gemini"

# Free Tier Mode
FREE_TIER = True

# Upload Restrictions
MAX_FILES_PER_UPLOAD = 3
MAX_FILE_SIZE_MB = 5

# AI Usage Protection
MAX_AI_CALLS_PER_DAY = 20

# Queue
REQUEST_DELAY_SECONDS = 2

# Features
ENABLE_IMAGE_COMPRESSION = True
ENABLE_DUPLICATE_DETECTION = False