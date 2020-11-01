# front - backend 소통 내용

- 2020-11-01
    - 실제 사용할 데이터 포맷 정의 완료 (mqtt)

```json
{
    "deviceId" : "test-group",
    "payload" : {
        "numberData" : {
            "data" : [
                1,
                2
            ],
            "field" :[
                "speed",
                "rpm"
            ]
        },
        "errorCode" : {
            "data" : [
                1,
                0
            ],
            "field" : [
                "engine",
                "tire"
            ]
        },
        "timestamp" : "16042123124214.12421"
    }
}
```