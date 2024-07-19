import os
import cv2
import time
import argparse
import random 

parse = argparse.ArgumentParser()
parse.add_argument("--video_path", type=str, help="the video path")
parse.add_argument("--output_path", type=str, help="the output path")
parse.add_argument("--frame_per_sec", type=int, help="the frame that will extract in one secend")
parse.add_argument("--imgsz" , type=int, help="the output image shape (optional)")
parse.add_argument("--noise" , type=bool , help="noise of image (optional)")
args = parse.parse_args()

VIDEO_PATH = args.video_path
OUTPUT_PATH = args.output_path
FRAME_PER = args.frame_per_sec
IMG_SZ = args.imgsz
NOISE = args.noise


def value_is_none(video_path: str, output_path: str, frame_per: int) -> str:
    value_object = {
        "video_path": video_path,
        "output_path": output_path,
        "frame_per_sec": frame_per
    }
    
    for key, value in value_object.items():
        if value is None:
            print(f"- please give a value to --{key} argument !")

def noise(frame , xs , ys):
    type_ = ["rectangle" , "circle"]
    choise = random.choice(type_)

    if choise == "rectangle" :
        for i in range(15):
            x , y = random.randint(0 , xs) , random.randint(0 , ys)
            color = [random.randint(100,255) , random.randint(100,255) , random.randint(100,255)]


            cv2.rectangle(frame , (x,y) , (x+7 , y+7) , color=color , thickness=-1)
    else :
        for i in range(15):
            x , y = random.randint(0 , xs) , random.randint(0 , ys)
            color = [random.randint(100,255) , random.randint(100,255) , random.randint(100,255)]


            cv2.circle(frame , (x,y) , 3 , color=color , thickness=-1)

    return frame


x = 0
sec = 0
if VIDEO_PATH != None and FRAME_PER != None and OUTPUT_PATH != None:
    if os.name == "posix" :
        video_name = VIDEO_PATH.split("/")[-1][:-4]
    if os.name == "nt" :
        video_name = VIDEO_PATH.split("\\")[-1][:-4]

    if os.path.exists(VIDEO_PATH):
        video = cv2.VideoCapture(VIDEO_PATH)
        fps = int(video.get(cv2.CAP_PROP_FPS))

        while video.isOpened():
            _, frame = video.read()
            
            if _:
                ys , xs = frame.shape[:-1]
                if IMG_SZ != None:
                    frame = cv2.resize(frame, (IMG_SZ, IMG_SZ))

                if x % fps == 0:
                    for i in range(FRAME_PER):
                       if NOISE and random.random() > 0.2 :
                           frame = noise(frame , xs , ys)
                       
                       cv2.imwrite(os.path.join(OUTPUT_PATH, f"{video_name}-{sec}-{i}.png"), frame)
                    sec += 1 
                x += 1
            else:
                print("done.")
                time.sleep(2)
                exit()
    else:
        print("the video does not exist!!!")
        time.sleep(2)
        exit()
else:
    print("==========================================")
    value_is_none(VIDEO_PATH, OUTPUT_PATH, FRAME_PER)
    print("==========================================")
