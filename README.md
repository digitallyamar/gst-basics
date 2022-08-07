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