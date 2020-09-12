# 산기대 졸업작품 팀 레포지토리

* 디렉터리 구성
```
/
front_codes
    - react-app
    README.md
backend_codes
    - platfrom code
    REAMDE.md
```

- master branch에서 각자 브랜치를 따서 작업한다.
    - 브랜치 컨벤션 : {내용}/{부분}/{세부내용}
    - 내용에는 총 4가지가 있다. feature , bugfix, hotfix, enhancement
    - 예제 : feature/front/add-react-app
    - 예제 : feature/back/fix-aws-resources

- 본인의 작업이 완료 되면 본인 브랜치에 Push 하고 PR을 작성한다.
```
git bracnh feature/back/fix-aws-resources
git checkout feature/back/fix-aws-resources
git pull origin master --rebaswe
- 본인의 작업 실시 -
- 완료 되었을 경우-
git add *
git commit -m "add some vaildation logic"
git push origin feature/back/fix-aws-resources
- 이후 깃헙에 들어가서 PR 작성 및 리뷰 리퀘스트 -
```

- 팀장(김세환)의 Review를 받고 PR 머지를 한다.


## 사용 기술 스택

1. AWS 
    - DynamoDB
    - RDS(Postgresql)
    - Lambda
    - GreenGrass
    - Appsync
    - GraphQL
    - Amplify
    - S3
    - CloudWatch

2. Front
    - React.js
    - Material UI
    - D3.js
    - webpack
    - yarn
    - npm

3. DevOps
    - Jenkins
    - Serverless(with AWS)
    - Docker(Greengrass Deploy)

