"""
This script is joined with filp.py
"""

import os
from PIL import Image

root_dir = r"C:\Users\lyin0\Desktop\Dataset\DOTA\train\\"  # DOTA dataset path
annotations_dir = root_dir + r"trainset_reclabelTxt\\"
image_dir = root_dir + r"images/"
xml_dir = root_dir + r"Flip_Annotations_XML/"  # output xml file path

flip_type = r'h'

"""
Script for converting DOTA annotation to VOC annotation
DOTA annotation format:
x1, y1, x2, y2, x4, y4, x3, y3, class_name, difficulty, (vertices are arranged in a clockwise order)
(x1, y1)-----------(x2, y2)
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
(x3, y3)-----------(x4, y4)
"""

for filename in os.listdir(annotations_dir):
    fin = open(annotations_dir + filename, 'r')
    image_name = filename.split('.')[0]
    img = Image.open(image_dir + image_name + ".jpg")
    xml_name = xml_dir + flip_type + r'_flip_' + image_name + '.xml'
    with open(xml_name, 'w') as fout:
        fout.write('<annotation>' + '\n')

        fout.write('\t' + '<folder>DOTA 1.0</folder>' + '\n')
        fout.write('\t' + '<filename>' + image_name + '.png' + '</filename>' + '\n')

        fout.write('\t' + '<source>' + '\n')
        fout.write('\t\t' + '<database>' + 'DOTA 1.0' + '</database>' + '\n')
        fout.write('\t\t' + '<annotation>' + 'DOTA 1.0' + '</annotation>' + '\n')
        fout.write('\t\t' + '<image>' + 'flickr' + '</image>' + '\n')
        fout.write('\t\t' + '<flickrid>' + 'Unspecified' + '</flickrid>' + '\n')
        fout.write('\t' + '</source>' + '\n')

        fout.write('\t' + '<owner>' + '\n')
        fout.write('\t\t' + '<flickrid>' + 'Kazusa' + '</flickrid>' + '\n')
        fout.write('\t\t' + '<name>' + 'Kazusa' + '</name>' + '\n')
        fout.write('\t' + '</owner>' + '\n')

        fout.write('\t' + '<size>' + '\n')
        fout.write('\t\t' + '<width>' + str(img.size[0]) + '</width>' + '\n')  # img_width
        fout.write('\t\t' + '<height>' + str(img.size[1]) + '</height>' + '\n')  # img_height
        fout.write('\t\t' + '<depth>' + '3' + '</depth>' + '\n')
        fout.write('\t' + '</size>' + '\n')

        fout.write('\t' + '<segmented>' + '0' + '</segmented>' + '\n')
        width, height = img.size[0], img.size[1]
        for line in fin.readlines():
            line = line.split(' ')
            fout.write('\t' + '<object>' + '\n')
            fout.write('\t\t' + '<name>' + str(line[8]) + '</name>' + '\n')
            fout.write('\t\t' + '<pose>' + 'Unspecified' + '</pose>' + '\n')
            fout.write('\t\t' + '<truncated>' + line[6] + '</truncated>' + '\n')
            fout.write('\t\t' + '<difficult>' + str(int(line[9])) + '</difficult>' + '\n')
            fout.write('\t\t' + '<bndbox>' + '\n')
            if flip_type == 'h':
                fout.write('\t\t\t' + '<xmin>' + str(width - float(line[4])) + '</xmin>' + '\n')
                fout.write('\t\t\t' + '<ymin>' + line[1] + '</ymin>' + '\n')
                fout.write('\t\t\t' + '<xmax>' + str(width - float(line[0])) + '</xmax>' + '\n')
                fout.write('\t\t\t' + '<ymax>' + line[5] + '</ymax>' + '\n')
            elif flip_type == 'v':
                fout.write('\t\t\t' + '<xmin>' + line[0] + '</xmin>' + '\n')
                fout.write('\t\t\t' + '<ymin>' + str(height - float(line[5])) + '</ymin>' + '\n')
                fout.write('\t\t\t' + '<xmax>' + line[4] + '</xmax>' + '\n')
                fout.write('\t\t\t' + '<ymax>' + str(height - float(line[1])) + '</ymax>' + '\n')
            elif flip_type == 'vh':
                fout.write('\t\t\t' + '<xmin>' + str(width - float(line[4])) + '</xmin>' + '\n')
                fout.write('\t\t\t' + '<ymin>' + str(height - float(line[5])) + '</ymin>' + '\n')
                fout.write('\t\t\t' + '<xmax>' + str(width - float(line[0])) + '</xmax>' + '\n')
                fout.write('\t\t\t' + '<ymax>' + str(height - float(line[1])) + '</ymax>' + '\n')
            else:
                print("Please choose flip type: h(horizontal), v(vertical), or vh(vertical + horizontal).")
            
            fout.write('\t\t' + '</bndbox>' + '\n')
            fout.write('\t' + '</object>' + '\n')

        fin.close()
        fout.write('</annotation>')
