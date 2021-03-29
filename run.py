from greetings import app
from greetings.settings import Config

if __name__ == "__main__":
    app.create().run(host="0.0.0.0", port=Config.PORT)
