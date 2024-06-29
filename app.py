import pyttsx3
from tkinter import Tk, Text, Button, END

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to read text aloud
def read_aloud():
    text = text_area.get("1.0", END)
    engine.say(text)
    engine.runAndWait()

# Function to save the draft to a file
def save_draft():
    with open("draft.txt", "w") as file:
        file.write(text_area.get("1.0", END))

# Function to load the draft from a file
def load_draft():
    try:
        with open("draft.txt", "r") as file:
            text_area.delete("1.0", END)
            text_area.insert("1.0", file.read())
    except FileNotFoundError:
        pass

# Create the main application window
root = Tk()
root.title("Research Paper Assistant")

# Create a text area for writing drafts
text_area = Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Create buttons to save, load, and read the draft aloud
save_button = Button(root, text="Save Draft", command=save_draft)
save_button.pack(side="left")

load_button = Button(root, text="Load Draft", command=load_draft)
load_button.pack(side="left")

read_button = Button(root, text="Read Aloud", command=read_aloud)
read_button.pack(side="left")

# Run the application
root.mainloop()
