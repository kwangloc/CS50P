import pyautogui, pyperclip, time
time.sleep(10)

li_emoji = ["😀", "😎", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹", "😊", "😇", "🙂", "🤗", "🫡", "🤔", "🫢", "🤭", "🥱", "😴"]
    
for i in range(len(li_emoji)):
    if i > 30:
        break
    pyperclip.copy("Chúc mừng sinh nhật lần " + str(i) + " " + li_emoji[i])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    # time.sleep()

