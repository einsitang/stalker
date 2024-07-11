# stalker

a sample program based on the [YOLOv8](https://github.com/ultralytics/ultralytics/) model for in-video character detection and tracking markup to learn python and understand how to  use yolo or other machine learning models

# documentation


## dependency

python version >=3.8 with ML package(ultralytics,pytorch) including opencv , moviepy

## install

clone and enter this repository

```bash
git clone https://github.com/einsitang/stalker.git
cd stalker
```

use venv to create python virtual env in python3(>=3.8) :

```bash
python3 -m venv venv
source venv/bin/activate
```

pip install the requirements

```bash
pip install -r requirements.txt
```

## usage

use python command:
```bash
python stalker.py -i video_file_path -o video_track_worked_path
```

example:
```bash
python stalker.py -i ~/Downloads/IMG_1120.MOV -o ~/Downloads/test5.mp4
```

you can also use `python stalker.py -h` to know all arguments instructions

> the first run this script may take few time,because yolo will download yolo model
> only happens on the first run

# effect

*origin video :*

![before](img/before.gif)

*after stalker :*

![after](img/after.gif)