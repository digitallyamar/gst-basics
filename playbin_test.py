import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)
myplay = Gst.ElementFactory.make("playbin", None)
assert myplay
print (myplay)