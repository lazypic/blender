import bpy
import os

class Wiki(bpy.types.Operator):
	"""Connect lazypic wiki"""
	bl_idname = "lazypic.wiki"
	bl_label = "wiki"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		os.system("open %s" % "https://www.gitbook.com/book/lazypic/blender/details")
		return {'FINISHED'}
