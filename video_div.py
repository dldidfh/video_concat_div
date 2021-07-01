
import os
import cv2
from pathlib import Path


read_file_path = './output_video/'
file = os.listdir(read_file_path)

for file_name in file:
    root, child = os.path.splitext(file_name)
    save_folder_path = "./label_data/"+ root + '/'
    Path(save_folder_path).mkdir(parents=True, exist_ok=True)
    url = read_file_path +file_name
    try:
        vid = cv2.VideoCapture(int(url))
    except:
        vid = cv2.VideoCapture(url)
    frame_num = 0
    i = 1
    while True:
        return_value, frame = vid.read()
        if return_value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            print('Video has ended or failed, try a different video format!')
            break
        if frame_num % 90 == 0:
            cv2.imshow("frame",frame)
            cv2.imwrite(save_folder_path + root + "_" + str(i) + ".jpg",frame)
            i+=1
        frame_num += 1






#3초마다 캡쳐 --> ffmpeg는 너무 느려서 opnecv 로 변경 
# for i in range(2):
#     if i == 0:
#         url = "./output_video/dongsin_one_"
#     else:
#         url = "./output_video/dongsin_two_"
#     
#     for j in range(29):
#         data_output = "./label_data/label_" + str(i) + '/' + str(i) + "_" + str(j) + ".bmp"
#         start_time2 = start_time1 + j*30
#         os.system(
#             'ffmpeg -y -loglevel warning -i ' + url + ' -ss ' + str(start_time2) + ' -frames:v 1 ' + data_output
#         )
    


    

