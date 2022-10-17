import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("AutoScheduler")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Parameters",
                                              text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=10, padx=10)
        
        label = customtkinter.CTkLabel(master=self.frame_left,
                               textvariable=tkinter.StringVar(value="Name:"),
                               width=60,
                               height=20,
                               corner_radius=8)
        label.place(relx=0.33, rely=0.13, anchor=tkinter.E)
        entryN = customtkinter.CTkEntry(master=self.frame_left,
                               placeholder_text="",
                               width=105,
                               height=20,
                               border_width=2,
                               corner_radius=10)
        entryN.place(relx=0.30, rely=0.13, anchor=tkinter.W)

        label = customtkinter.CTkLabel(master=self.frame_left,
                               textvariable=tkinter.StringVar(value="Event:"),
                               width=60,
                               height=20,
                               corner_radius=8)
        label.place(relx=0.33, rely=0.18, anchor=tkinter.E)
        entryE = customtkinter.CTkEntry(master=self.frame_left,
                               placeholder_text="",
                               width=105,
                               height=20,
                               border_width=2,
                               corner_radius=10)
        entryE.place(relx=0.30, rely=0.18, anchor=tkinter.W)

        label = customtkinter.CTkLabel(master=self.frame_left,
                               textvariable=tkinter.StringVar(value="Appearance Mode"),
                               width=60,
                               height=20,
                               corner_radius=8)
        label.place(relx=0.50, rely=0.89, anchor=tkinter.CENTER)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.changeAppearance)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=3, rowspan=5, pady=20, padx=20, sticky="nsew")

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CALENDAR WIP" ,
                                                   height=125,
                                                   corner_radius=6, 
                                                   fg_color=("white", "gray38"), 
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nswe", padx=15, pady=15)

        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Create Event",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.buttonEvent())
        self.button_1.grid(row=8, column=0, columnspan=1, pady=20, padx=20, sticky="e")

        self.optionmenu_1.set("Dark")
    
    def buttonEvent(self):
        return

    def changeAppearance(self, newAppearance):
        customtkinter.set_appearance_mode(newAppearance)

    def onClosing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()