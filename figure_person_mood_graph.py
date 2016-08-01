# -*- coding: utf-8 -*-

from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import pymongo
import json


def figure_person_mood_graph(qq_num, time_stamp_list, score_list):
    plt.plot(time_stamp_list, score_list)
    # plot(time_stamp_list,score_list,color="blue",linewidth=1.0,linestyle='-')
    plt.xlabel("time")
    plt.ylabel("score")
    plt.xlim(time_stamp_list[-1], time_stamp_list[0])
    plt.xticks(np.linspace(time_stamp_list[-1], time_stamp_list[0], 5, endpoint=True))
    plt.title("QQ " + qq_num + " chat Sentiment analysis graph")
    plt.savefig("picture/" + str(qq_num) + '.png', dpi=72)
    # plt.show()
    plt.close()

def obtain_socre_data():
    mongo = pymongo.MongoClient("localhost", 27017)
    db = mongo['QQ']  # 打开MongoDB的QQ数据库
    data = db.person_mood_score.find()
    picture_num = 0;
    for item in data:
        chat_num = len(json.loads(item['timestamps']))
        if chat_num < 50:
            continue
        picture_num += 1
        figure_person_mood_graph(item['qq_num'], json.loads(item['timestamps']),
                                 json.loads(item['score']))

    print picture_num

if __name__ == "__main__":
    obtain_socre_data()

