# Libraries
import board
import usb_hid
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# Set up Keyboard and Mouse
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

# Set up Buttons
# Select All Button
all_btn = digitalio.DigitalInOut(board.GP0)
all_btn.direction = digitalio.Direction.INPUT
all_btn.pull = digitalio.Pull.DOWN
# Save Button
save_btn = digitalio.DigitalInOut(board.GP1)
save_btn.direction = digitalio.Direction.INPUT
save_btn.pull = digitalio.Pull.DOWN
# Find Button
find_btn = digitalio.DigitalInOut(board.GP2)
find_btn.direction = digitalio.Direction.INPUT
find_btn.pull = digitalio.Pull.DOWN
# Find and Replace Button
find_replace_btn = digitalio.DigitalInOut(board.GP3)
find_replace_btn.direction = digitalio.Direction.INPUT
find_replace_btn.pull = digitalio.Pull.DOWN
# Copy Button
copy_btn = digitalio.DigitalInOut(board.GP4)
copy_btn.direction = digitalio.Direction.INPUT
copy_btn.pull = digitalio.Pull.DOWN
# Paste Button
paste_btn = digitalio.DigitalInOut(board.GP5)
paste_btn.direction = digitalio.Direction.INPUT
paste_btn.pull = digitalio.Pull.DOWN
# Cut Button
cut_btn = digitalio.DigitalInOut(board.GP6)
cut_btn.direction = digitalio.Direction.INPUT
cut_btn.pull = digitalio.Pull.DOWN
# ALT+TAB Button
alt_tab_btn = digitalio.DigitalInOut(board.GP7)
alt_tab_btn.direction = digitalio.Direction.INPUT
alt_tab_btn.pull = digitalio.Pull.DOWN
# CTRL+Z Button
ctrl_z_btn = digitalio.DigitalInOut(board.GP8)
ctrl_z_btn.direction = digitalio.Direction.INPUT
ctrl_z_btn.pull = digitalio.Pull.DOWN
# CTRL+Y Button
ctrl_y_btn = digitalio.DigitalInOut(board.GP9)
ctrl_y_btn.direction = digitalio.Direction.INPUT
ctrl_y_btn.pull = digitalio.Pull.DOWN

# Select All Function
def sel_all():
    print("Select All Button Pressed, CTRL+A Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.A)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.A)
    print("Select All Completed")

# Save Function
def save():
    print("Save Button Pressed, CTRL+S Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.S)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.S)

# Find Function
def find():
    print("Find Button Pressed, CTRL+F Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.F)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.F)

# Find and Replace Function
def find_replace():
    print("Find and Replace Button Pressed, CTRL + H Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.H)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.H)

# Select Word Function
def select_word():
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.2)  # Slightly longer delay to ensure double-click registers
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.2)  # Adjust this as needed

# Copy Function
def copy():
    print("Copy Button Pressed, CTRL+C Initiated")
    select_word()
    time.sleep(0.3)  # Allow time for word selection to complete
    keyboard.press(Keycode.CONTROL, Keycode.C)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.C)
    print("Copy Completed")

# Paste Function
def paste():
    print("Paste Button Pressed, CTRL+V Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.V)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.V)
    print("Paste Completed")

# Cut Function
def cut():
    print("Cut Button Pressed, CTRL+X Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.X)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.X)
    print("Cut Completed")

# Alt + Tab Function
def alt_tab():
    print("Alt Tab Button Pressed, ALT+TAB Initiated")
    keyboard.press(Keycode.ALT)
    time.sleep(0.1)
    keyboard.press(Keycode.TAB)
    time.sleep(0.1)
    keyboard.release(Keycode.TAB)
    time.sleep(0.3)
    keyboard.release(Keycode.ALT)
    print("Alt Tab Completed")

# CTRL + Z Function
def undo():
    print("Undo Button Pressed, CTRL+Z Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.Z)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.Z)
    print("Undo Completed")

# CTRL + Y Function
def redo():
    print("Redo Button Pressed, CTRL+Y Initiated")
    keyboard.press(Keycode.CONTROL, Keycode.Y)
    time.sleep(0.1)
    keyboard.release(Keycode.CONTROL, Keycode.Y)
    print("Redo Completed")

# Debounce function to prevent bouncing
def handle_button(button, action, delay=0.4):
    if button.value:  # Button pressed
        action()
        time.sleep(delay)  # Debounce time

# Main loop
print("Macro Keyboard Started. Press CTRL+C to exit")
try:
    while True:
        handle_button(all_btn, sel_all)
        handle_button(save_btn, save)
        handle_button(find_btn, find)
        handle_button(find_replace_btn, find_replace)
        handle_button(copy_btn, copy)
        handle_button(paste_btn, paste)
        handle_button(cut_btn, cut)
        handle_button(alt_tab_btn, alt_tab)
        handle_button(ctrl_z_btn, undo)
        handle_button(ctrl_y_btn, redo)
        time.sleep(0.1)

# Handle keyboard interrupt
except KeyboardInterrupt:
    print("Stopped by User")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleaning Up...")