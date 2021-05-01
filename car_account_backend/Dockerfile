FROM node:14
#도커 이미지 내 작업 디렉터리 생성
WORKDIR /usr/src/app

#의존성 설치를 위한 패키지 파일 복사
COPY package*.json ./

#프로덕션 빌드
RUN npm ci --only=production

COPY . .
#.env 는 jenkins 에서 주입.

EXPOSE 3000

CMD ["node", "server.js"]
