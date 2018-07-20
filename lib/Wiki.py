import bpy
import subprocess

class Wiki(bpy.types.Operator):
	"""Connect lazypic wiki"""
	bl_idname = "lazypic.wiki"
	bl_label = "wiki"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		wiki = "https://github.com/lazypic/blender/wiki"
		stdout = subprocess.check_output(["open",wiki])
		print(stdout)
		return {'FINISHED'}
