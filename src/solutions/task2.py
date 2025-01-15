import bpy
import random
import os

for i in range(30):

    # Delete all objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Import the model in FBX format
    models_path = "/path/to/models/"
    animal = random.choice(["giraffe", "zebra", "lion"])
    for _ in range(random.randint(1,4)):
        bpy.ops.import_scene.fbx(filepath=models_path + animal + ".fbx")
        
        # Randomize the imported object
        imported_object = bpy.context.selected_objects[0]
        imported_object.location = (random.uniform(-12,12), random.uniform(-12,12), random.uniform(-12,12))
        imported_object.rotation_euler = (random.uniform(-1.7,-1), random.uniform(-0.5,0.5), random.uniform(-2,2))
        scale = random.uniform(7,9)
        if animal == "giraffe":
            scale -=4
        imported_object.scale = (scale, scale, scale)

    # Add a camera
    bpy.ops.object.camera_add(location=(0, -50, 0), rotation=(3.14 / 2, 0, 0))
    bpy.context.scene.camera = bpy.context.active_object
    #bpy.context.scene.camera.data.lens = 18

    # Add a light
    for _ in range(4):
        bpy.ops.object.light_add(type='SUN', location=(0, 0, 0), rotation=(random.uniform(-2,2),random.uniform(-2,2),random.uniform(-2,2)))

    # Background plane
    bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 60, 0), rotation=(3.14/2, 0, 0))
    plane = bpy.context.active_object
    plane.scale = (120, 120, 120)
    mat = bpy.data.materials.new("BGMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    for node in nodes:
        nodes.remove(node)
    tex_node = nodes.new("ShaderNodeTexImage")
    emit_node = nodes.new("ShaderNodeEmission")
    out_node = nodes.new("ShaderNodeOutputMaterial")
    bgs_base_path = "/path/to/backgrounds/"
    bgs_paths = os.listdir(bgs_base_path)
    bg_path = random.choice(bgs_paths)
    tex_node.image = bpy.data.images.load(bgs_base_path + bg_path)
    links.new(tex_node.outputs["Color"], emit_node.inputs["Color"])
    links.new(emit_node.outputs["Emission"], out_node.inputs["Surface"])
    plane.data.materials.append(mat)

    # Render image
    bpy.context.scene.render.resolution_x = 256
    bpy.context.scene.render.resolution_y = 256
    bpy.context.scene.render.filepath = f"/path/to/output/{str(i).zfill(4)}_{animal}.png"
    bpy.ops.render.render(write_still=True)
