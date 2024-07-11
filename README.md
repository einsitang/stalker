# stalker

a sample program based on the [YOLOv8](https://github.com/ultralytics/ultralytics/) model for in-video character detection and tracking markup to learn python and understand how to  use yolo or other machine learning models

# documentation


## dependency

python version >=3.8 with ML package(ultralytics,pytorch) including opencv , moviepy

## install

clone and enter this repository

```
git clone https://github.com/einsitang/stalker.git
cd stalker
```

use venv to create python virtual env in python3(>=3.8) :

```python
python3 -m venv venv
```

pip install the requirements

```python
pip install -r requirements
```

## usage

use python command:
```
python stalker.py -i video_file_path -o video_track_worked_path
```

example:
```
python stalker.py -i ~/Downloads/IMG_1120.MOV -o ~/Downloads/test5.mp4
```

the first run this script may take few time,because yolo will download yolo model

only happens on the first run

# effect

> origin video :

![before](img/before.gif)

> after stalker :

![after](img/after.gif)