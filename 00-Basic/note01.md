#1 TensorFlow의 기본

#2 00-helloworld.py
- Tensorflow를 tf로 import한다.
- constant함수(function)로 hello라는 변수(variable)을 생성
- 텐서플로우의 세션을 시작한다 sess = tf.Session()
- 텐서플로우는 모든것이 오퍼레이션이다.
- hello 변수를 상수가 아닌 오퍼레이터(node)라고 생각해야 한다.
- node를 실제로 구동 하는 것은 sess.run 부분이다.
