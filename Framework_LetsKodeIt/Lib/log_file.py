import logging

logging.basicConfig(filename="test_log.txt",
                    format="%(asctime)s: - %(levelname)s:%(message)s",
                    level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
