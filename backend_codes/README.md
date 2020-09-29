# 백엔드 코드 디렉터리 구조

* backend_codes
    - api
    - doc_of_greengrass
    - dynamodb
    - greengrasslambda
    - Lambda
    - provisioning
    - rds

* api 디렉터리는 api에 관련된 코드들 (rest api 혹은 graphql을 위한 람다나 및 serverless 파일이 있음)

* dynamodb 디렉터리는 우리가 사용할 dynamodb를 배포하기 위한 serverless 파일을 구성할까 고민중.

* greengrasslambda -> greengrass상에 올라갈 람다

* Lambda -> 미사용 디렉토리

* provisioning -> greengrass-provisioner를 사용하기 위한 디렉터리
    - functions (greengrasslambda/ 를 심볼릭 링크 한 상태)
    - deployments -> 배포시에 코드에 들어가는 환경변수 및 셋업 설정
    - ggp.sh -> ./ggp.sh {commands} 를 이용해 greengrass 소프트웨어 배포를 위한 부트스트랩 파일 및 배포를 가능하게 하는 쉘 스크립트
    - serverless.yml -> 확인해보기
    
