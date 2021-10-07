import json

news_item_id = []
with open('test_text.txt', 'r') as t:
    for line in t.readlines():
        end = line.find(',')
        id = line[:end]
        news_item_id.append(id)
count = 0
data = []
print(len(news_item_id))
with open('trained_result_3sentence_4batch-5000step.txt', 'r') as f:
    for line in f.readlines():
        d = {'NewsItemId': news_item_id[count], 'summary':line}
        data.append(d)
        count += 1
        print(count)

with open('trained_result_3sentence_4batch-5000step.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)