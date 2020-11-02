# aws 람다 연구

* event(호출 방식)

- http -> api 게이트웨이와 연결
- schedule -> cron 표현식에 맞게 주기적 호출

```python3

import boto3

lambda = boto3.client('lambda')

lmd.invoke(FunctionName=(호출할 람다 이름),
                InvocationType='Event', Payload=json.dumps({딕셔너리 -> 전달받은 람다가 events 인자들로 받을 수 있음}, use_decimal=True))

```



```yml
functions:
  functionTrigger:
    module: module_name
    handler: main.handler
    name: here_is_name
    events:
      - schedule: cron(0 * * * ? *)  # every 1 hours ?
      # cron(0/1 * * * ? *) -> every 1 mins.
```

서버리스에 추후에 람다 배포할때 주기적으로 실행되야 하는 람다는
events에 schedule: cron(표현식) 이렇게 넣어주면 주기적 호출이 가능하다.

예를들어 우리가 평균 값을 1시간, 1일, 1주일, 1달 단위로 내려고 할 때 유용하게 쓰일 듯.

1시간 단위 평균부터는 DynamoDB에 저장하는 걸로 하고, 

1분 단위로 저장되는 raw 데이터는 S3 bucket에 저장하는 것으로 구조를 짜보자.