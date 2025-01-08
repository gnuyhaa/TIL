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

## [2] CSS 텍스트 속성
### (1) 폰트
1. font-size : 글꼴의 크기
2. font-weight : 글꼴의 두께
3. font-family : 글꼴의 종류
4. line-height : 줄의 높이
5. letter-spacing : 자간 결정 
6. font : 폰트 속성을 모두 포함하는 단축 속성
7. text-align : 텍스트 정렬

### (2) 단위
1. px
2. em
3. rem
4. %
5. viewport

### (3) 색상
1. color
2. background-color

## [3] CSS 상속
| <상속 가능 속성> | <상속 불가능 속성> |
| -- | -- |
| font (font-size, weight, style, family) | width & height |
| color | margin & padding |
| line-height | display |
| text-align | position |
| visibility | border |
| opacity | box-sizing |
|   | background |

### (1) 강제 상속
> inherit 속성을 사용해 상속되지 않는 요소를 강제로 상속할 수 있다.
```html
<div class="parent">
  부모
  <div class="child">자식</div>
</div>
```
```css
.parent {
      color: royalblue;
      border: 1px solid black;
      padding: 1px;
}

.child {
      border: inherit;
}
```
### (2) CSS 적용 우선순위
1. `!important` 
2. `inline style`
3. `id 선택자`
4. `class 선택자`
5. `요소 선택자`
6. `소스 순서`

### (3) 명시도
> 명시도 공식

```css
/* 명시도 예제 */
/* 1 element : 0-0-1 */
h1 { property : value}

/* 1 class Selector 0-1-0 */
.example { property : value}

/* 1 id Selector 1-0-0 */
#example { property : value}

/* 1 element & 1 attribute 0-1-1 */
input[type=email] { property : value}

/* 1 id & 1 class & 1 element 1-1-1 */
#example .example a { property : value}
```
> 명시도 예시
> 
아래 예시에서 같은 `input`의 스타일을 변경하려고 하지만 명시도 공식에 따라 blue 색상이 적용되게 되었음

```html
<div id="container">
  <label for="name">이름 :</label>
  <input type="text" class="textInput">
</div>
```
```css
#container .textInput {
    background-color: blue;
}

input {
    background-color: red;
}
```
## [4] 선택자 
### (1) 복합 선택자 
1. 일치 선택자 
    > 태그와 해당하는 클래스, 아이디가 `공백 없이` 이어지며 두 조건이 모두 만족되었을 경우만 선택

2. 자식 선택자
    > `>`으로 구분

3. 자손 선택자
    > `공백`으로 구분 
    ```css
    section > p {
          color: royalblue;
    }

    section p {
          border: 1px solid black;
    }
    ```

4. 형제 선택자 
    ```html
    <section>
      <p class="first">1</p>
      <p class="second">2</p>
      <p class="third">3</p>
      <div>
        <p class="fourth">4</p>
      </div>
    </section>
    ```

    ```css
    .first + p { /*인접 형제 선택자*/
          color: royalblue;
    }

    .first ~ p { /*일반 형제 선택자*/
          border: 1px solid black;
    }
    ```

### (2) 가상 클래스
💡`:`으로 시작하는 선택자

1. 링크 선택자
    > `<a>`태그에 적용하는 선택자

    ```html
    <a href="https://www.urlexample.com">이동하기</a>
    <a href="https://www.naver.com">이동하기</a>
    ```

    ```css
    a:link {
          color: royalblue
    }

    a:visited {
          color: green;
    }
    ```

    | `<a>` 태그의 상태 | 상세 설명 |
    | --- | --- |
    | :link | href 속성이 있는 `<a>`태그 선택 |
    | :visited | 방문했던 링크를 포함하는 `<a>`태그 선택 |

2. 반응 선택자

    > 사용자의 반응에 따라 특정 상태가 되면 선택합니다.
    > 

    ```html
    <p class="first">첫 번째</p>
    <p>두 번째</p>
    ```

    ```css
    p {
        border: 1px solid black;
    }

    .first:hover {
          background-color: aquamarine;
    }
    ```

    | 태그의 상태 | 상세 설명 |
    | --- | --- |
    | :hover | 마우스 커서를 올리면 선택 |
    | :active | 클릭하면 선택 |

    <aside>
    💡 마우스 오버 시 마우스 커서의 모양을 손가락 모양으로 바꿔 요소가 클릭할 수 있는 요소라는 것을 명시적으로 나타내려면 `cursor: pointer;`를 지정할 수 있습니다.
    </aside>

3. 입력 상태 선택자

    > `<input>` 태그의 특정 상태가 만족되면 선택합니다.
    > 

    ```html
    <input class="username" type="text" placeholder="아이디를 입력하세요">
    ```

    ```css
    .username {
        border: 2px solid royalblue;
        outline: none;
        padding: 5px 10px;
    }

    .username:focus {
        border-color: green;
    }
    ```

    | `<input>` 태그의 상태 | 상세 설명 |
    | --- | --- |
    | :focus | 포커싱 되었을 때 선택 |
    | :checked | 체크박스에 체크가 되면 선택 |
    | :disabled | 비활성화 상태면 선택 |
    | :enabled | 활성화 상태면 선택 |

4. 구조 선택자

    > 특정 위치의 태그를 선택합니다.
    > 

    ```html
    <div class="Learn">
      <span>1</span>
      <span>2</span>
      <span>3</span>
      <span>4</span>
      <span>5</span>
    </div>
    ```

    ```css
          .Learn > span:nth-child(2n + 1) {
            color: royalblue;
          }

          .Learn > span:nth-of-type(5) {
            color: crimson;
          }
    ```

    | 지정 방식 | 상세 설명 |
    | --- | --- |
    | :first-child | 첫 번째 형제 선택 |
    | :last-child | 마지막 형제 선택 |
    | :nth-child(n) | 앞에서부터 수열로 형제 선택 |
    | :nth-last-child(n) | 뒤에서부터 수열로 형제 선택 |
    | :first-of-type | 형제들 중 첫번째로 등장하는 요소 선택 |
    | :last-of-type | 형제들 중 마지막으로 등장하는 요소 선택 |
    | :nth-of-type(n) | 앞에서부터 수열로 등장하는 요소 선택 |
    | :nth-last-of-type(n) | 뒤에서부터 수열로 등장하는 요소 선택 |

<aside>
💡 element:nth-child(n)과 element:nth-of-type(n) 차이

</aside>

> element:nth-child(n)
> 

부모의 모든 자식 요소(element)중, n 번째를 찾습니다.

부모의 n 번째 자식이 지정된 요소를 만족하는 경우에만 작성한 스타일이 적용됩니다.

> element:nth-of-type(n)
> 

부모의 자식 요소 중, 지정한 요소의 n 번째를 선택합니다.

다른 요소들은 무시하고 지정한 요소 중, n 번째를 찾습니다.


> 주의 : n으로 수열 공식을 활용하는 경우, n은 0부터 시작하는 양의 정수가 차례대로  들어가게 됩니다. 그냥 n을 활용하는 경우 0 번째부터 시작을 하긴 하지만, 0 번째 요소는 없으므로 선택되지 않습니다.


### (3) 가상 요소 선택자

💡 `::`으로 시작하는 선택자들입니다.


> 요소의 앞과 뒤의 가상의 inline 요소를 지정하는 선택자입니다.
> 

기본적으로 content 속성 없이는 눈에 보이지 않으며, block 스타일 지정을 해주면 높이와 너비를 설정할 수 있습니다.

```html
<p>HTML/CSS</p>
```

```css
p::before {
    content: 'Learn ';
}
```

| 종류 | 상세 설명 |
| --- | --- |
| ::before | 요소 좌측에 인라인 가상 요소 추가 |
| ::after | 요소 우측에 인라인 가상 요소 추가 |