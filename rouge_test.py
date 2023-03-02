# -*- coding:utf-8 -*-
#from rouge_chinese import Rouge
import jieba # you can use any other word cutting library
from rouge import Rouge 

hypothesis = "台湾灯会今晚开幕"
hypothesis = ' '.join(jieba.cut(hypothesis)) 

reference = "台湾灯会今晚正式展开，晚间在国父纪念馆举行开灯仪式"
reference = ' '.join(jieba.cut(reference)) 

rouger = Rouge()
scores = rouger.get_scores(hypothesis, reference)
print(hypothesis)
print(reference)

print(scores)