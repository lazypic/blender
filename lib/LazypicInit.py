import bpy
import os

class LazypicInit(bpy.types.Operator):
	"""lazypic init scene"""
	bl_idname = "lazypic.init"
	bl_label = "lazypic_init"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
		bpy.context.scene.render.filepath = "//render_out"
		bpy.context.scene.render.engine = 'CYCLES'
		return {'FINISHED'}
