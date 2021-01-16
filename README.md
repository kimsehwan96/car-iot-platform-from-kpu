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

- front code는 github action 을 이용해 자동을고 deploy 된다. (master 브랜치에 푸시 이벤트 발생 시 마다 S3버킷에 업로드 함)

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
    - React
    - Typescript
    - Material UI
    - webpack
    - yarn
    - npm
    - Firebase
    - Grafana
    - ContextAPI
    - Redux

3. DevOps
    - Jenkins
    - Serverless(with AWS)
    - Docker(Greengrass Deploy)



## 구글 Python Coding-Style 번역 (번역자 김세환)

원본 : https://google.github.io/styleguide/pyguide.html

### 1 Background
파이썬은 구글에서 매우 활발하게 메인으로써 사용되는 언어입니다. 이 스타일 가이드는 파이썬 코딩을 위한 해야 할 것과 하지 말아야 할 것을 나열했습니다.  

코딩 자동 포매팅이 정확히 되도록, Vim 을 위한 세팅파일을 만들었습니다.(Vim 유저에 해당) 

```Vim
" Copyright 2019 Google LLC
"
" Licensed under the Apache License, Version 2.0 (the "License");
" you may not use this file except in compliance with the License.
" You may obtain a copy of the License at
"
"    https://www.apache.org/licenses/LICENSE-2.0
"
" Unless required by applicable law or agreed to in writing, software
" distributed under the License is distributed on an "AS IS" BASIS,
" WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
" See the License for the specific language governing permissions and
" limitations under the License.

" Indent Python in the Google way.

setlocal indentexpr=GetGooglePythonIndent(v:lnum)

let s:maxoff = 50 " maximum number of lines to look backwards.

function GetGooglePythonIndent(lnum)

  " Indent inside parens.
  " Align with the open paren unless it is at the end of the line.
  " E.g.
  "   open_paren_not_at_EOL(100,
  "                         (200,
  "                          300),
  "                         400)
  "   open_paren_at_EOL(
  "       100, 200, 300, 400)
  call cursor(a:lnum, 1)
  let [par_line, par_col] = searchpairpos('(\|{\|\[', '', ')\|}\|\]', 'bW',
        \ "line('.') < " . (a:lnum - s:maxoff) . " ? dummy :"
        \ . " synIDattr(synID(line('.'), col('.'), 1), 'name')"
        \ . " =~ '\\(Comment\\|String\\)$'")
  if par_line > 0
    call cursor(par_line, 1)
    if par_col != col("$") - 1
      return par_col
    endif
  endif

  " Delegate the rest to the original function.
  return GetPythonIndent(a:lnum)

endfunction

let pyindent_nested_paren="&sw*2"
let pyindent_open_paren="&sw*2"
```

(우리는 쓰지 않을 것)  

## 2 파이썬 규칙

### 2.2 Imports

`import` 구문은 각각의 클래스나 함수들을 import 할 때 사용하는 것이 아니라, 

#### 정의
해당 모듀로부터 다른 모듈로 코드를 공유하기 위한 재사용가능한 메커니즘입니다.

#### 장점
네임스페이스 관리 규칙은 매우 간단합니다. 각 식별자의 소스는 직관적인 방식으로 표현됩니다. `x.Obj`는   

`Obj` 라는 객체가 x라는 모듈 안에 정의되어있음을 의미합니다.

#### 단점
모듈의 이름은 충돌 될 수 있습니다. 그리고 어떤 모듈들의 이름은 불편할 만큼 길 수 있습니다.


#### 권장
* `import x`는 패키지들과 모듈들을 임포트하는데 사용해야합니다
* `from x import y`는 `x`가 패키지 prefix이고, `y`가 모듈이름임을 의미하며, `y`모듈을 prefix 없이 사용하기 위해 사용합니다.
* `from x import y as z`는 `y`라는 모듈 이름이 여러개 일때 임포트해서 사용하기 위해서, 또는 y라는 모듈 이름이 불편할정도로 길 때 사용합니다.
* `import y as z`는 오직 `z`가 덜리 알려진 convention이 있을때만 사용합니다. (numpy를 np로, 혹은 pandas를 pd로)

예를들어 `sound.effects.echo`는 다음과 같이 Import 되어야 합니다.
```python3
from sound.effects import echo

echo.EchoFilter(input, output, delay=0.7, atten=4)
```

import 할 때 realtive name은 사용하지 않습니다. 모듈이 같은 패키지 안에 있더라도, 패키지 전체의 이름을 사용해 임포트 합니다.  

이는 의도치 않게 패키지를 두번 임포트하는 것을 방지 가능합니다.

### 2.3 packages
각 모듈을 모듈의 위치 전체 경로를 명시하여 Import 합니다.

#### 장점
개발자의 예상과 다르게 모듈 경로를 탐색해서 발생해서 일어나는
모듈의 이름들 혹은 잘못된 import로 인한 충돌을 방지 할 수 있습니다.

#### 단점
개발 할 때 패키지 계층을 수정함으로써 코드 배포를 어렵게 만듭니다. 하지만 현대 배포 프로세스에 있어서 문제는 아닙니다.

#### 권장
새로 개발된 코드들은 반드시 풀 패키지 경로를 명시해서 import 되어야 합니다.

YES:
```python3
# Reference absl.flags in code with the complete name (verbose).
import absl.flags
from doctor.who import jodie

FLAGS = absl.flags.FLAGS
```

```python3
# Reference flags in code with just the module name (common).
from absl import flags
from doctor.who import jodie

FLAGS = flags.FLAGS
```


NO:( 이 파일은 doctor/who 디렉터리 안에 있으며, jodie.py 파일도 이 경로 안에 있을때를 가정합니다)
```python3
# Unclear what module the author wanted and what will be imported.  The actual
# import behavior depends on external factors controlling sys.path.
# Which possible jodie module did the author intend to import?
import jodie
```

이렇게 명시하면 `sys.path` 경로를 찾아서 모듈을 임포트하기 때문에 문제가 안될 수 있지만, 환경에 따라서 안될 수 있습니다.
파이썬 패키지 import 프로세스는 우선 third-party 혹은 top-level 패키지 부터 찾고, 그 이후 local 패키지를 찾기 때문에,
`jodie.py`가 올바르게 import 되지 않을 수 있습니다.

### 2.4 예외(Exceptions)

예외는 파이썬에서 허용되지만, 예외처리는 반드시 유의해서 사용해야 합니다.

#### 정의
Exception은 일반적인 code flow 혹은 code control을 망가트리는 에러나 예외 조건들을 핸들하기 위해서 만들어졌습니다.

#### 장점
예외 처리 코드는 일반적인 코드 플로우, 프로세스를 예외가 발생했을때 망가지지 않게 하는 장점이 있습니다.

#### 단점
예외처리 코드는 일반적인 프로세스, 플로우를 헷갈리게 만들 수 있습니다. 라이브러리 호출을 할 때 발생하는 에러를 놓치기 쉽습니다.
(최대한 예외처리 코드 대신에 분기문을 사용하라고 하더라구,,)

#### 권장
Exceptions는 반드시 확실한 조건을 통해 사용합니다.
- 빌트인(내장) 예외는 정말 말이 될 때만 사용합니다. 예를들어 `ValueError`는 사전 조건을 통과하지 못한 값들에 대해서 발생시킵니다.(예를 들면 양수 값만 들어와야 하는데 -사전조건- 입력이 음수가 들어왔다면 `ValueError` 예외 발생).
- `assert`구문을 퍼블릭 API의 인자 체크를 위해서 사용하지 마세요. `assert` 구문은 내부적인 체크를 위해서 사용하는 것이지, 올바른 사용이나 예측치 못한 결과가 나온다는 것을 확인 시켜주려는 용도가 아니에요. 

```python3
Yes:
  def connect_to_next_port(self, minimum):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """
    if minimum < 1024:
      # Note that this raising of ValueError is not mentioned in the doc
      # string's "Raises:" section because it is not appropriate to
      # guarantee this specific behavioral reaction to API misuse.
      raise ValueError(f'Min. port must be at least 1024, not {minimum}.')
    port = self._find_next_open_port(minimum)
    if not port:
      raise ConnectionError(
          f'Could not connect to service on port {minimum} or higher.')
    assert port >= minimum, (
        f'Unexpected port {port} when minimum was {minimum}.')
    return port
```


```python3
  def connect_to_next_port(self, minimum):
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """
    assert minimum >= 1024, 'Minimum port must be at least 1024.'
    port = self._find_next_open_port(minimum)
    assert port is not None
    return port
```

추가 설명
- 인자로 받은 minimum 을 YES에서는 조건문으로 처리, 만약 올바르지 않은 경우 rasie Exception을 한다. assert 구문을 사용하지 않는다.

- 라이브러리나 패키지들은 자체 익셉션을 갖고 있다. 이 익셉션들은 기존 존재하는 익셉션을 상속받아 구현한 것
- 익셉션 이름의 끝은 반드시 `Error`로 끝나야 한다.
- 절대로 모든 예외를 잡기 위해 `except:` 구문을 사용하지 마세요. (`Exception`이나 `StandardError`)
- 만약 위처럼 사용하면, 오타나, 인터럽트, 시스템 종료 콜등 모든 예외를 잡게 되어서, 원하는 에러를 찾기 힘듭니다.
- `try/except` 구문 안의 블럭은 반드시 짧게 작성합니다. 그래야 개발자가 예측하지 않은 다른 예외까지 잡지 않습니다(각 디버깅 포인트마다 try, except 짧게 작성)
- `finally` 문장을 사용 권장 예외가 발생하지 않았을 때 처리하는 구문 사용 가능함. cleanup, closing file 등의 상황에서 유용하다.

### 전역 변수(Global variables)
사용하는 것을 자제

#### 2.5.1 정의
모듈 레벨 혹은 클래스 속성으로 정의 된 변수들

#### 장점
때떄로 유용함

#### 단점
import 하는 동안 원하는 동작이 아닌 다른 동작을 할 잠재성을 내포하고있음.
모듈이 임포트 될 때 전역변수 할당(assignment)가 되기 때문입니다.

#### 권장
최대한 전역변수 사용을 피한다.

다만 모듈 레벨의 상수는 허용 및 권장.
예를들어 `MAX_HOLY_HANDGRENADE_COUNT = 3` 과 같이 상수는 모두 대문자 및 언더스코어로 사용한다.

만약 사용 할 경우, 모듈 임포트 될 때 바로 할당 되어서 오동작을 막기 위해서
`_`를 앞에 붙여서 사용한다.


### 컴프리헨션 및 제너레이터 
간단한 케이스에 대해서 괜찮다

#### 정의
리스트, 딕셔너리, 셋 컴프리헨션은 제너레이터, 제너레이터 표현은 `map()`, `filter()`, `lambda`를 사용하지 않고 컨테니어 자료형이나 이터레이터를 만들 수 있기 때문에 유용

#### 장점
간단한 컴프리헨션은 리스트, 딕셔너리, 셋을 생성하는 로직을 좀 더 간단하고 명료하게 만들어 준다.
제너레이터 표현 또한 매우 유용하다.(굳이 리스트를 모두 만들지 않고 중간에 끊어도 되는 경우에 해당)

#### 단점
복잡한 컴프리 헨션과 제너레이터는 가독성이 떨어진다

#### 권장
간단한 케이스에 대해서만 사용한다. 복잡한 로직은 루프, 반복문 사용할 것

```python3

Yes:
  result = [mapping_expr for value in iterable if filter_expr]

  result = [{'key': value} for value in iterable
            if a_long_filter_expression(value)]

  result = [complicated_transform(x)
            for x in iterable if predicate(x)]

  descriptive_name = [
      transform({'key': key, 'value': value}, color='black')
      for key, value in generate_iterable(some_input)
      if complicated_condition_is_met(key, value)
  ]

  result = []
  for x in range(10):
      for y in range(5):
          if x * y > 10:
              result.append((x, y))

  return {x: complicated_transform(x)
          for x in long_generator_function(parameter)
          if x is not None}

  squares_generator = (x**2 for x in range(10))

  unique_names = {user.name for user in users if user is not None}

  eat(jelly_bean for jelly_bean in jelly_beans
      if jelly_bean.color == 'black')

```

```python3
No:
  result = [complicated_transform(
                x, some_argument=x+1)
            for x in iterable if predicate(x)]

  result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

  return ((x, y, z)
          for x in range(5)
          for y in range(5)
          if x != y
          for z in range(5)
          if y != z)
```

### 기본 이터레이터와 연산자
기본 이터레이터와 연산을 리스트, 딕셔너리, 파일에 사용하는 것

#### 정의
컨테이너 자료형 (리스트, 딕셔너리)에 정의 된 멤버십 테스트 연산자(in, not in) 및 이터레이터

#### 장점
기본 이터레이터와 연산은 매우 효율적이고 심플함.

#### 권장
```python3
Yes:  for key in adict: ...
      if key not in adict: ...
      if obj in alist: ...
      for line in afile: ...
      for k, v in adict.items(): ...
      for k, v in six.iteritems(adict): ...
```


```python3
No:   for key in adict.keys(): ...
      if not adict.has_key(key): ...
      for line in afile.readlines(): ...
      for k, v in dict.iteritems(): ...
```
