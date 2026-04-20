"""Entry point for the virtual drawing board."""

from camera import Camera
from color_tracker import ColorTracker
import config
from drawing_canvas import DrawingCanvas
import ui


def run():
    camera = Camera()
    tracker = ColorTracker()
    canvas = None
    show_mask = config.SHOW_MASK_WINDOW

    try:
        while True:
            frame = camera.read()

            if canvas is None:
                canvas = DrawingCanvas(frame.shape)

            result = tracker.track(frame)
            canvas.update(result.center)

            output_frame = canvas.overlay_on(frame)
            output_frame = ui.draw_hud(
                output_frame,
                result.center,
                result.contour_area,
            )
            ui.show(output_frame, result.mask, show_mask)

            key = ui.read_key()
            if key in ui.QUIT_KEYS:
                break
            if key == ui.CLEAR_KEY:
                canvas.clear()
            if key == ui.SAVE_KEY:
                output_path = canvas.save()
                print(f"Saved drawing to {output_path}")
            if key == ui.DEBUG_MASK_KEY:
                show_mask = not show_mask
    finally:
        camera.release()
        ui.close_windows()


if __name__ == "__main__":
    run()
