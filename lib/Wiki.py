import bpy
import os

class Wiki(bpy.types.Operator):
	"""Connect lazypic wiki"""
	bl_idname = "lazypic.wiki"
	bl_label = "lazypic_wiki"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		os.system("open %s" % "https://sites.google.com/site/lazypicweb/")
		return {'FINISHED'}
