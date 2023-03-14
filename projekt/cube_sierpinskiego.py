from ursina import *
from ursina.shaders import basic_lighting_shader


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
    camera.rotation_x += held_keys["i"]
    camera.rotation_x -= held_keys["k"]
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
