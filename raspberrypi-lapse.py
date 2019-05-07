#raspberrypi-lapse
#timelapse program for rapsberry pi
#runs a timelapse based on several different methods of input

import os, sys
import argparse
import time
from picamera import PiCamera

#argparse
parser = argparse.ArgumentParser()
parser.add_argument('--mode', help='picam or usbcam')
parser.add_argument('--tlname', type=str, help='name of the timelapse.')
parser.add_argument('--duration', type=int, help='duration in seconds.  use argument --duration-unit to set a different unit')
parser.add_argument('--interval', type=int, help='interval between photos in seconds.  use argument --interval-unit to set a different unit')
args = parser.parse_args()




#needed configs
##timelapse name
##duration 
##interval
##
tl_name = args.tlname
duration = args.duration
interval = args.interval


camera = PiCamera()
camera.start_preview()
time.sleep(2)

try:
  original_umask = os.umask(0)
  os.mkdir('./' + tl_name,0o777)
except OSError as ose:
  print('Timelapse with the name %s already exists' % tl_name)
  sys.exit(1)
else:
  print('Created timelapse. Photos located under /%s' % tl_name)
finally:
  os.umask(original_umask)

initial_time = time.time()

for filename in camera.capture_continuous(tl_name + '/img{counter:03d}.jpg'):
  elapsed_time = int(time.time() - initial_time)
  print('Capture {}   {} seconds have passed since the beginning of the timelapse'.format(filename,elapsed_time))

  if elapsed_time > duration:
    break

  time.sleep(interval)
