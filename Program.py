import pynput

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

stop_program = False  # Initialize a variable to control program termination

def on_click(x, y, button, pressed):
    global stop_program  # Declare 'stop_program' as a global variable
    if pressed and button == pynput.mouse.Button.right:
        stop_program = True
    elif pressed and button == pynput.mouse.Button.left:
        keyboard.press('2')
        keyboard.release('2')
    

    if stop_program:
        return False  # Stop the listener

with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
