import bpy
import os
from os.path import expanduser

class PreviewRender(bpy.types.Operator):
	"""lazypic auto preview rendering setting"""
	bl_idname = "lazypic.preview_render"
	bl_label = "preview_render"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		bfile = bpy.data.filepath
		if bfile == "":
			#find how to run dialog err window.
			print("need save")
			return {'FINISHED'}
		bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
		bpy.context.scene.render.filepath = self.ogvFilename()
		bpy.context.scene.render.use_stamp = True
		bpy.context.scene.render.use_stamp_lens = True
		bpy.context.scene.render.use_stamp_marker = True
		bpy.context.scene.render.use_stamp_sequencer_strip = True
		bpy.context.scene.render.resolution_percentage = 100
		bpy.ops.render.opengl(animation=True)
		return {'FINISHED'}

	def ogvFilename(self):
		name = os.path.splitext(bpy.data.filepath)[0]
		return name + ".ogv"
