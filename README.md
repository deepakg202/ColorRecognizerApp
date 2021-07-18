# Color Recognizer App
Simple GUI app to detect colors from camera or an image file.

## Instructions
- Clone the repo and `cd` into the directory.
- Create a `venv` by running `python3 -m venv ./venv`
- Activate virtual env by running `source ./venv/bin/activate`
- Run `pip3 install -r requirements.txt`
- Run `python3 src`

## For using Mobile Camera (Android Devices)
- Make Sure the computer and the mobile is connected to the same wifi network
- Download `DroidCam` App
- Run the app and see the `Device IP`
- Open the Qt App and click on `Change Stream` 
- Type `http://<Device IP>:4747/mjpegfeed?640x480` and click `Ok`

To use the connected webcams on computer, type integers like `0` (Default) or `1` in `Change Stream` to use them. 

## Demo 
![Working Demo APNG](res/demo.apng)


## Python Libraries Used
- PyQt5
- OpenCV
- Pandas
