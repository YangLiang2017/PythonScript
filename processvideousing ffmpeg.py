# -*- coding: utf-8 -*-   


#顺时针旋转画面90度

#ffmpeg -i test.mp4 -vf "transpose=1" out.mp4
#逆时针旋转画面90度

#ffmpeg -i test.mp4 -vf "transpose=2" out.mp4
#顺时针旋转画面90度再水平翻转

#ffmpeg -i test.mp4 -vf "transpose=3" out.mp4
#逆时针旋转画面90度水平翻转

#ffmpeg -i test.mp4 -vf "transpose=0" out.mp4
#水平翻转视频画面

#ffmpeg -i test.mp4 -vf hflip out.mp4
#垂直翻转视频画面

#ffmpeg -i test.mp4 -vf vflip out.mp4

  
import os  
import argparse
import sys
import fileinput
parser = argparse.ArgumentParser(description='')
parser.add_argument('-file', type=str, default ='')
parser.add_argument('-rotate', type=str, default ='')
parser.add_argument('-outfile', type=str, default ='')
args = parser.parse_args()
input=args.file
rotate=args.rotate
output=args.outfile

outputFile=open(output,'w')
print input

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录 
        print(files) #当前路径下所有非目录子文件 
        for filename in files:
            filenamepath=input+"/"+filename
            str_video= "ffmpeg -i"+" "+filenamepath+" "+"-strict -2 -vf"+" transpose="+rotate+" "+filename+".mp4"
            outputFile.write(filename+"\n")
            os.popen(str_video)
            print filename 
file_name(input)
