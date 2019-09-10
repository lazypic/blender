### Blenderset
This Code is lazypic blender setting code.

#### Install Env
```
cd ~ && git clone https://github.com/lazypic/blender.git
```

#### Install Blender
아래 명령어를 이용해서 빠르게 블렌더를 설치할 수 있습니다.
클라우드 버킷 접근권한이 필요합니다. 일반적인 블랜더는 [Blender.org](https://blender.org) 에서 다운받으셔도 됩니다.
```bash
$ aws s3 sync s3://lazypic-app/$OSTYPE ~/app
```

- run
```bash
$ blender --python ~/blender/init.py
```

#### Download Blender
AWS S# 클라우드를 통해서 Blender를 다운로드 합니다.
```bash
$ aws s3 sync s3://lazypic-app/$OSTYPE/blender2.8 $HOME/app/blender2.8 --profile lazypic
```

#### Upload Blender
자신이 사용하는 버전을 클라우드에 업로드하는 명령어는 아래와 같습니다.

```
$ aws s3 sync $HOME/app/blender2.8 s3://lazypic-app/$OSTYPE/blender2.8 --profile lazypic
```

#### Reference
- https://blender.community/c/rightclickselect/
- Other Build Version: `https://blender.community/c/graphicall
