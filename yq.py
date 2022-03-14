import numpy as np
from pypinyin import lazy_pinyin
from xpinyin import Pinyin


def readfile(filename):
    data = np.loadtxt(filename, dtype=str, delimiter='\t',encoding='UTF-8')  # ,encoding='UTF-8'
    province1 = list(data[:, 0])
    # 此处得到每个省的数目：
    provinceclass = [[0] * 2 for _ in range(10)]
    province =list(set(province1)) # 去除相同省份
    province.sort(key=province1.index)
    for i in range(len(province)):
        provinceclass[i][0] = province[i]
        provinceclass[i][1] = 0
        for j in range(len(province1)):
            if province[i] == province1[j]:
                provinceclass[i][1] +=1
    provinceclass = [i for i in provinceclass if i[1] != 0 and i[0] != 0]  # 去掉列表中为0的以便于输出保存
    city = data[:, 1]
    number = data[:, 2]
    return province,city,number,data,provinceclass


def sortProvince(provinceclass):  # 按输出省总数大小排序
    for i in range(0, len(provinceclass)):
        for j in range(0, len(provinceclass)-i-1):
            if int(provinceclass[j][1]) < int(provinceclass[j+1][1]):
                provinceclass[j], provinceclass[j+1] = provinceclass[j+1], provinceclass[j]
    for i in range(0, len(provinceclass)-1):
        if provinceclass[i][1] == provinceclass[i+1][1]:
            if Pinyin().get_pinyin(provinceclass[i][0]) > Pinyin().get_pinyin(provinceclass[i+1][0]):
                provinceclass[i], provinceclass[i + 1] = provinceclass[i+1], provinceclass[i]
    return provinceclass
# yq_in_03.txt yq_out_04.txt
def sortCity(provinceclass):  # 按输出市总数大小排序
    provinceclass.remove(provinceclass[0])
    for i in range(0, len(provinceclass)):
        for j in range(0, len(provinceclass)-i-1):
            if int(provinceclass[j][1]) < int(provinceclass[j+1][1]):
                provinceclass[j], provinceclass[j+1] = provinceclass[j+1], provinceclass[j]
    for i in range(0, len(provinceclass)-1):
        if provinceclass[i][1] == provinceclass[i+1][1]:
            if Pinyin().get_pinyin(provinceclass[i][0]) > Pinyin().get_pinyin(provinceclass[i+1][0]):
                provinceclass[i], provinceclass[i + 1] = provinceclass[i+1], provinceclass[i]
    return provinceclass


def sortfinal(provinceclass):  # 排序结果
    finalresult = []
    for i in range(len(provinceclass)):
        m = 1
        province1 = [[0] * 2 for _ in range(1)]
        province1[0] = provinceclass[i]
        classresult = [[0] * 2 for _ in range(100)]
        classresult[0][0] = provinceclass[i][0]
        for j in range(len(data)):
            if data[j][0] == provinceclass[i][0] and data[j][2] != '0':  # 输出文本中需要删去待明确地区
                classresult[m][0] = str(data[j][1])
                classresult[m][1] = str(data[j][2])
                m = m + 1
        classresult[0][1] = m
        classresult = [i for i in classresult if i[1] != 0 and i[0] != 0]  # 去掉列表中为0的以便于输出保存
        sort_classresult = province1+sortCity(classresult)  # 城市也按数量和字母排序
        finalresult = finalresult + sort_classresult
        finalresult.append(' ')
    return finalresult



# def classification(province,data):
#     finalresult = []
#     for i in province:
#         m = 1
#         classresult = [[0] * 2 for _ in range(100)]
#         classresult[0][0] = i
#         for j in range(len(data)):
#             if data[j][0] == i and data[j][2] != '0' :  # 输出文本中需要删去待明确地区
#                 classresult[m][0] = str(data[j][1])
#                 classresult[m][1] = str(data[j][2])
#                 m = m + 1
#         classresult[0][1] = m
#         classresult =[i for i in classresult if i[1] != 0 and i[0] != 0]  # 去掉列表中为0的以便于输出保存
#         finalresult = finalresult +classresult
#         finalresult.append(' ')
#     return finalresult


def writeintotext(finalresult,out_filename):
    t = ''
    with open(out_filename, 'w') as q:
        for i in range(len(finalresult)):
            for e in range(len(finalresult[i])):
                t = t + str(finalresult[i][e])+' '
            q.write(t.strip(''))
            q.write('\n')
            t = ''


if __name__ == '__main__':
    # 实验二
    # filename = input("请输入要读取的文件名：")
    # province,city,number,data = readfile(filename)
    # finalresult = classification(province, data)
    # writeintotext(finalresult)

    # 实验三
    # in_filename, out_filename, province_name = (input().split(' '))
    # province, city, number, data = readfile(in_filename)
    # if province_name == '':
    #     finalresult = classification(province, data)
    #     writeintotext(finalresult,out_filename)
    # else:
    #     finalresult = outProvince(province_name)
    #     writeintotext(finalresult, out_filename)

    # 实验四 每个省后面有总数，输出省按总数大小排序
    in_filename, out_filename = (input().split(' '))
    province, city, number, data, province_class = readfile(in_filename)
    provinceclass = sortProvince(province_class)
    finalresult = sortfinal(provinceclass)
    writeintotext(finalresult, out_filename)
    # print(finalresult)







