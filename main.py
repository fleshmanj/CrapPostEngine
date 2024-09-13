import keyboard
import win32clipboard

# Create a dictionary with keys as strings "0" to "9" with empty string values
bank = {str(i): "" for i in range(10)}

def edit_slot(key, value):
    # Update the specified slot in the bank with the new value, appending a newline
    bank[key] = value + "\n"
    return bank

def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        clipboard_contents = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return clipboard_contents
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        return ""

def get_bank_slot(key):
    # Retrieve the value from the specified slot in the bank
    return bank.get(key, "")

def write_text(text):
    # Clear stuck modifiers before writing
    keyboard.release('ctrl')
    keyboard.release('alt')
    keyboard.release('shift')
    keyboard.write(text, delay=0.002)
    keyboard.release('ctrl')
    keyboard.release('alt')
    keyboard.release('shift')

if __name__ == '__main__':
    # Set up hotkeys for each digit
    for i in range(10):
        key = str(i)
        # Ctrl+Alt+<digit> to write the content of the corresponding slot
        keyboard.add_hotkey(f"left ctrl+alt+{key}", lambda k=key: write_text(get_bank_slot(k)))
        # Ctrl+Shift+<digit> to store clipboard content in the corresponding slot
        keyboard.add_hotkey(f"left ctrl+shift+{key}", lambda k=key: edit_slot(k, get_clipboard_data()))

    # Run until Ctrl+Alt+Q is pressed
    while True:
        keyboard.wait("left ctrl+alt+q")
        break
