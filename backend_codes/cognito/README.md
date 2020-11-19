# Cognito

- Cognito란 AWS에서 제공해주는 사용자 인증, 회원 관리 풀 서비스

- Cognito 유저 풀 기반 인가.

1. Application은 자신의 id, password를 통해 Cognito 서비스를 향해 Authenticating Chanllenge (인증 시도)를 한다.
2. 인증에 성공하면 코그니토 서비스에서 JWT 토큰을 반환한다.
3. 어플리케이션은 반환받은 JWT 토큰을 이용하여 API를 호출한다.
4. AWS는 헤더에 담긴 JWT토큰을 확인해보고, 인증 받은 토큰이라면 Lambda Invoke 혹은 VTL Resolver(Appsync)를 호출하여, DB에 엑세스한다.
5. 어플리케이션은 DB에서 리턴받은 값을 서비스에 활용한다.


## deploy with serverless 
