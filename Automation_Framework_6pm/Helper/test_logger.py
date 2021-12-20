from Testdata import test_data
import logging

logging.basicConfig(filename=test_data.log_file_name,
                    format="%(asctime)s: - %(levelname)s:%(message)s",
                    level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
