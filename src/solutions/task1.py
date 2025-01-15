import bpy
from random import uniform, choice

FOLDER_PATH = "/path/to/output/"

MAX_LOC = 8
MAX_ROT = 2
PI = 3.14

NUM_CUBES = 10
NUM_IMAGES = 20
RESOLUTION = 150

COLORS = {
    'r': (1, 0, 0, 1),
    'g': (0, 1, 0, 1),
    'b': (0, 0, 1, 1)
}

def get_color():
    name = choice(['r', 'g', 'b'])
    return name, COLORS[name]

for i in range(NUM_IMAGES):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    gt = {'r': 0, 'g': 0, 'b': 0}

    for _ in range(NUM_CUBES):
        bpy.ops.mesh.primitive_cube_add(
            location=(
                uniform(-MAX_LOC, MAX_LOC), uniform(-MAX_LOC, MAX_LOC), uniform(-MAX_LOC, MAX_LOC)
            ),
            rotation=(
                uniform(-MAX_ROT, MAX_ROT), uniform(-MAX_ROT, MAX_ROT), uniform(-MAX_ROT, MAX_ROT)
            )
        )
        cube = bpy.context.active_object

        cube.active_material = bpy.data.materials.new(name="MaterialName")
        name, color = get_color()
        gt[name] += 1
        cube.active_material.diffuse_color = color

    bpy.ops.object.camera_add(location=(0, -50, 0), rotation=(PI / 2, 0, 0))
    bpy.context.scene.camera = bpy.context.active_object

    bpy.ops.object.light_add(type='SUN')

    bpy.context.scene.render.resolution_x = RESOLUTION
    bpy.context.scene.render.resolution_y = RESOLUTION
    bpy.context.scene.render.filepath = f'{FOLDER_PATH}/{i}_{gt["r"]}_{gt["g"]}_{gt["b"]}.png'
    bpy.ops.render.render(write_still=True)