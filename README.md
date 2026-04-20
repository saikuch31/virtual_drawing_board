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

## Controls

- `q` or `Esc`: quit
- `c`: clear drawing
- `s`: save drawing to `drawings/`
- `m`: show/hide the black-and-white color mask debug window

The main window should show the normal color webcam feed. The color mask is a
debug view used later for tuning object tracking.

## macOS Notes

When you run the app for the first time, macOS may ask for camera permission.
Allow camera access for the terminal or IDE you are using to run Python.

## Tuning

The starter HSV range in `config.py` is set up for a blue object. If tracking is
poor, adjust `HSV_LOWER`, `HSV_UPPER`, and `MIN_CONTOUR_AREA` for your lighting
and object color.

4/19 -- Got the webcam working but I'm wearing a blue sweatshirt so it keeps on latching onto that. I need to find a way for it to select a specific object. I also want to add hand sign recognition technology as well. 