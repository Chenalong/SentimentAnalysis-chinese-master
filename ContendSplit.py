# -*- coding: utf-8 -*-
import json
import codecs
import urllib2
import jieba

# 把contend 类容分词以json格式返回
def xunfei_contend_split(contend):
    url_get_base = "http://api.ltp-cloud.com/analysis/?"
    api_key = 'Z6a3L161atTsfa5bBbWr9JIvTAYsAsoyvo9JUqyi'
    text = contend
    format = 'json'
    pattern = 'ws'
    result = urllib2.urlopen(
        "%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base, api_key, text, format, pattern))
    content = result.read().strip()
    print content


# 返回一个 list 该类型如下所示：[[(id,contend),()....]]
def jieba_contend_split(contend):
    punctuation = [u'，', u'/', u'！', u'？', u'。', u' ', u'\'']
    wordSequenceList = []  # 类型说明 [[(id,comtend),()....]] 每一个元素都是一个长短语，其中没有短语
    seg_list = jieba.cut(self.commentSentence)
    segmentedComment = [item for item in seg_list]
    segmentedCommentTuple = list(enumerate(segmentedComment))
    subWordSequenceList = []
    for wordTuple in segmentedCommentTuple:
        if wordTuple[1] in punctuation:
            if subWordSequenceList:
                wordSequenceList.append(subWordSequenceList)
                subWordSequenceList = []
        else:
            subWordSequenceList.append(wordTuple)
    if subWordSequenceList:
        wordSequenceList.append(subWordSequenceList)
    return wordSequenceList


if __name__ == "__main__":
    ss = "评语:哎，一年了，怎么我还是这个挫样--------->转载内容:内脏有多干净！！脸蛋就有多漂亮。 外面长什么， 里面就有什么病！1. 额头长痘 原因：压力大，脾气差，造成心火和血液循环有问题 改善：早睡早起，多喝水2.双眉间长痘： 原因：胸闷，心律不整，心悸 改善：不要做太过激烈的运动，避免烟、酒、辛辣食品3.鼻头长痘： 原因：胃火过盛，消化系统异常 改善：少吃冰冷食物"
    contend_split(ss)