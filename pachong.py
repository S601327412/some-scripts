import os
import xlrd
import urllib.request
import glob
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--excel_folder",default="/media/ubuntu/data1/20181214",type=str,help="your excel file saved folder")
parser.add_argument("--download_image_savedpath",default="/media/ubuntu/data1/20181214",type=str,help="your down_load iamges saved path")
parser.add_argument("--pre_url",default="https://www.123yb.cn/warn/",type=str,help="you need download image's url前缀")
parser.add_argument('--download_type',default="video",type=str,help="which source you want to download")
args = parser.parse_args()
path = args.excel_folder+"/*.xlsx"
if not os.path.exists(args.excel_folder):
    raise FileNotFoundError("path not found!")

xlsx_filepath = glob.glob(path)

print("该路径下一共有",int(len(xlsx_filepath)),"个excel文件")
if len(path)==0:
    raise ValueError("该路径下没有excel文件!")

pre_url = args.pre_url
type = args.download_type
savepaths = args.download_image_savedpath + "/"
if not os.path.exists(savepaths):
    raise FileNotFoundError("The path is not exists!")

def parse_xlsx_image(filelist,type):
    urllist = []
    if type=="images":
        indx = 2
    else:
        indx = 3
    for file in filelist:
        excelfile = xlrd.open_workbook(file)
        sheetname = excelfile.sheet_by_index(0)
        col_values = sheetname.col_values(2)
        urllist.append(col_values[2:])

    return urllist,filelist

def download_image(urllist,savepath,filelist,type):
    if type=="images":
        strs = ".jpg"
        name = "图"
    elif type=="video":
        strs = ".mp4"
        name = "视频"
    else:
        raise ValueError("The type is not current!")
    count = 0
    j = 0
    for urls in urllist:
        print("file is ", filelist[j])
        time.sleep(2)
        i=0
        for url in urls:
            times = time.time()
            try:
                urllib.request.urlretrieve(pre_url+url,savepath+"{}_{}{}".format(i,times,strs))
                i += 1
            except:
                if url==" ":
                    print("地址为空,下载失败!")
                else:
                    print(pre_url+url+":"+"下载失败!")
            print("第{}个文件的第{}{}".format(j+1,i,name))
        count+=i
        j += 1
    print("Download Finished!一共{}{}".format(count,name))

if __name__ == "__main__":
    data,filelist = parse_xlsx_image(xlsx_filepath,type)
    download_image(data,savepaths,filelist,type)

