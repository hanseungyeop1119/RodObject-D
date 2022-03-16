import json

f = open('../data/labels/labels.json')
label = json.load(f)

print(label)
print(type(label))
print(len(label))

# 0번지 주소
print(label[0])
print(type(label[0]))

print(label[0].keys())
# print(label[0]['name'])
print(label[0]['attributes'])
print(type(label[0]['attributes']))

# 사물 정보
print(label[0]['labels'])
print(type(label[0]['labels']))


print(label[0]['labels'][0]['category'])
print(label[0]['labels'][0]['box2d'])

'''for label in label[0]['labels']:
    print(label.keys())
    # print(label)
    # print(label[0]['labels'][0].keys())
    print(label.keys())
'''