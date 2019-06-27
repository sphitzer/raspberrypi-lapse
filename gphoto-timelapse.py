import subprocess

timelapse_name='four-hr'

shoot_timelapse = subprocess.Popen(["gphoto2","--capture-image-and-download","--filename","./" + timelapse_name + "/photo-%Y%m%d-%H%M%S.jpg","--interval","60","--frames","14400"],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout,stderr = shoot_timelapse.communicate()
print(stdout)
print(stderr)


