def read_data():
    data=[]
    with open(r'C:\开大\test\diesheng\data\ds1.txt','r') as fb:
        d=fb.readlines()
        for i in d:
            data.append(i.replace('\n','').split(','))
    return data
print(read_data())
