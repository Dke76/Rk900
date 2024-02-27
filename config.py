import os

API_ID = API_ID = 20346550

API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6949366970:AAFBenmXNLS4tYfWahFDxbBLMBH9klvD2uw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5665231556))

LOG = -1002102884801

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1183124209").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


