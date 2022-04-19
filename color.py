import os
import re
import cv2


root_dir = r"C:\Users\lyin0\Desktop\DOTA\\"  # DOTA dataset path
annotations_dir = root_dir + r"original_annotation_style2\\"
image_dir = root_dir + r"JPEGImages/"
xml_dir = root_dir + r"Color_Annotations_XML//"  # output xml file path
save = root_dir + r'Color_Images//'

COLORMAP = [cv2.COLORMAP_JET, cv2.COLORMAP_INFERNO, cv2.COLORMAP_AUTUMN,
            cv2.COLORMAP_PINK, cv2.COLORMAP_HSV, cv2.COLORMAP_HOT, cv2.COLORMAP_BONE]

colormap_type_idx = 0

for img_name in os.listdir(image_dir):
    # print(img_name)
    img_id = re.match(r'.+\.', img_name)

    img = cv2.imread(image_dir + img_name)  # height, width

    c_img = cv2.applyColorMap(img, COLORMAP[colormap_type_idx])
    save_dir = save + r'c_' + img_name
    cv2.imwrite(save_dir, c_img)
    
"""
RENAME PART


import os

c_annotation_files_dir = r'C:\Users\lyin0\Desktop\DOTA\Color_Annotations_XML\\'

for file_name in os.listdir(c_annotation_files_dir):
    new_name = r'c_' + file_name
    os.rename(c_annotation_files_dir + file_name, c_annotation_files_dir + new_name)
"""
