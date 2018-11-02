import bpy
import webbrowser

class Wiki(bpy.types.Operator):
	"""Connect lazypic wiki"""
	bl_idname = "lazypic.wiki"
	bl_label = "wiki"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		webbrowser.open("https://github.com/lazypic/blender/wiki")
		return {'FINISHED'}
