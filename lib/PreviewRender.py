import bpy
import os
from os.path import expanduser

class PreviewRender(bpy.types.Operator):
	"""lazypic auto preview rendering setting"""
	bl_idname = "preview_render"
	bl_label = "preview_render"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bfile = bpy.data.filepath
		if bfile != "":
			bpy.context.scene.render.image_settings.file_format = 'THEORA'
			bpy.context.scene.render.filepath = "%s.ogg" % (bfile.split(".blend")[0])
			bpy.context.scene.render.use_stamp = True
			bpy.context.scene.render.resolution_x = 1280
			bpy.context.scene.render.resolution_y = 720
			bpy.context.scene.render.resolution_percentage = 100
			bpy.ops.render.opengl(animation=True)
			return {'FINISHED'}
		else:
			#find how to run dialog err window.
			print("need save")
			return {'FINISHED'}
