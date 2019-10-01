# 계단 만들기 
복습을 겸해서 계단을 만들어 봅시다. 
[계단만들기 유튜브 튜토리얼](https://youtu.be/ky2Mp5yDGDA)
```python
import bpy

for i in range(10):
    bpy.ops.mesh.primitive_cube_add(location=(0,i*2,i*2))
    bpy.ops.transform.resize(value=(10, 1, 1))
```


# math모듈 사용하기 

## sin, cos사용하기 

```python
import bpy
import math

a=range(1,20)

for i in a:
    mesh = bpy.ops.mesh.primitive_cube_add(size=0.5,location=(i,math.sin(i),math.cos(i)))
```
