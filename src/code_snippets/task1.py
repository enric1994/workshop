import bpy

# Delete all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Add a cube
bpy.ops.mesh.primitive_cube_add(location=(0,4,0), rotation=(0, 0, 0.7))
cube = bpy.context.active_object

# Add a material
cube.active_material = bpy.data.materials.new(name="MaterialName")
cube.active_material.diffuse_color = (1, 0, 0, 1)

# Add a camera
bpy.ops.object.camera_add(location=(0, -50, 0), rotation=(3.14 / 2, 0, 0))
bpy.context.scene.camera = bpy.context.active_object

# Add a light
bpy.ops.object.light_add(type='SUN')

# Render image
bpy.context.scene.render.resolution_x = 100
bpy.context.scene.render.resolution_y = 100
bpy.context.scene.render.filepath = '/path/to/render.png'
bpy.ops.render.render(write_still=True)

# Useful commands
import random
random.randint(0, 10) # Random integer between 0 and 10
random.uniform(-3, 3) # Random float between -3 and 3
random.choice(['red', 'green', 'blue']) # Random choice from the list