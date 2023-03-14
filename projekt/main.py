import customtkinter
from PIL import Image
from ursina import *
from ursina.shaders import basic_lighting_shader

import test


class mem:
    def __init__(self):
        self.choose_id = 0
        self.save = {}
        self.guard = False


mem = mem()


class gen_win(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("Fractal App")

        self.radio_button_frame_1 = RadioButtonFrame(self)
        self.radio_button_frame_1.place(x=25, y=28)

        self.menu = 0

        self.tab_view = MyTabView(master=self, width=750)
        self.tab_view.place(x=280, y=10)
        self.tab_view1 = MyFrame3(master=self)
        self.tab_view2 = MyTabView1(master=self, width=750)

        self.generation = customtkinter.CTkButton(self, width=200, height=200, corner_radius=10, text="GENERUJ !",
                                                  fg_color="green", hover_color="darkgreen",
                                                  font=('Eras Bold ITC', 25))
        self.generation.place(x=35, y=310)

        self.choosen_option = None


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app = args[0]

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkButton(self, width=200, height=50, border_width=0, corner_radius=5,
                                                      text="2D", font=('Trebuchet MS', 18),
                                                      command=app.swap_to_0)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkButton(self, width=200, height=50, border_width=0, corner_radius=5,
                                                      text="3D", font=('Trebuchet MS', 18),
                                                      command=app.swap_to_1)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)
        self.radio_button_3 = customtkinter.CTkButton(self, width=200, height=50, border_width=0, corner_radius=5,
                                                      text="PRESET", font=('Trebuchet MS', 18),
                                                      command=app.swap_to_2)
        self.radio_button_3.grid(row=3, column=0, padx=10, pady=(10, 20))


class MyFrame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def swap_to_1():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label1.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 1

        def swap_to_2():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label2.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 2

        def swap_to_3():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label3.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 3

        def swap_to_4():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label4.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 4

        def swap_to_5():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label5.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 5

        def swap_to_6():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label6.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 6

        def swap_to_7():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label7.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 7

        def swap_to_8():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label8.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 8

        def swap_to_9():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label9.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 9

        def swap_to_10():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label10.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 10

        def swap_to_11():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label11.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 11

        def swap_to_12():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label12.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 12

        def swap_to_13():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label13.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 13

        def swap_to_14():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label14.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 14

        def swap_to_15():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label15.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 15

        self.label1 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0,
                                              text="TROJKAT\nSIERPINSKIEGO", command=swap_to_1,
                                              font=('Trebuchet MS', 15))
        self.label1.grid(row=0, column=0)
        self.label2 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="DYWAN\nSIERPINSKIEGO",
                                              command=swap_to_2,
                                              font=('Trebuchet MS', 15))
        self.label2.grid(row=0, column=1)
        self.label3 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="DRZEWKO\nBINARNE",
                                              command=swap_to_3,
                                              font=('Trebuchet MS', 15))
        self.label3.grid(row=0, column=2)
        self.label4 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="PLATEK\nKOCHA",
                                              command=swap_to_4,
                                              font=('Trebuchet MS', 15))
        self.label4.grid(row=0, column=3)
        self.label5 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="ZBIOR\nCANTORA",
                                              command=swap_to_5,
                                              font=('Trebuchet MS', 15))
        self.label5.grid(row=0, column=4)
        self.label6 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="KRZYWA\nLEVY’ego",
                                              command=swap_to_6,
                                              font=('Trebuchet MS', 15))
        self.label6.grid(row=1, column=0)
        self.label7 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="KRZYWA\nSMOCZA",
                                              command=swap_to_7,
                                              font=('Trebuchet MS', 15))
        self.label7.grid(row=1, column=1)
        self.label8 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="ROMB\nVICSEKA",
                                              command=swap_to_8,
                                              font=('Trebuchet MS', 15), text_color="orange")
        self.label8.grid(row=1, column=2)
        self.label9 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="KRZYWA\nHILBERTA",
                                              command=swap_to_9,
                                              font=('Trebuchet MS', 15))
        self.label9.grid(row=1, column=3)
        self.label10 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0,
                                               text="DANDELION\n''DMUCHAWIEC''", command=swap_to_10,
                                               font=('Trebuchet MS', 15))
        self.label10.grid(row=1, column=4)
        self.label11 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="PAPROC\nBARNSLEYA",
                                               command=swap_to_11,
                                               font=('Trebuchet MS', 15))
        self.label11.grid(row=2, column=0)
        self.label12 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="PENTA",
                                               command=swap_to_12,
                                               font=('Trebuchet MS', 15), text_color="orange")
        self.label12.grid(row=2, column=1)
        self.label13 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="REGRESS",
                                               command=swap_to_13,
                                               font=('Trebuchet MS', 15), text_color="orange")
        self.label13.grid(row=2, column=2)
        self.label14 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="KWADRAT",
                                               command=swap_to_14,
                                               font=('Trebuchet MS', 15))
        self.label14.grid(row=2, column=3)
        self.label15 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="HTREE",
                                               command=swap_to_15,
                                               font=('Trebuchet MS', 15))
        self.label15.grid(row=2, column=4)

        mem.save[1] = self.label1
        mem.save[2] = self.label2
        mem.save[3] = self.label3
        mem.save[4] = self.label4
        mem.save[5] = self.label5
        mem.save[6] = self.label6
        mem.save[7] = self.label7
        mem.save[8] = self.label8
        mem.save[9] = self.label9
        mem.save[10] = self.label10
        mem.save[11] = self.label11
        mem.save[12] = self.label12
        mem.save[13] = self.label13
        mem.save[14] = self.label14
        mem.save[15] = self.label15


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def swap_to_16():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label16.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 16

        def swap_to_17():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label17.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 17

        def swap_to_18():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label18.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 18

        def swap_to_19():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label19.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 19

        def swap_to_20():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label20.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 20

        self.label16 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="CIRCULAR\nINFINITY",
                                               command=swap_to_16,
                                               font=('Trebuchet MS', 15))
        self.label16.grid(row=0, column=0)
        self.label17 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="CIRCLE\nCROSS",
                                               command=swap_to_17,
                                               font=('Trebuchet MS', 15))
        self.label17.grid(row=0, column=1)
        self.label18 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="CIRCLE\nTRIANGLE",
                                               command=swap_to_18,
                                               font=('Trebuchet MS', 15))
        self.label18.grid(row=0, column=2)
        self.label19 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="PYTHAGORAS\nTREE",
                                               command=swap_to_19,
                                               font=('Trebuchet MS', 15))
        self.label19.grid(row=0, column=3)
        self.label20 = customtkinter.CTkButton(self, width=150, height=150, corner_radius=0, text="SPIRAL\nTRIANGLE",
                                               command=swap_to_20,
                                               font=('Trebuchet MS', 15))
        self.label20.grid(row=0, column=4)

        mem.save[16] = self.label16
        mem.save[17] = self.label17
        mem.save[18] = self.label18
        mem.save[19] = self.label19
        mem.save[20] = self.label20


class MyFrame3(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def swap_to_21():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label21.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 21

        my_image = customtkinter.CTkImage(dark_image=Image.open("textures/cube.png"), size=(750, 450))

        self.label21 = customtkinter.CTkButton(self, width=750, height=450, corner_radius=0, border_width=0,
                                               border_spacing=0, text="", image=my_image, command=swap_to_21)
        self.label21.grid(row=0, column=0)

        mem.save[21] = self.label21


class MyFrame4(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def swap_to_22():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label22.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 22

        def swap_to_23():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label23.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 23

        def swap_to_24():
            if mem.choose_id != 0:
                mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            self.label24.configure(border_color="yellow", fg_color="skyblue3", border_width=3)
            mem.choose_id = 24

        self.label22 = customtkinter.CTkButton(self, width=250, height=450, corner_radius=0, text="GRA W\nCHAOS",
                                               command=swap_to_22,
                                               font=('Trebuchet MS', 15))
        self.label22.grid(row=0, column=0)
        self.label23 = customtkinter.CTkButton(self, width=250, height=450, corner_radius=0, text="MANDELBROT",
                                               command=swap_to_23,
                                               font=('Trebuchet MS', 15))
        self.label23.grid(row=0, column=1)
        self.label24 = customtkinter.CTkButton(self, width=250, height=450, corner_radius=0, text="NENIO CIRCLE",
                                               command=swap_to_24,
                                               font=('Trebuchet MS', 15))
        self.label24.grid(row=0, column=2)

        mem.save[22] = self.label22
        mem.save[23] = self.label23
        mem.save[24] = self.label24


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Strona 1")
        self.add("Strona 2")

        self.tab("Strona 1").frame1 = customtkinter.CTkFrame(self.tab("Strona 1"))

        self.tab("Strona 1").grid_rowconfigure(0, weight=0)
        self.tab("Strona 1").grid_columnconfigure(0, weight=0)
        self.tab("Strona 1").grid_columnconfigure(1, weight=0)
        self.tab("Strona 1").grid_columnconfigure(2, weight=0)

        self.tab("Strona 1").my_frame = MyFrame1(self.tab("Strona 1"))
        self.tab("Strona 1").my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.tab("Strona 2").frame1 = customtkinter.CTkFrame(self.tab("Strona 2"))
        self.tab("Strona 2").grid_columnconfigure(0, weight=0)

        self.tab("Strona 2").my_frame = MyFrame2(self.tab("Strona 2"))
        self.tab("Strona 2").my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


class MyTabView1(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Strona 1")

        self.tab("Strona 1").frame1 = customtkinter.CTkFrame(self.tab("Strona 1"))

        self.tab("Strona 1").grid_rowconfigure(0, weight=0)
        self.tab("Strona 1").grid_columnconfigure(0, weight=0)

        self.tab("Strona 1").my_frame = MyFrame4(self.tab("Strona 1"))
        self.tab("Strona 1").my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1100x600")
        self.title("Fractal App")

        def generate():
            if mem.choose_id != 0:
                if mem.choose_id == 21:
                    mem.guard = True
                    app.destroy()
                app.destroy()
                gen_win2 = test.Gen_Win(mem.choose_id)
                gen_win2.mainloop()
            else:
                warning = customtkinter.CTkLabel(self, text="! Najpierw musisz wybrac co chcesz narysowac !",
                                                 text_color="red", width=100, font=('Eras Bold ITC', 15))
                warning.place(x=500, y=560)

        self.radio_button_frame_1 = RadioButtonFrame(self)
        self.radio_button_frame_1.place(x=25, y=28)

        self.menu = 0

        self.tab_view = MyTabView(master=self, width=750)
        self.tab_view.place(x=280, y=10)
        self.tab_view1 = MyFrame3(master=self)
        self.tab_view2 = MyTabView1(master=self, width=750)

        self.generation = customtkinter.CTkButton(self, width=200, height=200, corner_radius=10, text="GENERUJ !",
                                                  fg_color="green", hover_color="darkgreen",
                                                  font=('Eras Bold ITC', 25), command=generate)
        self.generation.place(x=35, y=310)

        self.choosen_option = None

    def clear_all(self):
        self.tab_view.place_forget()
        self.tab_view2.place_forget()
        self.tab_view1.place_forget()

    def swap_to_0(self):
        if mem.choose_id != 0:
            mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            mem.choose_id = 0
        if self.menu != 0:
            self.clear_all()
            self.menu = 0
            self.tab_view.place(x=280, y=10)

    def swap_to_1(self):
        if mem.choose_id != 0:
            mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            mem.choose_id = 0
        if self.menu != 1:
            self.clear_all()
            self.menu = 1
            self.tab_view1.place(x=305, y=70)

    def swap_to_2(self):
        if mem.choose_id != 0:
            mem.save[mem.choose_id].configure(fg_color="#1F6AA4", border_width=0)
            mem.choose_id = 0
        if self.menu != 2:
            self.clear_all()
            self.menu = 2
            self.tab_view2.place(x=280, y=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

if mem.guard:
    def cube_sierpinskiego(st, size, x=0, y=0, z=0):
        if st == 0:
            cube = Entity(model="cube", color=color.olive, texture="white_cube", scale=size, position=(x, y, z),
                          shader=basic_lighting_shader)
        else:
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y -= size / 3
            # -------------------------------------------
            x += size * 2 / 3
            z += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z -= size / 3
            # --------------------------------------------
            z += size * 2 / 3
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z -= size / 3
            y -= size * 2 / 3
            # ---------------------------------------------
            z += size * 2 / 3
            x += size * 2 / 3
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            x -= size / 3
            y -= size * 2 / 3
            z -= size * 2 / 3
            # ---------------------------------------------
            y += size * 2 / 3
            x += size * 2 / 3
            z += size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z += size / 3
            x -= size * 2 / 3
            z -= size * 2 / 3
            y -= size * 2 / 3
            # ---------------------------------------------
            x += size * 2 / 3
            z += size * 2 / 3
            y += size * 2 / 3
            z -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            z -= size / 3
            y -= size / 3
            cube_sierpinskiego(st - 1, size / 3, x, y, z)
            y -= size / 3
            x -= size * 2 / 3


    def camera_control():
        camera.z += held_keys["w"] * 10 * time.dt
        camera.z -= held_keys["s"] * 10 * time.dt
        camera.x += held_keys["d"] * 10 * time.dt
        camera.x -= held_keys["a"] * 10 * time.dt
        camera.y += held_keys["r"] * 10 * time.dt
        camera.y -= held_keys["e"] * 10 * time.dt
        camera.rotation_x += held_keys["k"]
        camera.rotation_x -= held_keys["i"]
        camera.rotation_y += held_keys["l"]
        camera.rotation_y -= held_keys["j"]


    def update():
        camera_control()


    def use():
        app = Ursina()
        pivot = Entity()
        DirectionalLight(parent=pivot, y=50, x=50, shadows=True)
        cube_sierpinskiego(3, 5, -1, -1, -1)
        app.run()


    use()
