import cv2
import os

img_dir = r'./DOTA/JPEGImages/'
save = r'./DOTA/Flip_Images/'
flip_type = r'h'

imgs_name = os.listdir(img_dir)
for img_name in imgs_name:
    # print(img_name)
    img = cv2.imread(img_dir + img_name)
    if flip_type == 'h':
        hf_img = cv2.flip(img, 1)  # flip horizontal
    elif flip_type == 'v':
        vf_img = cv2.flip(img, 0)  # flip vertical
    elif flip_type == 'hv' or flip_type == 'vh':
        hvf_img = cv2.flip(img, -1)  # flip vertical and horizontal
    else:
        print('Please choose flip type: h(horizontal), v(vertical), or vh(vertical + horizontal).')
    save_dir = save + r'hf_' + img_name
    cv2.imwrite(save_dir, hf_img)
