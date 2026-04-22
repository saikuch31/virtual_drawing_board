"""Webcam access helpers."""

import cv2

import config


class Camera:
    """Small wrapper around OpenCV camera capture."""

    def __init__(self, index=config.CAMERA_INDEX, flip=config.FLIP_CAMERA):
        self.index = index
        self.flip = flip
        self.capture = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)

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


def find_available_cameras(search_range=config.CAMERA_SEARCH_RANGE):
    """Return camera indexes that OpenCV can open on this machine."""
    available_indexes = []

    for index in search_range:
        capture = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)
        if capture.isOpened():
            success, _ = capture.read()
            if success:
                available_indexes.append(index)
        capture.release()

    return available_indexes
