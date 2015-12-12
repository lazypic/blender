import bpy
import os
from os.path import expanduser

class LazypicPreviewRender(bpy.types.Operator):
	"""lazypic auto preview rendering setting"""
	bl_idname = "lazypic.preview_render"
	bl_label = "lazypic_preview_render"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.context.scene.render.image_settings.file_format = 'THEORA'
		bpy.context.scene.render.filepath = "%s.ogg" % (bpy.data.filepath.split(".blend")[0])
		bpy.context.scene.render.use_stamp = True
		bpy.context.scene.render.resolution_x = 1280
		bpy.context.scene.render.resolution_y = 720
		bpy.context.scene.render.resolution_percentage = 100
		bpy.ops.render.opengl(animation=True)
		return {'FINISHED'}
