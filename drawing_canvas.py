"""Persistent drawing layer for tracked pen strokes."""

from pathlib import Path
from time import strftime

import cv2
import numpy as np

import config


class DrawingCanvas:
    """Keep drawing strokes separate from the live webcam frame."""

    def __init__(
        self,
        frame_shape,
        pen_color=config.PEN_COLOR,
        pen_thickness=config.PEN_THICKNESS,
    ):
        self.canvas = np.zeros(frame_shape, dtype=np.uint8)
        self.pen_color = pen_color
        self.pen_thickness = pen_thickness
        self.previous_point = None

    def update(self, point):
        """Draw from the previous tracked point to the current point."""
        if point is None:
            self.previous_point = None
            return

        if self.previous_point is not None:
            cv2.line(
                self.canvas,
                self.previous_point,
                point,
                self.pen_color,
                self.pen_thickness,
            )

        self.previous_point = point

    def overlay_on(self, frame):
        """Combine the webcam frame with the drawing canvas."""
        return cv2.addWeighted(frame, 1.0, self.canvas, 1.0, 0)

    def clear(self):
        """Erase all strokes."""
        self.canvas[:] = 0
        self.previous_point = None

    def save(self, directory=config.SAVE_DIR):
        """Save the current drawing canvas and return the output path."""
        output_dir = Path(directory)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f"drawing_{strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(str(output_path), self.canvas)
        return output_path
