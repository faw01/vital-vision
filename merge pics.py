import cv2
import numpy as np
import glob

frameSize = (1920, 1080)

out = cv2.VideoWriter('output_video3.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 59.94, frameSize)

for filename in glob.glob('D:/GitHub/kitahack-2023/output-data-faw_preprocess.mp4-2/frames-uvw/*.png'):
    img = cv2.imread(filename)
    out.write(img)

out.release()