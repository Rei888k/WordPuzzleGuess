#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG, INFO, WARNING, ERROR, CRITICAL

import os

# ログ出力レベル
loglevel = DEBUG


class LogCollection:
    def __init__(self, name=__name__):
        self.logger = getLogger(name)
        self.logger.setLevel(loglevel)
        # ログ出力フォーマット
        formatter = Formatter(
            "%(asctime)s:%(levelname)s:%(process)d:%(name)s:%(message)s")

        # stdout
        # コンソール出力をやめたいときはここをコメントアウトする
        handler = StreamHandler()
        handler.setLevel(loglevel)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        # 相対パスでsrcと同じ階層にlogfileフォルダを作成する
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir('../../')
        if not os.path.exists(os.getcwd() + "/logfile"):
            os.mkdir(os.path.expanduser(os.getcwd() + "/logfile"))

        os.chdir('logfile')

        filename = os.getcwd() + '/logger.log'

        # output file
        handler = handlers.RotatingFileHandler(filename,
                                               #    maxBytes = 1048576,
                                               #    backupCount = 3)
                                               maxBytes=4194304,
                                               backupCount=10)

        handler.setLevel(loglevel)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, *args):
        # print()のように出力したいので少し整形する
        args2 = ""
        for arg in args:
            args2 = args2 + str(arg) + " "
        self.logger.debug("%s", args2)

    def info(self, *args):
        # print()のように出力したいので少し整形する
        args2 = ""
        for arg in args:
            args2 = args2 + str(arg) + " "
        self.logger.info("%s", args2)

    def warn(self, *args):
        # print()のように出力したいので少し整形する
        args2 = ""
        for arg in args:
            args2 = args2 + str(arg) + " "
        self.logger.warning("%s", args2)

    def error(self, *args):
        # print()のように出力したいので少し整形する
        args2 = ""
        for arg in args:
            args2 = args2 + str(arg) + " "
        self.logger.error("%s", args2)

    def critical(self, *args):
        # print()のように出力したいので少し整形する
        args2 = ""
        for arg in args:
            args2 = args2 + str(arg) + " "
        self.logger.critical("%s", args2)
