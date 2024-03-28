import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)
def start(command) :
    # Media Keys
    if command == "play" :
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
    elif command == "mute" :
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.1)
    elif command == "next" :
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.1)
    elif command == "prev" :
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
    # Open Applications 
    elif command == "firefox" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Firefox\n')
        time.sleep(0.1)
    elif command == "discord" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Discord\n')
        time.sleep(0.1)
    elif command == "steam" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Steam\n')
        time.sleep(0.1)
    elif command == "Spotify" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Spotify\n')
        time.sleep(0.1)
    elif command == "vscode" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Visual Studio\n')
        time.sleep(0.1)
    # Open Websites
    elif command == "youtube" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Firefox\n')
        time.sleep(0.3)
        write_text.write('youtube\n')
        time.sleep(0.1)
    elif command == "instagram" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Firefox\n')
        time.sleep(0.3)
        write_text.write('inst\n')
        time.sleep(0.1)
    elif command == "reddit" :
        keyboard.send(Keycode.GUI)
        time.sleep(0.3)
        write_text.write('Firefox\n')
        time.sleep(0.3)
        write_text.write('reddit\n')
        time.sleep(0.1)
        
        
        
        
        
        