# 산기대 졸업작품 팀 레포지토리

url : http://sehwan96.com.s3-website.ap-northeast-2.amazonaws.com/


* 디렉터리 구성
```
/
front_codes
    - react-app
    README.md
backend_codes
    - platfrom code
    REAMDE.md
test_codes
    - 테스트 디렉터리들
```

- master branch에서 각자 브랜치를 따서 작업한다.
    - 브랜치 컨벤션 : {내용}/{부분}/{세부내용}
    - 내용에는 총 4가지가 있다. feature , bugfix, hotfix, enhancement
    - 예제 : feature/front/add-react-app
    - 예제 : feature/back/fix-aws-resources

- 본인의 작업이 완료 되면 본인 브랜치에 Push 하고 PR을 작성한다.
```
git branch feature/back/fix-aws-resources
git checkout feature/back/fix-aws-resources
git pull origin master --rebase
- 본인의 작업 실시 -
- 완료 되었을 경우-
git add *
git commit -m "add some validation logic"
git push origin feature/back/fix-aws-resources
- 이후 깃헙에 들어가서 PR 작성 및 리뷰 리퀘스트 -
```

- 팀장(김세환)의 Review를 받고 PR 머지를 한다.

## 배포

- front code는 github action 을 이용해 deploy (master 브랜치에 푸시 이벤트 발생 시 마다 S3버킷에 업로드 함)

```yml

name: React build
on: 
  push:                               # master Branch에서 push 이벤트가 일어났을 때만 실행
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-18.04
    steps:
      - name: Checkout source code.   # 레포지토리 체크아웃
        uses: actions/checkout@master

      - name: Cache node modules      # node modules 캐싱
        uses: actions/cache@v1
        with:
          path: front_codes/my-app/node_modules
          key: ${{ runner.OS }}-build-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.OS }}-build-
            ${{ runner.OS }}-
            
      - name: Display the path
        run: pwd && ls

      - name: change directory # 디렉터리 이동
        run: cd front_codes/my-app

      - name: Install Dependencies    # 의존 파일 설치
        run: cd front_codes/my-app && npm install

      - name: Build                   # React Build
        run: cd front_codes/my-app && npm run build

      - name: Deploy                  # S3에 배포하기
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: |
          aws s3 cp \
            --recursive \
            --region ap-northeast-2 \
            front_codes/my-app/build s3://sehwan96.com # 

```

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

