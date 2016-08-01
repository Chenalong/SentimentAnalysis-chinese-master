# coding=utf-8
import json
from pylab import *
import numpy as np
import pymongo

class BestFriendAnalysis:
    def __init__(self):
        pass

    def figure_best_friend_bar(self, qq_num):
        mongo = pymongo.MongoClient("localhost", 27017)
        db = mongo['QQ']  # 打开MongoDB的QQ数据库

        data = db.person_relationship.find({'qq_num': qq_num})
        best_friend_list = {}

        max_score = 0
        for item in data:
            friend_list = json.loads(item['friend_list'])
            for tup in friend_list:
                best_friend_list.setdefault(tup[0], [])
                best_friend_list[tup[0]].append(tup[1])
                max_score = max(max_score, tup[0])
        print max_score
        X = np.arange(max_score + 1)

        Y = np.zeros(max_score + 1)

        for key in best_friend_list:
            Y[key] = len(best_friend_list[key])
        print Y

        bar(X, Y, facecolor='#9999ff', edgecolor='white')

        xlabel("intimacy")
        ylabel("friend_num")
        title(str(best_friend_list[max_score]))
        for x, y in zip(X, Y):
            text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        show()

if __name__ == "__main__":
    best_friend_analysis = BestFriendAnalysis()
    best_friend_analysis.figure_best_friend_bar('562963835')


