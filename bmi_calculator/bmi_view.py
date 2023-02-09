import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class Bmi_view(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("350x300")
        self.create_bmi_view()

    def create_bmi_view(self):
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
        self.bmi_label = customtkinter.CTkLabel(self, text = "BMI-Wert: 0", 
                                           font = customtkinter.CTkFont(family = "futura", size = 20))
        self.bmi_label.grid(column = 0, row = 3, columnspan = 2, padx = 20, pady = 20)

    def calculate_event(self):
        bmi = float(self.weight_input_field.get()) / pow(float(self.height_input_field.get()), 2)
        self.bmi_label.configure(text = "BMI-Wert: " + str(round(bmi, 2)))
        self.set_bmi_coloring(round(bmi, 2))

        
    def set_bmi_coloring(self, bmi):
        if bmi <= 17:
            self.bmi_label.configure(fg_color = "#e78284", text_color = "black")
        elif bmi <= 18.5 and bmi > 17:
            self.bmi_label.configure(fg_color = "#e5c890", text_color = "black")
        elif bmi <= 25 and bmi > 18.5:
            self.bmi_label.configure(fg_color = "#a6d189", text_color = "black")
        elif bmi <= 30 and bmi > 25:
            self.bmi_label.configure(fg_color = "#e5c890", text_color = "black")
        elif bmi <= 35 and bmi > 30:
            self.bmi_label.configure(fg_color = "#ef9f76", text_color = "black")
        elif bmi > 35:
            self.bmi_label.configure(fg_color = "#e78284", text_color = "black")

view = Bmi_view()
view.mainloop()
