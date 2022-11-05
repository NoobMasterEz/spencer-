import threading
import os

import cv2
from django.http.response import StreamingHttpResponse
from django.shortcuts import render


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(
            f"rtsp://admincamera:camera20scoopscnx@{os.getenv('LOCATIONS_CAMERA')}:554/stream1"
        )
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def __call__(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    response = StreamingHttpResponse(
        gen(VideoCamera()),
        status=200,
        content_type='multipart/x-mixed-replace; boundary=frame')
    response['Cache-Control'] = 'no-cache'
    return response


def index(request):
    return render(request, 'streamapp/camera.html')
