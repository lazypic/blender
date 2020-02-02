import bpy

class AllRender(bpy.types.Operator):
	#lazypic all object restict rendering on
	bl_idname = "lazypic.allrender"
	bl_label = "allrender"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		for obj in bpy.context.scene.objects:
			obj.hide_render = obj.hide
		return {'FINISHED'}
