# Ref: https://www.youtube.com/watch?v=HDY8pf-b1nA

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstApp', '1.0')
from gi.repository import Gst, GstApp, GLib
from threading import Thread
from time import sleep

Gst.init()

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target = main_loop.run)
main_loop_thread.start()

pipeline = Gst.parse_launch('v4l2src ! decodebin ! videoconvert ! appsink name=sink')
appsink = pipeline.get_by_name('sink')

pipeline.set_state(Gst.State.PLAYING)

# Wait to give enough time for pipeline to startup

try:
    while True:
        # Try to pull a sample within a second, if not give up
        sample = appsink.try_pull_sample(Gst.SECOND)
        if sample is None:
            continue

        print ("I've got a sample!")
except KeyboardInterrupt:
    # Ctrl C to stop this app
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()