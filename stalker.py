import sys,os,getopt

APP_NAME = "stalker"
VERSION = "0.2.0"

def track(input,output,yolo_model):
    
    import cv2,time
    from ultralytics import YOLO
    from moviepy.editor import VideoFileClip
    
    model = YOLO(yolo_model)
    tracker = "bytetrack.yaml"

    tmp = str(int(time.time()))+"_temp.mp4"
    source = input
    cap = cv2.VideoCapture(source)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count/fps
    count = 0

    # 保存临时文件
    fourcc = cv2.VideoWriter_fourcc('M','P','4','V')
    temp_out = cv2.VideoWriter(tmp,fourcc,fps,(frame_width,frame_height))
    
    while cap.isOpened():
        frame_exists, frame = cap.read()
        
        if frame_exists :
            
            count = count + 1
            results = model.track(source=frame,tracker=tracker,persist=True)
        
            annotated_frame = results[0].plot(boxes=False)
        
            # cv2.imshow("YOLOv8 Tracking",annotated_frame)
            temp_out.write(annotated_frame)
        
            # Press Q on keyboard to exit (with cv2.imshow)
            # if cv2.waitKey(1) & 0xFF == ord("q"):
            #     break
        else:
            break
    cap.release()
    temp_out.release()
    # cv2.destroyAllWindows()
    
    # 补全音轨
    video_clip = VideoFileClip(tmp)
    origin_video_clip = VideoFileClip(input)

    video_clip_with_audio = video_clip.set_audio(origin_video_clip.audio)
    video_clip_with_audio.write_videofile(output)
    
    # 删除临时文件
    os.remove(tmp)

def main(argv):
    help_message = '''stalker.py %s 
options:
    -h,--help       :   查看帮助
    -v,--version    :   程序版本
    -m,--model      :   yolo8模型
args:
    -i,--input      :   输入需要追踪的视频地址
    -o,--output     :   输出追踪视频存放地址
    ''' % (VERSION)
    
    input = None
    output = None
    model = "yolov8n-pose.pt"
    try:
        opts,args = getopt.getopt(argv,"vhi:o:",["version","help","input=","output="])
    except:
        print(help_message)
        sys.exit(2)
    for opt,arg in opts:
        if opt in ("-v","--version"):
            print("%s (%s)" % (APP_NAME,VERSION))
            sys.exit()
        elif opt in("-h","--help"):
            print(help_message)
            sys.exit()
        elif opt in ("-i","--input"):
            input = arg
        elif opt in ("-o","--output"):
            output = arg
        elif opt in ("-m","--model"):
            model = arg
    
    if input is None or output is None:
        print(help_message)
        sys.exit(2)
    
    print("input : %s" % (input))
    print("output : %s" % (output))
    print("yolo model : %s" % (model))
        

    track(input,output,yolo_model=model)
    
if __name__ == "__main__":
    main(sys.argv[1:])