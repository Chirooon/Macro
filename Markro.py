import keyboard
import time
import pyautogui
from tkinter import Tk, Label, Button, filedialog

class MacroRecorder:
    def __init__(self):
        self.recorded_keys = []

    def start_recording(self):
        keyboard.hook(self.record_key_event)
        print("Recording...")

    def stop_recording(self):
        keyboard.unhook_all()
        print("Recording stopped")
        self.save_macro()

    def play_macro(self):
        self.app_switch()
        time.sleep(1)  
        for key in self.load_macro():
            keyboard.press_and_release(key)
            time.sleep(0.1)

    def record_key_event(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == "esc":
                self.stop_recording()
            else:
                self.recorded_keys.append(key)
                print(f"Key recorded: {key}")

    def save_macro(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(file_path, "w") as file:
            file.write("\n".join(self.recorded_keys))
        print(f"Macro saved to {file_path}")

    def load_macro(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(file_path, "r") as file:
            return file.read().splitlines()

    def app_switch(self):
        # Hier Anwendungswechsel durchführen (z. B. zu Chrome)
        # Du kannst die Anwendung und den Wechselzeitpunkt anpassen
        pyautogui.hotkey('alt', 'tab')

class App:
    def __init__(self, master):
        self.master = master
        master.title("Macro Recorder")

        self.label = Label(master, text="Macro Recorder")
        self.label.pack()

        self.recorder = MacroRecorder()

        self.start_button = Button(master, text="Start Recording", command=self.recorder.start_recording)
        self.start_button.pack()

        self.stop_button = Button(master, text="Stop Recording", command=self.recorder.stop_recording)
        self.stop_button.pack()

        self.play_button = Button(master, text="Play Macro", command=self.recorder.play_macro)
        self.play_button.pack()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
