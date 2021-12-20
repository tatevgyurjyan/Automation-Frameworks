from testdata import test_data as data
import logging

logging.basicConfig(filename=data.log_file,
                    format="%(asctime)s: - %(levelname)s:%(message)s",
                    level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
