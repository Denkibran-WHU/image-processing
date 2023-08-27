from  detect import *
from PIL import ImageDraw,Image
import os

'''
Author: 李泓俭
studentscode：2020302191936
'''

if __name__ =="__main__":

    list_number = []
    # 遍历inputs文件夹中的jpg文件，并将读取的数字字符串形式保存在list中
    imglist = glob.glob('inputs/*.jpg')
    for fhoto in imglist:
            A=MeterDetection(fhoto)
            A.Readvalue()
            readValue=A.Readvalue()
            try:
                Significant_figures = '%.5f' % readValue
                list_number.append(Significant_figures)
            except:
                list_number.append(0)
                print('识别错误')

    s = 0
    print(list_number)

    images_dir = './inputs/'
    filenames = os.listdir(images_dir)
    for filename in filenames:  # 将读取的数字写在图片左上角
        img = Image.open(images_dir + filename)
        draw_obj = ImageDraw.Draw(img)
        num = str(list_number[s])
        draw_obj.text((20, 20), num, fill='red')
        img.save('outputs/{}.jpg'.format(s))
        s += 1












