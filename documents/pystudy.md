# Python으로 뭐하지?

[파이썬강의](https://github.com/studio2l/pystudy)를 듣고 난 후에 드는 생각은 "파이썬으로 뭐하지?" 일 것이다.
파이썬으론 참 다양한 것들을 할 수 있다. 웹 사이트를 만들 수도 있고, 게임을 만들 수도 빅 데이터를 분석할 수도 있다. 
하지만 막상 시작하려고 보면 막막함을 느끼게 된다. 
"대체 그 거대한 것들을 어떻게 혼자 짤 수 있을까?"
답은 혼자 짜지 않는다는 것이다. 
다른 프로그래머들이 짜놓은 라이브러리나 API를 이용하면 쉽고 빠르게 원하는 프로그램을 만들 수 있다. 

#Python으로 Blender제어하기 

파이썬으로 Blender를 제어하기 위해선 [Blender Python API](https://docs.blender.org/api/current/)를 이용한다. 

일단 Blender 2.8을 실행해보자.
Blender에서 python 코딩을 할 땐,  [Text Editor](https://docs.blender.org/manual/en/latest/editors/text_editor.html)를 사용한다. 

 New를 클릭해서 새로운 문서를 만들고, 아래 코드를 써보자.

 ```python
import bpy

mesh = bpy.ops.mesh.primitive_cube_add()
```
Run Script버튼을 누르면 커서 위치에 큐브가 하나 생성된다. 


