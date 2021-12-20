import re
import logging


def formatting():

    try:
        with open("/home/tatevik/Desktop/QA_Automation/Tatevik_Gyurjyan/input_data.txt") as file:
            pattern = file.readlines()

        for lines in pattern:
            if re.findall(r"#", lines):
                pass
        else:
            if re.findall(r"#", lines):
                value1, value2 = re.split(r"#", lines)
                my_list = re.split(r":|\t", value1)

            my_dict = {}
            my_dict["userId"] = my_list[0]
            my_dict["title"] = my_list[1]
            my_dict["body"] = my_list[2]
            return my_dict

    except Exception as e:
        logging.exception(e)
