import pandas as pd
# libraries for  logging
from datetime import datetime
import inspect
import logging



def pd_get_file(path, sheetname="Sheet1"):
    data = pd.read_excel(path, sheetname, header=0, index_col=0)
    return data


def pd_getRowCount(data):
    return len(data)


def pd_getColumnCount(data):
    return len(data.columns)


def pd_readData(data, test_case_name, column):
    ind_of_row = data[data['Test case Name'] == str(test_case_name)].index.values[0]
    print("ind_of_row", ind_of_row)
    return data.at[ind_of_row, column]


def pd_writeData(data, test_case_name, column, value):
    # print("testcase_name",test_case_name)
    # print(data['Test case Name'] == str(test_case_name))
    # print(data[data['Test case Name'] == str(test_case_name)].index.values[0])
    ind_of_row = data[data['Test case Name'] == str(test_case_name)].index.values[0]
    # print("ind_of_row", ind_of_row)
    data.at[ind_of_row, column] = value


def pd_save_excel(data, file):
    data.to_excel(file)


def pd_read_test_data(data):
    data


def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    fileHandler = logging.FileHandler(str(current_time) + 'logfile.log')
    # fileHandler = logging.FileHandler(str(conftest.env_name)+"_"+str(conftest.test_start_time)+"_"+'logfile.log')
    # fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger


"""
file = "C:/Users/ustad.shafiyodin/PycharmProjects/pytest-pr/TestData/format for automation.xlsx"
    pd_xlutils = pdXLUtils(file, "Sheet1")

    print(pd_xlutils.pd_getRowCount(), pd_xlutils.pd_getColumnCount())
    pd_xlutils.pd_writeData("test_login_invalid_username", "Status", "pass")
    print(pd_xlutils.data["Status"])

"""
