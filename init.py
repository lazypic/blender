#lazypic blender python setting file
#khw7096@gmail.com
import os
import sys
import bpy
import time
sys.path.append('%s/blenderset/lib' % (os.path.expanduser("~")))

#import custom python files.
from LazypicWiki import *
from LazypicInit import *

def register():
	bpy.utils.register_class(LazypicWiki)
	bpy.utils.register_class(LazypicInit)

def unregister():
	bpy.utils.unregister_class(LazypicWiki)


if __name__ == "__main__":
	register()
	print("===lazypic blender python setting loaded===")
