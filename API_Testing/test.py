import logging
import formatting_input_data
from post_user import Post
from validator import UserSchema
import config

#Configure logging, arces log file from config file
log = config.request_data["log"]
logging.basicConfig(filename=log,
                    format='%(asctime)s: - %(levelname)s:%(message)s', 
                    level=logging.DEBUG)


# Getting data to be posted
posted_data = formatting_input_data.formatting()

# Getting post response
posted_user = Post()
response_data = posted_user.post_user()

# Validating response data
valid = UserSchema()
valid.validate(response_data)

# Checking whether data are equal or not
response_data.pop("id")
assert posted_data == response_data, "DATA ARE NOT EQUAL"
logging.info("DATA ARE EQUAL")
