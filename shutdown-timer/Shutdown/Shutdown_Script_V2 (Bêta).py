import tkinter as tk
import tkinter.messagebox
import os

var_restart = False
var_shutdown = False

seconds = 0 # [0, 59] 0 s -> 59 seconds # timer+=1
minutes = 60 # [1, 59] 1m -> 59 minutes # timer+=60
hours = 3600 # [1, 23] 1h -> 23 hours # timer+=3600
days = 86400 # [1, 3650] 1d -> 365 days (1 year) # timer+=86400

message_stop = "echo vous avez annulé l'action"
message_stop2 = "echo vous avez déjà annulé l'action"
cmd_stop = 'shutdown -a'

message_shutdown = "echo votre ordinateur va s'éteindre dans 7200 secondes"
cmd_shutdown = 'shutdown -s -t '

message_restart = "echo votre ordinateur va redémarrer dans 7200 secondes"
cmd_restart = 'shutdown -r -t '

message_welcome = "echo Vous pouvez à tout instant programmer l'interruption ou le redémarrage de votre machine !"

time = 0

def ft_shutdown():
    global var_restart, var_shutdown
    if (var_restart or var_shutdown == True):
        os.system(cmd_stop) # commande d'annulation
    else:
        var_shutdown = True
    os.system(cmd_shutdown + str(time)) # commande d'interruption et timer modifiable
    tkinter.messagebox.showinfo("Juste pour dire", "Votre ordinateur va s'éteindre dans " + str(time) + " secondes") # message info
    return var_restart, var_shutdown
        

def ft_restart():
    global var_restart, var_shutdown
    if (var_restart or var_shutdown == True):
        os.system(cmd_stop)
    else:
        var_restart = True
    tkinter.messagebox.showinfo("Juste pour dire", "Votre ordinateur va redémarrer " + str(time) + " secondes") # message info
    os.system(cmd_restart + str(time)) # commande de redémarrage et timer modifiable
    return var_restart, var_shutdown
    

def ft_cancel():
    global var_restart, var_shutdown
    if(var_restart or var_shutdown == True):
        # os.system(message_stop) ancienne méthode
        tkinter.messagebox.showinfo("Juste pour dire", "Plus aucun plannification n'est en cours")
        os.system(cmd_stop)
        var_restart =  False
        var_shutdown = False
    else:
        # os.system(message_stop2) # Ancienne méthode
        tkinter.messagebox.showwarning("Arrêtes la drogue", "Calme toi c'est bon, tu cliques une fois ça marche !")

    return var_restart, var_shutdown

def programming(seconds, minutes, hours, days):
    os.system(message_welcome)
        
root = tk.Tk()

canvas = tk.Canvas(root, heigh="200", width="200", bg="grey")
canvas.pack()

label = tk.Label(root,  text="GUI SOFTWARE", bg="blue", fg="white")
label.pack(side="top")

# entry = tk.Entry(root, heigh="100", width="100", bg="purple")
# entry.pack()

s_button = tk.Button(canvas, text="Shutdown",
                   bg='black', fg='red', command=ft_shutdown)
s_button.pack(side='left', fill="both", expand=True)

r_button = tk.Button(canvas, text="Restart",
                   bg='black', fg='red', command=ft_restart)
r_button.pack(side='left', fill="both", expand=True)

c_button = tk.Button(canvas, text="Cancel",
                   bg='black', fg='red', command=ft_cancel)
c_button.pack(side='left', fill="both", expand=True)

# t_button = tk.Entry(canvas, font=40)
# t_buttun.place(relwidth=0.5, relheight=0.5)

root.mainloop()