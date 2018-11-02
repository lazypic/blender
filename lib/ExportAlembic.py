import bpy
import os

class LazypicExportAbcMesh(bpy.types.Operator):
	bl_idname = "lazypic.export_abc_mesh"
	bl_label = "Mesh"
	
	def execute(self, context):
		blend_file_path = bpy.data.filepath
		if not blend_file_path:
			return {'CANCELLED'}
		obj = bpy.context.active_object
		if obj.type != "MESH":
			return {'CANCELLED'}
		directory = os.path.dirname(blend_file_path)+"/abc"
		# if no exists then make
		if not os.path.exists(directory):
			os.makedirs(directory)
		target_file = os.path.join(directory,'%s.abc' % obj.name)
		bpy.ops.wm.alembic_export(filepath=target_file, selected=True, face_sets=True) # for unreal
		return {'FINISHED'}

class LazypicExportAbcCard(bpy.types.Operator):
	bl_idname = "lazypic.export_abc_card"
	bl_label = "Card"
	
	def execute(self, context):
		blend_file_path = bpy.data.filepath
		if not blend_file_path:
			return {'CANCELLED'}
		obj = bpy.context.active_object
		if obj.type != "MESH":
			return {'CANCELLED'}
		directory = os.path.dirname(blend_file_path)+"/abc"
		# if no exists then make
		if not os.path.exists(directory):
			os.makedirs(directory)
		target_file = os.path.join(directory,'card.abc')
		bpy.ops.wm.alembic_export(filepath=target_file, selected=True, face_sets=True) # for unreal
		return {'FINISHED'}

class LazypicExportAbcCam(bpy.types.Operator):
	bl_idname = "lazypic.export_abc_cam"
	bl_label = "Cam"
	
	def execute(self, context):
		blend_file_path = bpy.data.filepath
		if not blend_file_path:
			return {'CANCELLED'}
		obj = bpy.context.active_object
		if obj.type != "CAMERA":
			return {'CANCELLED'}
		directory = os.path.dirname(blend_file_path)+"/abc"
		# if no exists then make
		if not os.path.exists(directory):
			os.makedirs(directory)
		target_file = os.path.join(directory,'cam.abc')
		bpy.ops.wm.alembic_export(filepath=target_file, selected=True, face_sets=True) # for unreal
		return {'FINISHED'}

class LazypicExportAbcProjectionCam(bpy.types.Operator):
	bl_idname = "lazypic.export_abc_projectioncam"
	bl_label = "ProjectionCam"
	
	def execute(self, context):
		blend_file_path = bpy.data.filepath
		if not blend_file_path:
			return {'CANCELLED'}
		obj = bpy.context.active_object
		if obj.type != "CAMERA":
			return {'CANCELLED'}
		directory = os.path.dirname(blend_file_path)+"/abc"
		# if no exists then make
		if not os.path.exists(directory):
			os.makedirs(directory)
		target_file = os.path.join(directory,'projectioncam.abc')
		bpy.ops.wm.alembic_export(filepath=target_file, selected=True, face_sets=True) # for unreal
		return {'FINISHED'}

class ExportAlembic(bpy.types.Panel):
	"""Creates a Panel in the scene context of the properties editor"""
	bl_label = "ABC Export"
	bl_idname = "SCENE_PT_layout"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "scene"

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		# Big render button
		row = layout.row()
		row.operator("lazypic.export_abc_mesh")
		row.operator("lazypic.export_abc_card")

		# Different sizes in a row
		row = layout.row()
		row.operator("lazypic.export_abc_cam")
		row.operator("lazypic.export_abc_projectioncam")

def register():
	bpy.utils.register_class(LazypicExportAbcCam)
	bpy.utils.register_class(LazypicExportAbcProjectionCam)
	bpy.utils.register_class(LazypicExportAbcMesh)
	bpy.utils.register_class(LazypicExportAbcCard)
	bpy.utils.register_class(ExportAlembic)


def unregister():
	bpy.utils.unregister_class(LazypicExportAbcCam)
	bpy.utils.unregister_class(LazypicExportAbcProjectionCam)
	bpy.utils.unregister_class(LazypicExportAbcMesh)
	bpy.utils.unregister_class(LazypicExportAbcCard)
	bpy.utils.unregister_class(ExportAlembic)


if __name__ == "__main__":
	register()
