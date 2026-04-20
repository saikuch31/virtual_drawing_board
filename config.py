"""Shared configuration for the virtual drawing board."""

CAMERA_INDEX = 0
FLIP_CAMERA = True

WINDOW_NAME = "Virtual Drawing Board"
MASK_WINDOW_NAME = "Color Mask"
SHOW_MASK_WINDOW = False

# Starter HSV range for a blue object. Tune these for your lighting/object.
HSV_LOWER = (90, 80, 50)
HSV_UPPER = (130, 255, 255)

MIN_CONTOUR_AREA = 800

PEN_COLOR = (255, 0, 0)
PEN_THICKNESS = 6

SAVE_DIR = "drawings"
