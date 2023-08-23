from simple_term_menu import TerminalMenu
import os
import subprocess

def destroy_from_list(options):
    for process in options:
        command = "tmux kill-window -t " + process[4:]
        os.system(command)
    exit()


output = subprocess.run(["tmux", "ls"], capture_output=True).stdout
output_list = output.decode("utf8").split("\n")

options = []

for line in output_list:
    line = line[0:line.find(":")]
    options.append("[ ] " + line)

options = options[:-1]
options.append("Destroy")
options.append("Exit")

menu_entry_index = -1

while True:
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == options.index("Destroy"):
        kill_list = list()
        for process in options[0:-2]:
            if "x" in process:
                kill_list.append(process)
        destroy_from_list(kill_list)
    if menu_entry_index == options.index("Exit"):
        exit()

    fliped_option = options[menu_entry_index]
    if fliped_option[1] == " ":
        fliped_option = "[x]" + fliped_option[3:]
    else:
        fliped_option = "[ ]" + fliped_option[3:]
    options[menu_entry_index] = fliped_option
