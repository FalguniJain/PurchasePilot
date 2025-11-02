import os

<<<<<<< HEAD
# Reddit Configuration
CLIENT_ID = os.environ.get("REDDIT_APP_CLIENT_ID")
CLIENT_SECRET = os.environ.get("REDDIT_APP_CLIENT_SECRET")

# Environment Configuration
RECOMMENDER_ENV = os.getenv("RECOMMENDER_ENV", "development")
IS_DEVELOPMENT = RECOMMENDER_ENV == "development"

# URLs for Development
if IS_DEVELOPMENT:
    PROTOCOL = "http"
    BACKEND_HOST = "localhost:8000"  # Your actual backend port
    FRONTEND_HOST = "localhost:3001"  # Your React port
else:
    PROTOCOL = "https"
    BACKEND_HOST = os.getenv("NGINX_HOST", "your-production-domain.com")
    FRONTEND_HOST = BACKEND_HOST

# Reddit OAuth - Use Backend URL for callback (CORRECT PATH)
REDIRECT_URI = f"{PROTOCOL}://{BACKEND_HOST}/reddit/callback"

# Frontend redirect after auth
REDIRECT_URL = f"{PROTOCOL}://{FRONTEND_HOST}"

# CORS Origins
ORIGIN = [
    "http://localhost:3001", 
    "http://localhost:3000", 
    REDIRECT_URL,
    f"http://{BACKEND_HOST}",
    f"https://{BACKEND_HOST}"
]

# Other configurations
USER_AGENT = "web:product-review-app:v1.0 (by /u/tobiadefami)"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "randomsecretkey12345")
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:password@db/recommender_db"
)




=======
CLIENT_ID = os.environ.get("REDDIT_APP_CLIENT_ID")
CLIENT_SECRET = os.environ.get("REDDIT_APP_CLIENT_SECRET")
NGINX_HOST = os.getenv("NGINX_HOST")
RECOMMENDER_ENV = os.getenv("RECOMMENDER_ENV", "development")
PROTOCOL = "http" if RECOMMENDER_ENV == "development" else "https"
REDIRECT_URI = f"{PROTOCOL}://{NGINX_HOST}/api/reddit/callback"
USER_AGENT = "web:product-review-app:v1.0 (by /u/tobiadefami)"
REDIRECT_URL = f"{PROTOCOL}://{NGINX_HOST}"
ORIGIN = [REDIRECT_URL]
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:password@db/recommender_db"
)
>>>>>>> 482bf18602e4fe7feccde359a87ce6631b7aac5d
