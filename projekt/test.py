import customtkinter
from PIL import Image

import fraktale


class Gen_Win(customtkinter.CTk):
    def __init__(self, id):
        super().__init__()
        fractal = fraktale.Fractals[id]

        self.geometry("600x600")
        self.title("Fractal App")

        self.st = customtkinter.CTkLabel(self, text="STOPIEN", font=('Eras Bold ITC', 25), width=50)
        self.st.place(x=275, y=10)

        self.entry = customtkinter.CTkEntry(self,
                                            placeholder_text="1",
                                            width=120,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        self.entry.insert(0, 1)
        self.entry.place(x=50, y=50)

        def slider_event(value):
            self.entry.delete(0, "end")
            self.entry.insert(0, str(round(value)))

        def handle_return_key(event):
            try:
                if 0 > (n := int(self.entry.get())):
                    self.entry.delete(0, "end")
                    self.entry.insert(0, 1)
                    self.slider.set(0)
                elif 15 < n:
                    self.entry.delete(0, "end")
                    self.entry.insert(0, 15)
                    self.slider.set(15)
                else:
                    self.slider.set(n)
            except ValueError:
                self.entry.delete(0, "end")
                self.entry.insert(0, 1)
                self.slider.set(0)

        self.entry.bind("<Return>", handle_return_key)

        self.slider = customtkinter.CTkSlider(self, from_=1, to=15, command=slider_event, width=350)
        self.slider.set(1)
        self.slider.place(x=200, y=54)

        self.st2 = customtkinter.CTkLabel(self, text="DLUGOSC", font=('Eras Bold ITC', 25), width=50)
        self.st2.place(x=275, y=110)

        self.entry2 = customtkinter.CTkEntry(self,
                                             placeholder_text="0",
                                             width=120,
                                             height=25,
                                             border_width=2,
                                             corner_radius=10)
        self.entry2.insert(0, 1)
        self.entry2.place(x=50, y=150)

        def slider_event2(value):
            self.entry2.delete(0, "end")
            self.entry2.insert(0, str(round(value)))

        def handle_return_key2(event):
            try:
                if 0 > (n := int(self.entry2.get())):
                    self.entry2.delete(0, "end")
                    self.entry2.insert(0, 1)
                    self.slider2.set(1)
                elif 1000 < n:
                    self.entry2.delete(0, "end")
                    self.entry2.insert(0, 1000)
                    self.slider2.set(1000)
                else:
                    self.slider2.set(n)
            except ValueError:
                self.entry2.delete(0, "end")
                self.entry2.insert(0, 1)
                self.slider2.set(1)

        self.entry2.bind("<Return>", handle_return_key2)

        self.slider2 = customtkinter.CTkSlider(self, from_=1, to=1000, command=slider_event2, width=350)
        self.slider2.set(1)
        self.slider2.place(x=200, y=154)

        def confirm():
            st, length, animation = int(self.entry.get()), int(self.entry2.get()), self.switch_var.get()
            if self.switch_var2.get() == "True":
                if id != 24:
                    st, length = fractal.check_limit(st, length)
            fractal.draw(st, length, animation, self)

        self.button = customtkinter.CTkButton(self, width=100, height=50, corner_radius=8, text="CONFIRM",
                                              command=confirm)
        self.button.place(y=520, x=250)

        self.switch_var = customtkinter.StringVar(value="False")

        switch_1 = customtkinter.CTkSwitch(self, text="Animacja",
                                           variable=self.switch_var, onvalue="True", offvalue="False")
        switch_1.place(x=70, y=535)

        self.switch_var2 = customtkinter.StringVar(value="True")

        switch_2 = customtkinter.CTkSwitch(self, text="Koretktor",
                                           variable=self.switch_var2, onvalue="True", offvalue="False")
        switch_2.place(x=430, y=535)

        my_image = customtkinter.CTkImage(dark_image=Image.open(fractal.photo), size=(500, 300))

        button = customtkinter.CTkLabel(self, image=my_image, text="")
        button.place(x=50, y=200)

        warning = customtkinter.CTkLabel(self, text="! Brak animacji moze spowodowac braki w rysunku !", width=100,
                                         text_color="red", font=('Eras Bold ITC', 12))
        warning.place(x=150, y=570)
