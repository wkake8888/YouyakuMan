import pandas as pd
body_list = []
sum_list = []
text_file = open('test_text.txt', "r")
for line in text_file.readlines():
    l = line
    s1 = l.find('body') + 8
    e1 = l.find("'}")
    t1 = l[s1: e1]
    body_list.append(t1)

    s2 = l.find('body', s1) + 8
    e2 = l.find("'}", s2)
    t2 = l[s2: e2]
    body_list.append(t2)

