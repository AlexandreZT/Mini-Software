import tkinter as tk
import os

var_restart = False
var_shutdown = False

message_stop = "echo vous avez annulé l'action"
message_stop2 = "echo vous avez déjà annulé l'action"
cmd_stop = 'shutdown -a'

message_shutdown = "echo votre ordinateur va s'éteindre dans 300 secondes"
cmd_shutdown = 'shutdown -s -t 300'

message_restart = "echo votre ordinateur va redémarrer dans 300 secondes"
cmd_restart = 'shutdown -r -t 300'

message_welcome = "echo Vous pouvez à tout instant programmer l'interruption ou le redémarrage de votre machine !"

def ft_shutdown():
    global var_restart, var_shutdown
    if (var_restart or var_shutdown == True):
        os.system(cmd_stop)
    else:
        var_shutdown = True
    os.system(message_shutdown)
    os.system(cmd_shutdown)
    return var_restart, var_shutdown
        

def ft_restart():
    global var_restart, var_shutdown
    if (var_restart or var_shutdown == True):
        os.system(cmd_stop)
    else:
        var_restart = True
    os.system(message_restart)
    os.system(cmd_restart)
    return var_restart, var_shutdown
    

def ft_cancel():
    global var_restart, var_shutdown
    if(var_restart or var_shutdown == True):
        os.system(message_stop)
        os.system(cmd_stop)
        var_restart =  False
        var_shutdown = False
    else:
        os.system(message_stop2)

    return var_restart, var_shutdown

def ft_welcome():
    os.system(message_welcome)
        
root = tk.Tk()

canvas = tk.Canvas(root, heigh="200", width="200", bg="grey")
canvas.pack()

label = tk.Label(root,  text="GUI SOFTWARE", bg="blue", fg="white")
label.pack(side="top")

s_button = tk.Button(canvas, text="Shutdown",
                   bg='black', fg='red', command=ft_shutdown)
s_button.pack(side='left', fill="both", expand=True)

r_button = tk.Button(canvas, text="Restart",
                   bg='black', fg='red', command=ft_restart)
r_button.pack(side='left', fill="both", expand=True)

c_button = tk.Button(canvas, text="Cancel",
                   bg='black', fg='red', command=ft_cancel)
c_button.pack(side='left', fill="both", expand=True)

root.mainloop()