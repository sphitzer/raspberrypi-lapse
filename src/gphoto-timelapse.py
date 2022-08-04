import subprocess
import argparse

parser = argparse.ArgumentParser(description='Timelapse via picamera or gphoto2')

parser.add_argument('--name', type=str, dest='name', help='name of folder timelapse to be saved in')

parser.add_argument('--frames', type=int, dest='frames',
                   help='Total number of photos taken')
parser.add_argument('--interval', dest='interval', type=int,
                   help='Time between each photo')

args = parser.parse_args()
print(args)

timelapse_name=str(args.name)


print("interval: " + str(args.interval))
print("frames: " + str(args.frames))
print("timelapse name: " + timelapse_name)

shoot_timelapse = subprocess.Popen(["gphoto2","--capture-image-and-download","--filename","./" + timelapse_name + "/photo-%Y%m%d-%H%M%S.arw","--interval",str(args.interval),"--frames",str(args.frames)],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = shoot_timelapse.communicate()
print(stdout)
print(stderr)
