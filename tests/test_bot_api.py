import json
import unittest
from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from bot import create_app


class SettingBase(TestCase):
    def create_app(self):
        return create_app()

    def set_signature(self):
        return {"X-Line-Signature": "00000000000000000000"}

    def set_message(self, message_text):
        return json.dumps(
            {
                "events": [
                    {
                        "replyToken": "ffffffffffffffffffffffffffffffff",
                        "type": "message",
                        "source": {
                            "userId": "Uab4b4b9cb8be2488507bd67f95715dd9",
                            "type": "user",
                        },
                        "message": {
                            "type": "text",
                            "id": "12345678912345",
                            "text": message_text,
                        },
                    }
                ],
            }
        )


class Check_bot_api(SettingBase):
    def test_get_bot_api(self):
        response = self.client.get(url_for("callback"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"66")

    def test_post_bot_api_400(self):
        response = self.client.post(
            url_for("callback"),
            headers=self.set_signature(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    @patch("pygsheets.Worksheet.insert_rows")
    @patch("pygsheets.authorization.authorize")
    @patch("linebot.api.LineBotApi.reply_message")
    @patch("linebot.webhook.SignatureValidator.validate")
    def test_post_bot_api(
        self,
        mock_linebot_validate,
        mock_linebot_reply,
        mock_pygsheets_authorize,
        mock_pygsheets_insert_row,
    ):
        mock_linebot_validate.return_value = True

        self.client.post(
            url_for("callback"),
            headers=self.set_signature(),
            data=self.set_message("9527 早"),
            content_type="application/json",
        )

        self.client.post(
            url_for("callback"),
            headers=self.set_signature(),
            data=self.set_message("9527 請假"),
            content_type="application/json",
        )

        self.assertEqual(mock_linebot_reply.call_count, 2)
        self.assertEqual(mock_linebot_validate.call_count, 2)
        self.assertEqual(mock_pygsheets_insert_row.call_count, 2)


if __name__ == "__main__":
    unittest.main()
