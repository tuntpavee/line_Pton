from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi,
    PushMessageRequest, TextMessage
)

CHANNEL_ACCESS_TOKEN = "0pQ6/CJtGagSJVZYaGWmLdlEF49N2YAQ1LrK+07aMSpxYHUqXgY+HFSn8vkfDFjEPYRsSTFTyJWRv7wupYnzz1h/LC/sfErvUVa3XvSVoAC3WTzkN4FtNJuKYSci1Zz98O56/1N5Lf07xVFKHt75EwdB04t89/1O/w1cDnyilFU="

USER_ID = "U679eda5fb3d53820b21ba96981abf704"

config = Configuration(access_token=CHANNEL_ACCESS_TOKEN)

with ApiClient(config) as api_client:
    messaging_api = MessagingApi(api_client)
    messaging_api.push_message(
        PushMessageRequest(
            to=USER_ID,
            messages=[TextMessage(text="Hello")]
        )
    )

print("Message sent!")

