# CSS의 개념
## [1] CSS 문법
### (1) 선택자(Selector)
선택자로 지정한 다음 중괄호 (`{` , `}`)를 통해 선언문들을 감싸게 되며, 각 선언문은 세미콜론(`;`)으로 종결

1. 전체선택자 (지양함)
  - `*`를 활용해 모든 요소를 지정
  - `<body>`안의 태그뿐만 아니라 `<head>`태그의 요소도 모두 선택하게 됨
    ```css
    * {
      color:red;
    }
    ```

2. 요소 선택자
  - 개별 태그를 선택
    ```css
    h1 {
      color : blue;
    }
    ```

3. 클래스 선택자 (제일 많이 사용)
  - `.`을 이용하여 특정 class가 적용된 요소를 선택
  
    ```html
    <span class="my_class">Learn</span>
    <span>HTML</span>
    <span class="my_class">CSS</span>
    ```
    ```css
    .my_class {
      color: green;
    }
    ```
4. 아이디 선택자
  - `#`을 이용하여 특정 id의 요소를 선택
  
5. 속성 선택자 (실무에서 잘 사용 안함)
  - 대괄호(`[` ,`]`)안에 속성을 특정하여 선택 
    ```css
    a[href="https://google.com"] {
      color: yellowgreen;
    }
    ```

### (2) 선언
- 속성과 값의 연결은 콜론(`:`)이며, `=`을 쓰지 않도록 주의

## [2] CSS 적용 방법
- html태그 안에 직접 css구문을 작성하는건 추천하지 않음 

- 보통 외부참조 사용 
