# -*- coding: utf-8 -*-

import re
import time
import datetime
import logging
import json
import pymongo
from multiprocessing.dummy import Pool as ThreadPool


class DataRead:
    def __init__(self, ip, port):
        self.id_to_qq_chat = {}
        self.ip = ip
        self.port = port

    def date_time_change(self, str_time):
        return time.mktime(time.strptime(str(str_time), '%Y-%m-%d %H:%M:%S'))

    # record 是一个字典
    def insert_data(self, record):
        _position = record["_id"].find('_')
        qq_num = record["_id"][:_position]
        self.id_to_qq_chat.setdefault(qq_num, {})
        self.id_to_qq_chat[qq_num].setdefault("PubTime", [])
        self.id_to_qq_chat[qq_num].setdefault("Mood_cont", [])
        self.id_to_qq_chat[qq_num].setdefault("chat", [])
        self.id_to_qq_chat[qq_num].setdefault("TimeStamps", [])
        self.id_to_qq_chat[qq_num].setdefault("score", [])

        self.id_to_qq_chat[qq_num]["PubTime"].append(record["PubTime"])
        self.id_to_qq_chat[qq_num]["TimeStamps"].append(self.date_time_change(record["PubTime"]))
        self.id_to_qq_chat[qq_num]["Mood_cont"].append(record["Mood_cont"])
        self.id_to_qq_chat[qq_num]["score"].append(0)
        if record.has_key('chat') is False:
            self.id_to_qq_chat[qq_num]["chat"].append('')
        else:
            self.id_to_qq_chat[qq_num]["chat"].append(record["chat"])


    def read_data_from_mongo(self):
        # 562953835该QQ号好友说说总数是56423
        self.mongo = pymongo.MongoClient(self.ip, int(self.port))
        self.db = self.mongo['QQ']  # 打开MongoDB的QQ数据库
        Mood_num = 0
        for record in self.db.Mood.find():
            self.insert_data(record)
            Mood_num += 1
        print Mood_num

    def save_data_to_mongo(self,data):
        self.mongo = pymongo.MongoClient(self.ip, int(self.port))
        self.db = self.mongo['QQ']  # 打开MongoDB的QQ数据库
        for item in data:
            self.db['person_mood_score'].insert(item)



if __name__ == "__main__":
    dataReadExample = DataRead("localhost", "27017")
    dataReadExample.read_data_from_mongo()
