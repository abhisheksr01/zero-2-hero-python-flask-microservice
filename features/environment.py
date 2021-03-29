from greetings import app


def before_scenario(context, scenario):
    context.web_client = app.create().test_client()
