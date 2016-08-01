# -*- coding: utf-8 -*-

from data_read import *
from SentiAnalysis import *
from person_relationship import *
import json


class PersonSentiAnalysis:
    def __init__(self):
        self.data_read_example = DataRead("localhost", "27017")
        self.comment_senti_cal_example = commentSentiCalc()
        self.personRelationship = PersonRelationship()

    def cal_person_senti_score(self):
        self.data_read_example.read_data_from_mongo()
        for qq_num in self.data_read_example.id_to_qq_chat:
            for item in enumerate(self.data_read_example.id_to_qq_chat[qq_num]['Mood_cont']):
                score = self.comment_senti_cal_example.groupSentiCalc(item[1])
                self.data_read_example.id_to_qq_chat[qq_num]['score'][item[0]] = score

    def save_person_mood_score_to_mongodb(self):
        data = []
        for qq_num in self.data_read_example.id_to_qq_chat:
            tmp_dict = {}
            score_list_str = json.dumps(self.data_read_example.id_to_qq_chat[qq_num]['score'], encoding='utf-8')
            timestamps_list_str = json.dumps(self.data_read_example.id_to_qq_chat[qq_num]['TimeStamps'],
                                             encoding='utf-8')
            tmp_dict['score'] = score_list_str
            tmp_dict['timestamps'] = timestamps_list_str
            tmp_dict['qq_num'] = qq_num
            data.append(tmp_dict)
        self.data_read_example.save_data_to_mongo(data)

    def cal_person_relationship(self):
        self.data_read_example.read_data_from_mongo()
        for qq_num in self.data_read_example.id_to_qq_chat:
            for item in self.data_read_example.id_to_qq_chat[qq_num]['chat']:
                if item != '':
                    chat_list = json.loads(item)
                    for dialog in chat_list:
                        self.personRelationship.insert_data(dialog['user_1'], dialog['user_2'])

    def save_person_relationship_to_mongodb(self):
        mongo = pymongo.MongoClient("localhost", 27017)
        db = mongo['QQ']  # 打开MongoDB的QQ数据库

        people_relationship_list = {}

        for key in self.personRelationship.person_relationship:
            people_relationship_list.setdefault(str(key[0]), [])
            people_relationship_list[str(key[0])].append((self.personRelationship.person_relationship[key],str(key[1])))

        for key in people_relationship_list:
            friend_list_str = json.dumps(people_relationship_list[key])
            dic = {}
            dic['qq_num'] = key
            dic['friend_list'] = friend_list_str
            db.person_relationship.insert(dic)

if __name__ == "__main__":
    person_senti_analysis_example = PersonSentiAnalysis()
    # person_senti_analysis_example.cal_person_senti_score()
    # person_senti_analysis_example.save_person_mood_score_to_mongodb()

    # print person_senti_analysis_example.comment_senti_cal_example.invalid_chat
    # print person_senti_analysis_example.data_read_example.id_to_qq_chat['562963835']['score']

    # 计算qq 号之间的关系

    person_senti_analysis_example.cal_person_relationship()
    person_senti_analysis_example.save_person_relationship_to_mongodb()


