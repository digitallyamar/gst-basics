# gst-basics
Basic Gstreamer tutorial practice programs using Python

# gst-launch-1.0 basic commands

## To create a single frame image from videotestsrc

```
gst-launch-1.0 videotestsrc num-buffers=1 ! jpegenc ! filesink location=testImage.jpg
```

## To combine video and audio source with limited no. of input buffers

```
gst-launch-1.0 audiotestsrc num-buffers=50 ! vorbisenc ! oggmux name=mux ! filesink location=test.ogg videotestsrc num-buffers=50 ! theoraenc ! mux.
```

## Building GST Players using Python

### Audio Player

```
python3 playbin_audioplayer.py
```

### Video Player

```
python3 playbin_videoplayer.py
```

### Webcam Viewer

```
python3 webcam_viewer.py
```

### App sink demo

```
python3 appsink_demo.py
```

### RTSP Server and client
#### Server
```
python3 rtsp_server.py
```

#### Client
```
gst-launch-1.0 rtspsrc location=rtsp://127.0.0.1:8554/test is-live=true ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! videoscale ! autovideosink
```

### Webcam MJPEG stream	using UDP
#### Server
```
gst-launch-1.0 -v v4l2src ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5200
```
#### Client
```
gst-launch-1.0 udpsrc port=5200 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)JPEG, a-framerate=(string)30.000000, a-framesize=(string)320-240, payload=(int)96" ! rtpjpegdepay ! jpegdec ! videoconvert ! xvimagesink
```
