"""Webcam access helpers."""

import cv2

import config


class Camera:
    """Small wrapper around OpenCV camera capture."""

    def __init__(self, index=config.CAMERA_INDEX, flip=config.FLIP_CAMERA):
        self.index = index
        self.flip = flip
        self.capture = cv2.VideoCapture(index)

        if not self.capture.isOpened():
            raise RuntimeError(f"Could not open webcam at index {index}.")

    def read(self):
        """Return the next camera frame."""
        success, frame = self.capture.read()
        if not success:
            raise RuntimeError("Could not read frame from webcam.")

        if self.flip:
            frame = cv2.flip(frame, 1)

        return frame

    def release(self):
        """Release the camera device."""
        self.capture.release()
