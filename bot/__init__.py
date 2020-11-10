import os
from datetime import datetime

from flask import Flask, abort, request

# https://pygsheets.readthedocs.io/en/stable/
import pygsheets

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


def create_app():

    app = Flask(__name__)

    google_sheet_gcp_key_path = os.path.join(
        os.path.dirname(__file__), "config/api-key.json"
    )
    gss_client = pygsheets.authorize(service_file=google_sheet_gcp_key_path)
    google_sheet = gss_client.open_by_url(os.environ.get("google_sheet_url")).sheet1

    line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
    handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

    @app.route("/", methods=["GET", "POST"])
    def callback():

        if request.method == "GET":
            return "66"
        if request.method == "POST":
            signature = request.headers["X-Line-Signature"]
            body = request.get_data(as_text=True)

            try:
                handler.handle(body, signature)
            except InvalidSignatureError:
                abort(400)

            return "OK"

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        user_msg = event.message.text
        if user_msg.find("9527") != -1:

            timesmap = datetime.now().strftime("%Y-%m-%d %H:%M")
            user_id = event.source.user_id
            user_name = line_bot_api.get_profile(user_id).as_json_dict()["displayName"]

            tag = "default"
            custom_reply_message = "沒事不要叫我"

            if user_msg.find("早") != -1:
                tag = "打卡"
                custom_reply_message = "收到～辛苦了"
            if user_msg.find("請假") != -1:
                tag = "請假"
                custom_reply_message = "加油好嗎"

            # Send To Google Sheet
            values = [timesmap, user_id, user_name, user_msg, tag]
            google_sheet.insert_rows(row=1, number=1, values=values)

            # Send To Line
            reply = TextSendMessage(text=f"{user_name} {custom_reply_message}")
            line_bot_api.reply_message(event.reply_token, reply)

    return app
