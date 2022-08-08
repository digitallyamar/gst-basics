###############################################################################
# To run on Ubuntu 22.04, need to install:
# sudo apt install gir1.2-gst-rtsp-server-1.0
# Ref: https://stackoverflow.com/questions/52634893/importerror-cannot-import-name-gstrtspserver-introspection-typelib-not-found
###############################################################################

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GLib, Gst, GstRtspServer

Gst.init(None)

mainloop = GLib.MainLoop()
server = GstRtspServer.RTSPServer()
mounts = server.get_mount_points()

factory = GstRtspServer.RTSPMediaFactory()
factory.set_launch('(v4l2src device=/dev/video0 ! videoconvert ! x264enc speed-preset=ultrafast tune=zerolatency ! rtph264pay name=pay0 pt=96 )')

mounts.add_factory('/test', factory)

server.attach(None)

print ('Streaming at rtsp://127.0.0.1:8554/test')
mainloop.run()