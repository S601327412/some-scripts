import os
import glob
import shutil
#import randompy
image_path = "/media/ubuntu/data/DataSet/dataall/前置摄像头/qianzhi"
count = 500
batch = []
new_folder = "/media/ubuntu/data/DataSet/dataall/前置摄像头/qianzhi/new/"
#os.mkdir(new_folder)
for root,dirs,files in os.walk(image_path):
    for x in dirs:
        for j in glob.glob(os.path.join(image_path,x)+"/*.jpg"):

            batch.append(j[:count])

def copy(nums,filelist):
    num = 0
    for j in filelist:
        new_file = os.path.splitext(os.path.split(j)[1])[0]
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        shutil.copyfile(j,new_folder+new_file)
        nums+=1
        print(j)
    print("total num is {}".format(num))

#copy(count,batch)