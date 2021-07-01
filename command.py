
import os
import cv2
import time
import numpy as np

from pathlib import Path
from line_draw import draw_line
draw=True
for i in range(8):
    folder_path = "dongsin_two_" + str(i+1)
    save_folder_path = "ROI/" + folder_path + "/"
    Path(save_folder_path).mkdir(parents=True, exist_ok=True)
    image_path = "label_data/" + folder_path
    file = os.listdir(image_path)
    for file_name in file:
        root, child = os.path.splitext(file_name)
        image = cv2.imread(image_path + "/"+ file_name)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        width, height, _ = image.shape
        if draw :
            line_info = draw_line(image)
            draw = False
    
        x_min = line_info[0][0] if line_info[0][0] < line_info[1][0] else line_info[1][0]
        x_max = line_info[0][0] if line_info[0][0] > line_info[1][0] else line_info[1][0]
        y_min = line_info[0][1] if line_info[0][1] < line_info[1][1] else line_info[1][1]
        y_max = line_info[0][1] if line_info[0][1] > line_info[1][1] else line_info[1][1]
        roi = image[y_min:y_max,x_min:x_max]
        black_img = np.zeros((width, height,3),np.uint8)
        black_img[y_min:y_max,x_min:x_max] = roi

        roi_output_path = save_folder_path + "ROI_" + file_name
        cv2.imwrite(roi_output_path, black_img) 


