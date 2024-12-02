import pyautogui
import time

# Remember to delimit items in the string with a space. e.g. item1 item2 item3
import_data = """ 

""".split()

batch_size = 10  # Number of items per batch

# Process import_data in batches of batch_size (adjustable)
for i in range(0, len(import_data), batch_size):
    batch = import_data[i:i + batch_size]

    input(f"Press Enter to start batch {i // batch_size + 1}...")  # Wait for user to start
    time.sleep(1)  # Time delay before starting script to focus the cursor on the input field (adjustable)

    for item in batch:
        pyautogui.typewrite(item)  # Type the item
        pyautogui.press('enter')  # Press Enter
        time.sleep(0.3)  # Allow system time to process

    print(f"Batch {i // batch_size + 1} completed!")

print("-------------------\nAll data inputted!")
