import cv2
import os

def get_frames(video_path:str, output_folder:str='images', num_frames=10):
    # Read video
    cap = cv2.VideoCapture(video_path)

    # read num_frames number of frames with even distances between and save those to output_folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_num % (cap.get(cv2.CAP_PROP_FRAME_COUNT) // num_frames) == 0:
            cv2.imwrite(f'{output_folder}/{frame_num}.jpg', frame)
        frame_num += 1
    cap.release()
    cv2.destroyAllWindows()
    return frame_num
