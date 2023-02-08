import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class Bmi_view(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x240")
        
        self.init_input_fields()
        
    def init_grid_laylout(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)        

    
        
    def init_input_fields(self): 
        weight_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in kg")
        weight_input_field.grid(row = 1, column = 2, padx = 20, pady = 20)
        
        height_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in m")
        height_input_field.grid(row = 2, column = 2, padx = 20, pady = 20)

    def init_labels(self):
        weight_label = customtkinter.CTkLabel(self, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))

    
view = Bmi_view()
view.mainloop()
