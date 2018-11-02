#lazypic blender python setting file
#khw7096@gmail.com
import os
import sys
import bpy
import time
sys.path.append("%s/lib" % os.path.dirname(__file__))

#import custom python files.
from Wiki import *
from Init import *
from PreviewRender import *
from ExportAlembic import *

def register():
	bpy.utils.register_class(Wiki)
	bpy.utils.register_class(Init)
	bpy.utils.register_class(PreviewRender)
	# Export Alembic for Nuke and Unreal
	bpy.utils.register_class(ExportAlembic)
	bpy.utils.register_class(LazypicExportAbcCam)
	bpy.utils.register_class(LazypicExportAbcProjectionCam)
	bpy.utils.register_class(LazypicExportAbcMesh)
	bpy.utils.register_class(LazypicExportAbcCard)

if __name__ == "__main__":
	register()
