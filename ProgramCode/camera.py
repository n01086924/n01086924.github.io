from picamera import PiCamera

from time import sleep

camera = PiCamera()
camera.rotation =180
def recVideo( sNum ):
	dest = '/home/pi/Videos/TeleVideo/'+str(sNum)+'video.h264'
	camera.start_preview()
	camera.start_recording(dest)
	sleep(4)
	camera.stop_recording()
	camera.stop_preview()
	return;

str1 = 'asda'
recVideo(str1)
