import bpy

# Delete all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Import the model in FBX format
bpy.ops.import_scene.fbx(filepath="/path/to/model.fbx")
imported_object = bpy.context.selected_objects[0]
imported_object.location = (0, 0, 0)
imported_object.rotation_euler = (0, 0, 0)
imported_object.scale = (4, 4, 4)

# Add a camera
bpy.ops.object.camera_add(location=(0, -50, 0), rotation=(3.14 / 2, 0, 0))
bpy.context.scene.camera = bpy.context.active_object

# Add a light
bpy.ops.object.light_add(type='SUN', location=(0, 0, 0), rotation=(0, 0, 0))

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
tex_node.image = bpy.data.images.load("/path/to/background.png")
links.new(tex_node.outputs["Color"], emit_node.inputs["Color"])
links.new(emit_node.outputs["Emission"], out_node.inputs["Surface"])
plane.data.materials.append(mat)

# Render image
bpy.context.scene.render.resolution_x = 256
bpy.context.scene.render.resolution_y = 256
bpy.context.scene.render.filepath = "/path/to/render.png"
bpy.ops.render.render(write_still=True)

# Remove orphan data
for block in bpy.data.meshes:
    if block.users == 0:
        bpy.data.meshes.remove(block)
for block in bpy.data.materials:
    if block.users == 0:
        bpy.data.materials.remove(block)
for block in bpy.data.images:
    if block.users == 0:
        bpy.data.images.remove(block)