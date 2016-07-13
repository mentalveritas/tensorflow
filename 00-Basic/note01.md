# TensorFlow의 기본

## 00-helloworld.py
- Tensorflow를 tf로 import한다.
- constant함수(function)로 hello라는 변수(variable)을 생성
- 텐서플로우의 세션을 시작한다 sess = tf.Session()
- 텐서플로우는 모든것이 오퍼레이션이다.
- hello 변수를 상수가 아닌 오퍼레이터(node)라고 생각해야 한다.
- node를 실제로 구동 하는 것은 sess.run 부분이다.

## placeholder란?
- 변수를 할당만 하고, 해당 변수의 데이터 값은 세션이 구동될 때 입력해 주는 방식(함수의 파라미터와 비슷함)
- 대량의 데이터를 순차적으로 받아오거나, 노드의 연쇄적인 산출값이 다음 노드의 입력값이 되는 경우 등 매우 유용한 기능.
