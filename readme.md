# Face recognition

Simple app for face recognition

### dataset

```bash
curl -O http://vis-www.cs.umass.edu/lfw/lfw.tgz && tar -xzvf lfw.tgz
```

### run dockerfile with tensorflow 

```bash
docker build -t colemurray/medium-facenet-tutorial -f Dockerfile.gpu .
```

### install dlib’s face landmark predictor

```bash
curl -O http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
```

### link to original repository

https://github.com/ColeMurray/medium-facenet-tutorial/tree/add_alignment
