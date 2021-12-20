import requests
import config
import logging
import json
import formatting_input_data


class Post():

    def post_user(self):
        try:
            api_url = config.request_data["url"]
            logging.info(f"Connected to {api_url}")

            get_data = formatting_input_data.formatting()
            response = requests.post(api_url, json=get_data)

            status_code = response.status_code
            assert int(status_code) in range(200, 299), "Code Mismatch"
            logging.info("Success POST!")

        except Exception as e:
            logging.exception(e)

        finally:
            json_response = json.loads(response.text)
            return json_response
