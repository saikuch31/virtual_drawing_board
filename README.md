A webcam-based drawing board for getting familiar with OpenCV.

The app tracks a colored object, finds its center point, and connects those
points over time to draw virtual pen strokes.

## Project Structure

```text
virtual_drawing_board/
  main.py              # App loop
  config.py            # Shared settings
  camera.py            # Webcam access
  color_tracker.py     # HSV masking and contour tracking
  drawing_canvas.py    # Persistent drawing layer
  pointer_colors.py    # Color presets and terminal prompt
  ui.py                # Windows, keyboard input, and display helpers
  requirements.txt
```

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python main.py
```

Before the camera opens, the terminal prompts for a camera index. On macOS,
this lets you avoid Continuity Camera by choosing the index for the Mac's
built-in webcam and reusing that same index.

Before the camera opens, the terminal prompts you to choose `red`, `green`, or
`blue`. The drawing ink matches the selected pointer color.

## Controls

- `q` or `Esc`: quit
- `c`: clear drawing
- `s`: save drawing to `drawings/`
- `m`: show/hide the black-and-white color mask debug window
- `t`: pause/resume pointer tracking

The main window should show the normal color webcam feed. The color mask is a
debug view used later for tuning object tracking.

## macOS Notes

When you run the app for the first time, macOS may ask for camera permission.
Allow camera access for the terminal or IDE you are using to run Python.

OpenCV on macOS usually selects cameras by index rather than by friendly device
name in this setup. If your iPhone appears through Continuity Camera, pick the
index that corresponds to the Mac webcam when prompted.

## Tuning

The default HSV presets live in `pointer_colors.py`. If tracking is poor for a
selected color, adjust those ranges for your lighting and object color.
