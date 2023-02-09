import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class Bmi_view(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("350x300")
        
        self.init_grid_laylout()
        self.init_input_fields()
        self.init_labels()
        self.init_calculate_button()
        self.init_bmi_label()
        
    def init_grid_laylout(self):
        self.grid_rowconfigure(0, weight = 0)
        self.grid_columnconfigure((0, 1), weight = 0)    
        
    def init_input_fields(self): 
        self.weight_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in kg")
        self.weight_input_field.grid(column = 1, row = 0, padx = 20, pady = 20)
        
        self.height_input_field = customtkinter.CTkEntry(master = self, placeholder_text="in m")
        self.height_input_field.grid(column = 1, row = 1, padx = 20, pady = 20)

    def init_labels(self):
        weight_label = customtkinter.CTkLabel(self, text="Gewicht", font=customtkinter.CTkFont(family = "futura", size=20))
        weight_label.grid(column = 0, row = 0, padx = 20, pady = 20)

        height_label = customtkinter.CTkLabel(self, text="Höhe", font=customtkinter.CTkFont(family = "futura", size=20))
        height_label.grid(column = 0, row = 1, padx = 20, pady = 20)

    def init_calculate_button(self):
        self.calculate_button = customtkinter.CTkButton(self, text = "Berechnen", width = 300, command = self.calculate_event)
        self.calculate_button.grid(column = 0, row = 2, columnspan = 2, padx = 20, pady = 20)

    def init_bmi_label(self):
        self.bmi_label = customtkinter.CTkLabel(self, fg_color = "#a6d189", text_color = "black", text = "BMI-Wert: 0", 
                                           font = customtkinter.CTkFont(family = "futura" ,size = 20))
        self.bmi_label.grid(column = 0, row = 3, columnspan = 2, padx = 20, pady = 20)

    def calculate_event(self):
        bmi = float(self.weight_input_field.get()) / pow(float(self.height_input_field.get()), 2)
        self.bmi_label.configure(text = "BMI-Wert: " + str(round(bmi, 2)))

view = Bmi_view()
view.mainloop()
