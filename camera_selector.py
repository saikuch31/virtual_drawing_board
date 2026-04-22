"""Camera selection helpers for macOS/OpenCV."""

import config
from camera import find_available_cameras


def prompt_for_camera_index():
    """Prompt for a camera index and keep the choice explicit."""
    available_indexes = find_available_cameras()

    if not available_indexes:
        raise RuntimeError("No available cameras were found.")

    choices = ", ".join(str(index) for index in available_indexes)
    default_index = config.CAMERA_INDEX

    print(f"Available camera indexes: {choices}")
    print(
        "If Continuity Camera is being selected automatically, "
        "choose the index for your Mac webcam and keep using that one."
    )

    while True:
        response = input(
            f"Choose a camera index [{default_index}]: "
        ).strip()

        if response == "":
            response = str(default_index)

        if not response.isdigit():
            print(f"Invalid choice. Please enter one of: {choices}")
            continue

        camera_index = int(response)
        if camera_index in available_indexes:
            return camera_index

        print(f"Invalid choice. Please enter one of: {choices}")
