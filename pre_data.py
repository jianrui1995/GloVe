# @Time: 2020/2/20 21:09
# @Author: R.Jian
# @Note: 预处理data文件夹中的文件，形成语料库

import json
import os

crop = open("crops.txt","w",encoding="utf8")
paths = os.walk("data/")
for path in paths:
    print(path)
    for data in path[2]:
        path1 = path[0]+data
        print(path1)
        f = open(path1,"r",encoding="utf-8-sig")
        for sentence in f.readlines():
            dict_sent = json.loads(sentence.strip())
            list_sent = list(dict_sent["originalText"])
            print(" ".join(list_sent),file=crop)
        f.close()
crop.close()


