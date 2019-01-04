import xml.etree.ElementTree as ET
import os
import glob
import argparse
import shutil
import time
parse = argparse.ArgumentParser()
parse.add_argument("--path",default="/media/ubuntu/data1/dataset/大车数据/images/images/",type=str,help="dataset path")
args = parse.parse_args()
path = args.path
if not os.path.exists(path):
    raise FileNotFoundError("路径不存在:{}".format(path))
xml_file = glob.glob(path+"/*.xml")
image_file = glob.glob(path+"/*.jpg")
new_imagespath = path+"/images"
new_xmlpath = path+"/annotations"
if len(xml_file)==0:
    raise ValueError("There is no any xmlfile:{}".format(path))

if len(image_file)==0:
    raise ValueError("There is no any imagefile:{}".format(path))

img_count=0
xml_count=0

for i in xml_file:
    tree = ET.parse(i)
    root = tree.getroot()
    rootlist = []
    for child in root:
        rootlist = [child.tag]
        rootlist.append(rootlist)
        #print(child.tag)
    #print(rootlist)
    annotation = root.findall('object')
    if not annotation:
        filepath = os.path.split(i)[0]
        filename = os.path.splitext(os.path.split(i)[1])[0]
        if not os.path.exists(filepath+"/"+filename+".jpg"):
            print(filepath+"/"+filename+".jpg"+"不存在")
            continue
        #print(filepath+"/"+filename+".jpg")
        os.remove(filepath+"/"+filename+".jpg")
        img_count+=1
        if not os.path.exists(filepath+"/"+filename+".xml"):
            print(filepath+"/"+filename+".xml"+"不存在!")
            continue
        #print(filepath+"/"+filename+".xml")
        os.remove(filepath+"/"+filename+".xml")
        xml_count+=1
if img_count!=xml_count:
    print("图片数量和xml数量不相等")
print("一共删除图片{}个".format(img_count))
print("一共删除xml{}个".format(xml_count))

if not os.path.exists(new_imagespath):
    os.mkdir(new_imagespath)
if not os.path.exists(new_xmlpath):
    os.mkdir(new_xmlpath)

print("对齐图片与xml的数量!")
time.sleep(1)
new_image_list = glob.glob(path+"/*.jpg")
new_xml_list = glob.glob(path+"/*.xml")
list =[]
if len(new_image_list)>len(new_xml_list):
    list = new_image_list
else:
    list = new_xml_list
new_img_count = 0
new_xml_count = 0
for j in list:
    path = os.path.split(j)[0]
    name = os.path.splitext(os.path.split(j)[1])[0]
    type = os.path.splitext(os.path.split(j)[1])[1]

    if type==".jpg":
        xmlfile =path+"/"+name+".xml"
        if xmlfile not in new_xml_list:
            os.remove(j)
            print("删除xml:{}".format(j))
        else:
            shutil.move(xmlfile, new_xmlpath + "/" + name + ".xml")
            shutil.move(j,new_imagespath + "/" + name + ".jpg")

    else:
        jpgfile = path+"/"+name+".jpg"
        if jpgfile not in new_image_list:
            os.remove(j)
            print("删除图片:{}".format(j))
        else:
            shutil.move(jpgfile,new_imagespath+"/"+name+".jpg")
            shutil.move(j, new_xmlpath + "/" + name + ".xml")
