import tkinter as tkinter
import json

# Create window
root = tkinter.Tk()
# Add title to window
root.title("My Window")
# Add window sizes
root.geometry("500x500")

# Back to main view
def switch_to_main(view) :
    view.pack_forget()
    mainView.pack()

# Go to jsoan view
def switch_to_json(jsonName):
    mainView.pack_forget()
    # cardLevelsView.columnconfigure(0, weight=1)
    # cardLevelsView.columnconfigure(1, weight=3)
    cardLevelsView.pack()
    # Load and parse JSON
    with open(f"json/{jsonName}.json", "r") as file:
        data = json.load(file)

    text = json.dumps(data, indent=4)
    txt.delete("1.0", "end")
    txt.insert("end", text)

# WINDOW ELEMENTS
# Main view
mainView = tkinter.Frame(root)
mainView.pack()
# View with card levels
cardLevelsView = tkinter.Frame(root)
# Scrollbar
scrollBar = tkinter.Scrollbar(root)
scrollBar.pack(side="right", fill="y")

# Buttons
# Buttons for main view
btnUndead = tkinter.Button( mainView, text="Display Undead Cards", command=lambda: switch_to_json("undead"))
btnDamned = tkinter.Button(mainView, text="Display Damned Cards", command=lambda: switch_to_json("damned"))
btnElves = tkinter.Button(mainView, text="Display Elves Cards", command=lambda: switch_to_json("elves"))
btnEmpire = tkinter.Button(mainView, text="Display Empire Cards", command=lambda: switch_to_json("empire"))
btnOrcs = tkinter.Button(mainView, text="Display Orcs Cards", command=lambda: switch_to_json("orcs"))

btnUndead.pack()
btnDamned.pack()
btnElves.pack()
btnEmpire.pack()
btnOrcs.pack()
# Buttons for card levels view
btnBack = tkinter.Button(cardLevelsView, text="Back to races", command=lambda: switch_to_main(cardLevelsView))
btnBack.pack()
# Text
txt = tkinter.Text(cardLevelsView, font="Courier", yscrollcommand=scrollBar.set)
txt.pack(fill="both", expand=True)

# Some kind of watcher for events and interactions with window
root.mainloop()