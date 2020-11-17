# 프로젝트를 위한 개발 Study
## 1. 로컬 저장소 (local storage)
-  상태 유지를 하려면 어찌할까?
 + 백엔드 어플리케이션을 사용하여 DB에 저장한다
> 더 간단하지만 대부분의 경우 더 충분한 솔루션은  
브라우저의 기본 로컬 저장소를 사용하는 것

### 1.1 로컬 저장소 소개
- 로컬 저장소에 데이터를 저장하고 검색하려면  
setter & getter 가 있는 인스턴스에 엑세스해야 함
```js
// 세터
localStorage.setItem('myData', 데이터);
// 게터
localStorage.getItem('myData');
// 제거
localStorage.removeItem('myData');
// 모두 제거
localStorage.clear();
```
- 첫 번째 인수는 데이터를 저장 / 검색하는 키 
- 두 번째 인수는 데이터를 저장할 때 실제 데이터
- 브라우저를 닫고 Application 다시 열면 데이터가  
여전히 로컬 저장소에 존재함

### 1.2 React의 로컬 저장소
```js
import React from 'react';

const useStateWithLocalStorage = localStorageKey => {
    const [value, setValue] = useState(
        localStorage.getItem(localStorageKey) || ''
    );
    useEffect(() => {
        localStorage.setItem(localStorageKey, value);
    }, [value]);

    return [value, setValue];
};

const App = () => {
    const [value, setValue] = useStateWithLocalStorage(
        'userId'
    );
    const onChange = e => setValue(e.target.value);
    return (
        <div>
            <h1>Hello React with Local Storage !</h1 >
            <input value={value} type="text" onChange={onChange}  />
            <p> {value} </p>
        </div>
    );
};
export default App;
```

### 1.3 React에서 데이터를 캐시하는 방법
- 로컬 스토리지 사용량을 한 단계 더 발전시켜 보자
- 원격 API에서 데이터를 가져와 구상요소의 상태에 저장
  
- 로컬 저장소에도 저장 이후 다른 검색 요청을 할 때마다  
로컬 저장소를 캐시로 사용함
- 키워드 검색했는데 이 키워드애 대한 결과가 이미  
로컬 저장소에 저장되어있는 경우 다른 API 호출을 실행하는  
대신 로컬 저장소를 사용함. 로컬 저장소에 결과가 없으면  
일반적인 API 요청을 수행함

