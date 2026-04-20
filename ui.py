"""Display and keyboard handling."""

import cv2

import config


QUIT_KEYS = {ord("q"), 27}
CLEAR_KEY = ord("c")
SAVE_KEY = ord("s")
DEBUG_MASK_KEY = ord("m")
_mask_window_open = False


def draw_hud(frame, center, contour_area):
    """Draw basic status text on the output frame."""
    status = "tracking" if center is not None else "not tracking"
    help_text = "q: quit | c: clear | s: save | m: mask"

    cv2.putText(
        frame,
        f"{status} | area: {int(contour_area)}",
        (12, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        help_text,
        (12, 58),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    if center is not None:
        cv2.circle(frame, center, 8, (0, 255, 255), -1)

    return frame


def show(output_frame, mask=None, show_mask=False):
    global _mask_window_open

    cv2.imshow(config.WINDOW_NAME, output_frame)

    if show_mask and mask is not None:
        cv2.imshow(config.MASK_WINDOW_NAME, mask)
        _mask_window_open = True
    else:
        if _mask_window_open:
            cv2.destroyWindow(config.MASK_WINDOW_NAME)
            _mask_window_open = False


def read_key(delay=1):
    return cv2.waitKey(delay) & 0xFF


def close_windows():
    cv2.destroyAllWindows()
