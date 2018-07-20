#lazypic blender python setting file
#khw7096@gmail.com
import os
import sys
import bpy
import time
sys.path.append('%s/blender/lib' % (os.path.expanduser("~")))

#import custom python files.
from Wiki import *
from Init import *
from PreviewRender import *

def register():
	bpy.utils.register_class(Wiki)
	bpy.utils.register_class(Init)
	bpy.utils.register_class(PreviewRender)

if __name__ == "__main__":
	register()
