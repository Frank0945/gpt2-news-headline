# -*- coding:utf-8 -*-
#from rouge_chinese import Rouge
import jieba # you can use any other word cutting library
from rouge import Rouge 

hypothesis = "世界幸福報告出爐芬蘭連7年拔得頭籌"
hypothesis = ' '.join(jieba.cut(hypothesis)) 

reference = "芬蘭連7年列世界最幸福國家阿富汗墊底"
reference = ' '.join(jieba.cut(reference)) 

rouger = Rouge()
scores = rouger.get_scores(hypothesis, reference)
print(hypothesis)
print(reference)

print(scores)