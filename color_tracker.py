"""Color-based object tracking."""

from dataclasses import dataclass

import cv2
import numpy as np

import config


@dataclass(frozen=True)
class TrackingResult:
    center: tuple[int, int] | None
    mask: np.ndarray
    contour_area: float


class ColorTracker:
    """Find the center point of the largest object in an HSV color range."""

    def __init__(
        self,
        hsv_lower=config.HSV_LOWER,
        hsv_upper=config.HSV_UPPER,
        min_contour_area=config.MIN_CONTOUR_AREA,
    ):
        self.hsv_lower = np.array(hsv_lower, dtype=np.uint8)
        self.hsv_upper = np.array(hsv_upper, dtype=np.uint8)
        self.min_contour_area = min_contour_area

    def track(self, frame):
        """Return the tracked center point, debug mask, and contour area."""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.hsv_lower, self.hsv_upper)
        mask = self._clean_mask(mask)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if not contours:
            return TrackingResult(center=None, mask=mask, contour_area=0.0)

        largest_contour = max(contours, key=cv2.contourArea)
        contour_area = cv2.contourArea(largest_contour)

        if contour_area < self.min_contour_area:
            return TrackingResult(center=None, mask=mask, contour_area=contour_area)

        moments = cv2.moments(largest_contour)
        if moments["m00"] == 0:
            return TrackingResult(center=None, mask=mask, contour_area=contour_area)

        center_x = int(moments["m10"] / moments["m00"])
        center_y = int(moments["m01"] / moments["m00"])

        return TrackingResult(
            center=(center_x, center_y),
            mask=mask,
            contour_area=contour_area,
        )

    @staticmethod
    def _clean_mask(mask):
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=2)
        return mask
