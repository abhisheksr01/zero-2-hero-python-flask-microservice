import os


class Config:
    PORT = int(os.getenv("PORT", 5001))
