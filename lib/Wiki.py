import bpy
import os

class Wiki(bpy.types.Operator):
	"""Connect lazypic wiki"""
	bl_idname = "wiki"
	bl_label = "wiki"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		os.system("open %s" % "https://sites.google.com/site/lazypicweb/")
		return {'FINISHED'}
