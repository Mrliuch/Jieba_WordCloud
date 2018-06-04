#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 16:32
# @Author  : 刘晨
# @File    : test.py
# @Software: PyCharm Community Edition
import jieba
import jieba.analyse
import time
import re
import os
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import matplotlib.pyplot as plt
lis = ["南音","可爱的小蘑菇"]
#############################
reg = "\d\d\d\d-\d\d-\d\d"
reg1 = '\d\d:\d\d:\d\d'
reg2 = '(\[[\u4e00-\u9fa5][\u4e00-\u9fa5]\])'
reg3 = '-?[1-9]\d*'
reg4 = '[a-zA-z]+://[^\s]*'
def wenjian():#读取文件
    with open("0.txt", "r", encoding='utf-8') as f:
        txt = f.read()
    return txt
######利用字符串函数replace进行字符串替换 参数i为替换的字符串########
def tihuan(i):
    f = open('0.txt', 'r', encoding='utf-8')
    txt = f.read()
    txt1 = txt.replace("\n", "").strip()
    # txt7 = txt.replace(" ", "").strip()
    txt4 = txt1.replace(i, "")
    with open('0.txt','w',encoding = 'utf-8') as f:
        f.write(txt4)
    f.close()
# #####利用正则表达式去掉正则匹配内容  参数：reg为正则表达式##########
def zhengze(reg):
    regg = set(re.findall(reg, txt))
    for i in regg:
        tihuan(i)
#####遍历列表内需要替换的字符串，调用tihuan函数
for i in range(len(lis)):
    tihuan(lis[i])

txt = wenjian()
zhengze(reg1)
zhengze(reg2)
zhengze(reg3)
zhengze(reg4)
txt3 = wenjian()
print(txt3)
jieba.load_userdict("zidian.txt")   #添加字典
cut = jieba.cut(txt3,cut_all=False)      #jieba分词
txt4 = ' '.join(cut)     #拼接输出

# 显示词频，显示10个词
# seg = jieba.analyse.extract_tags(txt3, topK = 10, withWeight = True,allowPOS=())
# for tag, weight in seg:
#     print("%s %s" %(tag, weight))
######生成词云#######
alice_coloring = np.array(Image.open(os.path.join( "1.jpg")))
my_wordcloud = WordCloud(background_color="pink", height=1000,width=1000,max_words=5000,mask=alice_coloring,max_font_size=40, random_state=42,font_path='G:\\SIMLI.TTF').generate(txt4)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()#显示生成的词云
my_wordcloud.to_file(os.path.join("222.png"))#保存文件
