"""Entry point for the virtual drawing board."""

from camera_selector import prompt_for_camera_index
from camera import Camera
from color_tracker import ColorTracker
import config
from drawing_canvas import DrawingCanvas
from pointer_colors import prompt_for_pointer_color
import ui


def run():
    camera_index = prompt_for_camera_index()
    color_name, color_config = prompt_for_pointer_color()
    camera = Camera(index=camera_index)
    tracker = ColorTracker(hsv_ranges=color_config["hsv_ranges"])
    canvas = None
    show_mask = config.SHOW_MASK_WINDOW
    tracking_enabled = True

    try:
        while True:
            frame = camera.read()

            if canvas is None:
                canvas = DrawingCanvas(
                    frame.shape,
                    pen_color=color_config["pen_color"],
                )

            if tracking_enabled:
                result = tracker.track(frame)
                canvas.update(result.center)
            else:
                result = ui.paused_tracking_result(frame.shape)
                canvas.lift_pen()

            output_frame = canvas.overlay_on(frame)
            output_frame = ui.draw_hud(
                output_frame,
                result.center,
                result.contour_area,
                color_name,
                tracking_enabled,
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
            if key == ui.TRACKING_TOGGLE_KEY:
                tracking_enabled = not tracking_enabled
                canvas.lift_pen()
    finally:
        camera.release()
        ui.close_windows()


if __name__ == "__main__":
    run()
