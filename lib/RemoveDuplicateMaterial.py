import bpy

class RemoveDuplicateMaterial(bpy.types.Operator):
    '''
    replace material with 3 characters at the end to material without number 
    ex) 'material.001' --> 'material' 
        'material.099' --> 'material'
    '''

    bl_idname = "lazypic.remove_duplicate_material"
    bl_label = "remove_duplicate_material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #make all material list 
        mat_list = [mat.name for mat in bpy.data.materials]

        #remove duplicate material name
        for obj in bpy.context.scene.objects:
            for objmat in obj.material_slots:
                if objmat.material.name[-3:].isnumeric():
                    # last 3 character are numbers 
                    if objmat.material.name[:-4] in mat_list:
                        #material without number exist
                        objmat.material=bpy.data.materials[objmat.material.name[:-4]]
                        #replace duplicated material to orign material
        #remove unused matrials
        for material in bpy.data.materials:
            if not material.users:
                bpy.data.materials.remove(material)
        return {'FINISHED'}

