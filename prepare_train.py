import pickle
import json

with open('2020-12.train.json') as f:
    data = json.load(f)
    for i in range(2739):
        article = data[i]['paper']['body']
        summary = data[i]['summary']['body']
        dic = {'body': article, 'summary': summary}
        file_name = 'train_txt' + str(i) + '.pickle'
        train_file = open('train_datas/' + file_name, 'wb')
        pickle.dump(dic, train_file)

# train_file = open("train_txt3.pickle", "wb")
# train_file2 = open("train_txt4.pickle", "wb")

# pickle.dump(a, train_file)
# pickle.dump(b, train_file2)