import numpy as np
def readfile(filename):
    data = np.loadtxt(filename, dtype=str, delimiter='\t')
    province1 = list(data[:, 0])
    province =list(set(province1)) # 去除相同省份
    province.sort(key=province1.index)
    city = data[:, 1]
    number = data[:, 2]
    return province,city,number,data


def classification(province,data):
    finalresult = []
    for i in province:
        m = 1
        classresult = [[0] * 2 for _ in range(100)]
        classresult[0][0] = i
        classresult[0][1] = ''
        for j in range(len(data)):
            if data[j][0] == i and data[j][2] != '0' :  # 输出文本中需要删去待明确地区
                classresult[m][0] = str(data[j][1])
                classresult[m][1] = str(data[j][2])
                m = m + 1
        classresult =[i for i in classresult if i[1] != 0 and i[0] != 0]  # 去掉列表中为0的以便于输出保存
        finalresult = finalresult +classresult
        finalresult.append(' ')
    return finalresult


def writeintotxt(finalresult):
    t = ''
    with open('yq_out.txt', 'w') as q:
        for i in range(len(finalresult)):
            for e in range(len(finalresult[i])):
                t = t + str(finalresult[i][e])+' '
            q.write(t.strip(''))
            q.write('\n')
            t = ''


if __name__ == '__main__':
    filename = input("请输入要读取的文件名：")
    province,city,number,data = readfile(filename)
    finalresult = classification(province, data)
    writeintotxt(finalresult)






