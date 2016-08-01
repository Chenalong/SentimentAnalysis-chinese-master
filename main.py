# -*- coding: utf-8 -*-

from person_senti_analysis import *
from figure_person_mood_graph import *
from best_friend_analysis import *


if __name__ == '__main__':
    # 构造个人情感分析类
    person_senti_analysis_example = PersonSentiAnalysis()

    # 从mongodb中读取说说，根据评分分析每个人的情感波动，并把数据存储到mongodb中
    person_senti_analysis_example.cal_person_senti_score()
    person_senti_analysis_example.save_person_mood_score_to_mongodb()

    # 根据个人情感数据画图  存储在SentimentAnalysis-chinese-master\figure里面
    obtain_socre_data_and_figure()

    # 计算朋友之间的关系，并把数据存储到mongodb数据库中
    person_senti_analysis_example.cal_person_relationship()
    person_senti_analysis_example.save_person_relationship_to_mongodb()

    # 构造好友分析类，并统计某个好友的朋友关系图，画条形图展示
    best_friend_analysis = BestFriendAnalysis()
    best_friend_analysis.figure_best_friend_bar('562963835')