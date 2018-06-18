import csv
import os
import shutil
import string

typeofobject = 2874
basepath = '/home/hszc/Desktop/ZHIHUICHENGSHI/version1/facenet/data/mydata/'
pic_path = '/home/hszc/Desktop/ZHIHUICHENGSHI/version1/facenet/data/mydata/train/'
csvfile = open(basepath+'train.csv', 'r')
data = []
pic_name = []
for line in csvfile:
    data.append(list(line.strip().split(',')))
# print(data[0][0])
print(len(data))


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print "---  new folder...  ---"
        print "---  OK  ---"

    else:
        print "---  There is this folder!  ---"



#directly generate new folder
# def genDir():
#     base = basepath+'train_new/'
#     i = 0
#     for j in range(typeofobject):
#         file_name = base + str(i)
#         os.mkdir(file_name)
#         i=i+1
#
# genDir()

for i in range(len(data)):

    cl = data[i][1]
    print(cl)
    ffolder = basepath+'train_new/'+cl
    print(ffolder)
    mkdir(ffolder)
    pic_name = data[i][0]
    print(pic_name)

    path = pic_path + pic_name
    print('path is',path)

    isExists = os.path.exists(path)
    if (isExists):
        newpath = ffolder + '/' + pic_name
        shutil.copyfile(path, newpath)
        print 'success'
    else:
        print "not here"
