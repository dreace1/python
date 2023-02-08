import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class Bmi_view(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x240")
        
        self.init_grid_laylout()
        self.init_input_fields()
        self.init_labels()
        
    def init_grid_laylout(self):
        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure((0, 1), weight = 0)    
          

    
        
    def init_input_fields(self): 
        weight_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in kg")
        weight_input_field.grid(column = 1, row = 0, padx = 20, pady = 20)
        
        height_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in m")
        height_input_field.grid(column = 1, row = 1, padx = 20, pady = 20)

    def init_labels(self):
        weight_label = customtkinter.CTkLabel(self, text="Gewicht", font=customtkinter.CTkFont(family = "futura", size=20))
        weight_label.grid(column = 0, row = 0, padx = 20, pady = 20)

        height_label = customtkinter.CTkLabel(self, text="Höhe", font=customtkinter.CTkFont(family = "futura", size=20))
        height_label.grid(column = 0, row = 1, padx = 20, pady = 20)
    
view = Bmi_view()
view.mainloop()
