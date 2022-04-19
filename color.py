import os
import re
import cv2

"""
DOTA annotation format:
0    1   2   3  4    5   6   7
x1, y1, x2, y2, x4, y4, x3, y3, class_name, difficulty, (vertices are arranged in a clockwise order)
(x1, y1)-----------(x2, y2)
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
(x3, y3)-----------(x4, y4)
"""

root_dir = r"C:\Users\lyin0\Desktop\DOTA\\"  # DOTA dataset path
annotations_dir = root_dir + r"original_annotation_style2\\"
image_dir = root_dir + r"JPEGImages/"
xml_dir = root_dir + r"Jet_Annotations_XML//"  # output xml file path
save = root_dir + r'Jet_Images//'

COLORMAP = [cv2.COLORMAP_JET, cv2.COLORMAP_INFERNO, cv2.COLORMAP_AUTUMN,
            cv2.COLORMAP_PINK, cv2.COLORMAP_HSV, cv2.COLORMAP_HOT, cv2.COLORMAP_BONE]

colormap_type = COLORMAP[0]

for img_name in os.listdir(image_dir):
    # print(img_name)
    img_id = re.match(r'.+\.', img_name)

    img = cv2.imread(image_dir + img_name)  # height, width

    jet_img = cv2.applyColorMap(img, colormap_type)
    save_dir = save + r'jet_' + img_name
    cv2.imwrite(save_dir, jet_img)

    filename = img_id.group() + 'txt'
    fin = open(annotations_dir + filename, 'r')
    image_name = filename.split('.')[0]
    # img = Image.open(image_dir + image_name + ".jpg")  # width, height
    xml_name = xml_dir + r'r_' + image_name + '.xml'
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
        fout.write('\t\t' + '<width>' + str(img.shape[0]) + '</width>' + '\n')  # img_width
        fout.write('\t\t' + '<height>' + str(img.shape[1]) + '</height>' + '\n')  # img_height
        fout.write('\t\t' + '<depth>' + '3' + '</depth>' + '\n')
        fout.write('\t' + '</size>' + '\n')

        fout.write('\t' + '<segmented>' + '0' + '</segmented>' + '\n')
        o_height, o_width = img.shape[0], img.shape[1]  # int
        for line in fin.readlines():
            line = line.split(' ')
            fout.write('\t' + '<object>' + '\n')
            fout.write('\t\t' + '<name>' + str(line[8]) + '</name>' + '\n')
            fout.write('\t\t' + '<pose>' + 'Unspecified' + '</pose>' + '\n')
            fout.write('\t\t' + '<truncated>' + line[6] + '</truncated>' + '\n')
            fout.write('\t\t' + '<difficult>' + str(int(line[9])) + '</difficult>' + '\n')
            fout.write('\t\t' + '<bndbox>' + '\n')

            fout.write('\t\t\t' + '<xmin>' + str(o_height - float(line[5])) + '</xmin>' + '\n')
            fout.write('\t\t\t' + '<ymin>' + line[0] + '</ymin>' + '\n')
            fout.write('\t\t\t' + '<xmax>' + str(o_height - float(line[1])) + '</xmax>' + '\n')
            fout.write('\t\t\t' + '<ymax>' + line[2] + '</ymax>' + '\n')

            fout.write('\t\t' + '</bndbox>' + '\n')
            fout.write('\t' + '</object>' + '\n')

        fin.close()
        fout.write('</annotation>')
