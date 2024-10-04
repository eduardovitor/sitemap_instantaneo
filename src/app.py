import customtkinter as ctk
import sitemap
import validators
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window definition
        self.geometry("650x500")
        # Min window size
        self.minsize(650,500)
        # Max window size
        self.maxsize(800,500)
        # Grid configuration
        self.grid_columnconfigure((0, 1, 2), weight=1)
        # Defining window title
        self.title("Sitemap instantâneo")
        # Defining main label
        self.label_title = ctk.CTkLabel(self,text="Sitemap instantâneo",font=("Open Sans",30))
        # Defining URL label
        self.label_url = ctk.CTkLabel(self,text="URL: ",font=("Open Sans",15))
        # Defining URL entry
        self.entry_url = ctk.CTkEntry(self, placeholder_text="Endereço do website",width=250, fg_color="transparent",text_color="white",corner_radius=20)
        # Defining action button
        self.action_button = ctk.CTkButton(self, text="Gerar sitemap",command=self.button_callback, corner_radius=20)
        # Define success/failure message
        self.label_success = ctk.CTkLabel(self, text="", font=("Open Sans",12))
        self.label_success.grid(row=3, padx=60, pady=60)
        # Positioning elements on grid
        self.label_title.grid(row=0,column=0,padx=40,pady=70)
        self.label_url.grid(row=1,column=0,columnspan=1,sticky="ew")
        self.entry_url.grid(row=1,column=1,columnspan=2,sticky="w")
        self.action_button.grid(row=2,column=2,padx=70,pady=70,sticky="w")
    def button_callback(self):
        if self.entry_url.get() != "":
            if validators.url(self.entry_url.get()):
                links = sitemap.scrapy_subpages(self.entry_url.get())
                filename = filedialog.asksaveasfilename()
                sitemap.generate_xml(f"{filename}.xml",links,self.entry_url.get())
                self.label_success.configure(text="Arquivo gerado com sucesso!")
            else:
                self.label_success.configure(text="URL inválida!")


app = App()
app.mainloop()