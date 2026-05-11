import os

class Config(object):
    BOT_TOKEN = os.environ.get("8669372993:AAEl4wFWPefNAXTH2qmRFRVCOs_LkLbjvwI")
    API_ID = int(os.environ.get("35279304"))
    API_HASH = os.environ.get("49ea7646f4251b3ca5a7798c61bb5e9f")
    VIP_USER = os.environ.get('VIP_USERS', '6824252172').split(',')
    VIP_USERS = [int(user_id) for user_id in VIP_USER]
