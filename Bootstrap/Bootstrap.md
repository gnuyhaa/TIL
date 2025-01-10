# Bootstrap 문법
## Spacing

### Margin & Padding

> 마진과 패딩을 손쉽게 지정할 수 있습니다.
> 

| 클래스명 | 상세 설명 |
| --- | --- |
| m | margin |
| p | padding |

### 방향

> 마진과 패딩의 방향을 설정할 수 있습니다.
> 

| 구분 | 상세 설명 |
| --- | --- |
| t | 위쪽 방향 지정 |
| b | 아래쪽 방향 지정 |
| s | 왼쪽 방향 지정 |
| e | 오른쪽 방향 지정 |
| x | x축 방향 동시 지정(왼쪽, 오른쪽) |
| y | y축 방향 동시 지정(위쪽, 아래쪽) |

### 단위

> 0~5까지의 단위가 가능합니다.
> 

| 범위 | 상세 설명 |
| --- | --- |
| 0 | 0rem, 0px |
| 1 | 0.25rem, 4px |
| 2 | 0.5rem, 8px |
| 3 | 1rem, 16px |
| 4 | 1.5rem, 24px |
| 5 | 3rem, 48px |

### 적용 예시

> my-2 : 위, 아래의 마진을 8px만큼 적용한다.
> 

```html
<p class="my-2">Learn</p>
<p class="my-2">HTML/CSS</p>
```

<aside>
💡 Boostrap margin, padding은 !important로 적용되어 있어, 일반적인 CSS와 병행하여 사용할 때 주의하여야 합니다.

</aside>

## Color

> Bootstrap이 미리 설정해둔 색상을 활용할 수 있습니다.
>
> 
```css
--bs-primary: #0d6efd;
--bs-secondary: #6c757d;
--bs-success: #198754;
--bs-info: #0dcaf0;
--bs-warning: #ffc107;
--bs-danger: #dc3545;
--bs-light: #f8f9fa;
--bs-dark: #212529;
```

> text, btn(button), bg(background)와 함께 쓸 수 있습니다.
> 

```html
<p class="text-primary">Learn</p>
<button class="btn btn-success">HTML</button>
<p class="bg-warning">CSS</p>
```

## Display

### Block & Inline

> Display를 변경할 수 있습니다.
> 

| 클래스명 | 상세 설명 |
| --- | --- |
| d-block | display: block; |
| d-inline | display: inline; |
| d-none | display: none; |

```html
<div class="d-inline">Learn</div>
<div class="d-inline">HTML/CSS</div>
```
### Flex

> Flexbox 관련 설정을 할 수 있습니다.
> 

| 클래스명 | 상세 설명 |
| --- | --- |
| d-flex | display flex 설정 |
| justify-content-{위치} | start, end, center, between, around, evenly 조정 |
| align-items-{위치} | start, end, center, baseline, stretch 조정 |
| flex-row | flex direction row 설정 |
| flex-row-reverse | flex direction row-reverse 설정 |
| flex-column | flex direction column 설정 |
| flex-column-reverse | flex direction column-reverse 설정 |

### 예시

> Display & Flexbox를 이용해 손쉽게 레이아웃을 할 수 있습니다.
> 

`container` 클래스를 통해, 페이지의 좌우 여백을 주어 감쌀 수 있습니다.

```html
<section class="container">
  <span class="mt-2 bg-primary d-block">Learn</span>
  <span class="mt-2 bg-warning d-block">HTML</span>
  <div class="d-flex justify-content-center">
    <button class="mt-2 btn btn-success">CSS</button>
  </div>
</section>
```
## Break Points

> 범위
> 

특정 크기 이상에서만 원하는 스타일링이 되도록 나눌 수 있습니다.

<aside>
💡 Breakpoint를 활용해 디바이스 크기에 따라 레이아웃을 다르게 설정할 수 있습니다.
이후 CSS Grid에서 유용하게 활용됩니다.

</aside>

| 클래스명 | 상세 설명 |
| --- | --- |
| sm | x-small (≥ 576px) |
| md | medium (≥ 768px) |
| lg | large (≥ 992px) |
| xl | extra large (≥ 1200px) |
| xxl | extra extra large (≥ 1400px) |

> {attribute}-{breakpoint}-{value} 형태로 사용합니다.
> 

```html
<section class="container">
  <p class="mt-2 bg-primary d-inline d-lg-block">Learn</p>
  <p class="mt-2 bg-warning d-inline d-lg-block">HTML</p>
  <button class="mt-2 btn btn-success">CSS</button>
</section>
```
