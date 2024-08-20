import time, datetime

text = 'dbus-send --system --print-reply --dest=com.cosworth.alivedrive.trackMapping\
        --type=method_call /com/cosworth/alivedrive/trackMapping/server com.cosworth.alivedrive.trackMapping.service.simulateRun\
            string:\\"/tmp/autocross_track.gpx\\" uint32:{timestamp} double:10 double:0 double:1'
result = text.format(timestamp=int(time.time()))
print(result)