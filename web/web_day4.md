## MTV
- Model - DB (필요하다면 view가 db를 받아옴)
- Template - HTML (화면)
- View - Controller (제어, url로부터 request를 받음)

## Tip!
- `cd -` 마지막에 있던 위치로 보내줌

## directory/templates
- templates 폴더가 각 app마다 들어있는데 그 안에 html명이 동일하면 각 app별 있는 html을 구분하여 호출하지 못함 
- => 따라서 app 별로 templates 안에 디렉토리를 만들어서 a/???.html로 구분해줘야함

## 사용자 입력값 처리

- 사용자 입력값 처리는 하나의 url / function으로 불가함 input이 있으면 output이 있어야함
  
## GET / POST 방식

- GET 방식으로 데이터 전송: 정보 공개됨,
method default 방식이 GET방식

- POST로 방식으로 데이터 전송: 데이터에 대한 안정성 보장

## middleware

- 가장 첫번째 검문소와 같음 
- c.f) csrf middleware: 다른 사이트에서 기존 사이트와 동일하게 위조한 사이트에서의 해킹을 막기 위함

- form에서 POST 양식으로 데이터를 넘기려면 csrf_token 필요, input tag에는 name이 있어야함

## etc

- 사용자 입력은 항상 'str'임
- https: 보안 ㅇ / http: 보안 x