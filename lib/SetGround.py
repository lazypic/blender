import bpy
from mathutils import Vector
import bmesh

def origin_to_bottom(obj):
	mw = obj.matrix_world
	local_verts = [Vector(v[:]) for v in obj.bound_box]
	bm = bmesh.new()
	bm.from_mesh(obj.data)
	x, y, z = 0, 0, 0

	l = len(local_verts)
	z = min([v.z for v in local_verts])

	local_origin = Vector((x, y, z))
	global_origin = mw * local_origin

	for v in bm.verts:
		v.co = v.co - local_origin

	bm.to_mesh(obj.data)

	#move the mesh back
	mw.translation = global_origin

class SetGround(bpy.types.Operator):
	#lazypic asset setting- origin to bottom & move to 0,0,0
	bl_idname = "lazypic.set_ground"
	bl_label = "set_ground"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		#select active mesh 
		mesh_objs = [mo for mo in bpy.context.selected_objects if mo.type == 'MESH']
		#origin to center of geometry
		bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
		#origin to bottom & move to 0,0,0
		for o in mesh_objs:
			origin_to_bottom(o)
			o.location=(0,0,0)
		return {'FINISHED'}
