import os

# import self as self


class Qase:
    # В файл config/qase.py внутрь класса QASE надо добавить строку
    # self.CASE_PARAMS = ['layer', 'status', 'behavior', 'severity', 'priority']

    TOKEN = os.getenv('QASE_TOKEN') if os.getenv('QASE_TOKEN') is not None else False
    IS_DOC_UPDATE_NEEDED = True if os.getenv('QASE_DOC') == 'True' else False

    API_DOMAIN = 'https://api.qase.io'
    FRONTEND_DOMAIN = 'https://app.qase.io'
    API_VERSION = 'v1'
    PROJECT = 'GS'