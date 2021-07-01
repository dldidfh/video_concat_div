import os

# read all video file to directory --> make txt file for concat --> make concat video file
read_file_path = "YOUR_PATH"
output_file_path = "OUTPUT_FILE_PATH"

file = os.listdir(read_file_path)
i = 0
q = 0
for directory_path in file:
    i +=1 
    write_file_path = output_file_path + str(i) + ".txt"
    if i == 9 : break # edit number for your data
    with open(write_file_path, mode="wt", encoding="UTF8") as f:
        for j in range(5):  # edit number for your data
            if j == 4:  # edit number for your data
                f.write("file input_video/" + output_file_path + file[q])
            else:
                f.write("file input_video/" + output_file_path + file[q] + "\n")
            q +=1 


for i in range(8):
    input_name = 'dongsin_two_'  + str(i+1) + '.txt'
    output_name = "./output_video/dongsin_two_" + str(i+1) + '.avi'
    os.system('ffmpeg -safe 1 -f concat -i ' + input_name + " -c copy " + output_name)
