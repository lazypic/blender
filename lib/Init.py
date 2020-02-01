#coding:utf-8
import bpy
import os

class Init(bpy.types.Operator):
	"""lazypic init scene"""
	bl_idname = "lazypic.init"
	bl_label = "init"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
		bpy.context.scene.render.filepath = "//render_out"
		bpy.context.scene.render.engine = 'CYCLES'
		bpy.data.scenes["Scene"].cycles.shading_system = True # OSL Shader Enable
		bpy.data.scenes["Scene"].unit_settings.system = "METRIC" # default meter setting.

		# Python Editor setting
		bpy.context.space_data.show_line_numbers = True
		bpy.context.space_data.show_word_wrap = True
		bpy.context.space_data.show_syntax_highlight = True
		return {'FINISHED'}
