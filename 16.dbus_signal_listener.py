from pydbus import SystemBus
from gi.repository import GLib

# Create a SystemBus instance
bus = SystemBus()

# Define the signal handler function
def signal_handler(*args, **kwargs):
    print("Signal received:", args, kwargs)

# Specify the service, path, and interface
service = 'org.freedesktop.login1'
path = '/org/freedesktop/login1'
interface = 'org.freedesktop.login1.Manager'

# Get the object proxy
login_manager = bus.get(service, path)

# Connect the signal to the handler
bus.subscribe(object=path,
              signal_fired=signal_handler,
              signal='PrepareForSleep',
              dbus_interface=interface)

# Start the main loop to listen for signals
loop = GLib.MainLoop()
loop.run()
