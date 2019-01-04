import os
import glob
import shutil
folder = "/media/ubuntu/data/DataSet/dataall/前置摄像头/qianzhi/FrontCamera"
files = glob.glob(folder+"/*.jpg")

batch =[]
batch_size = len(files)//10
batch_sizes =[batch_size*t for t in range(11)]
for i,j in enumerate(batch_sizes):
    if i!=10:
        batch.append(files[batch_sizes[i]:batch_sizes[i+1]])

for l,x in enumerate(batch):
    new_path = "/media/ubuntu/data/DataSet/dataall/前置摄像头/qianzhi/batch_{}".format(l)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for new_file in x:
        shutil.move(new_file,new_path)
        print(new_file)