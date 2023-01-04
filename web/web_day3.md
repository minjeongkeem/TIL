# github.io

- 계정명.github.io : github가 제공해주는 pages

- 경로와 파일명을 입력하지 않을경우 index.html이 default값으로 오픈됨

- static web

- dynamic web (web app): html은 1개고 안에 data만 바꿔서 보내줌

# Django

- 사용자 요청이 들어오면 SW가 받아서 일련의 연산 후 html 템플릿에 내용 채워서 주는 서버 프로그램 

   - manage.py: 프로젝트 총괄 매니저
   
   - project: app들의 집합 
  
   - app: 폴더 (부서)

   - Model (DB)
   - Templete(HTML)
   - View(Controller - 관리자) 
   - request - response는 한세트
   - view.py: 함수들 모음
   - view 함수는 HttpResponse 객체로 끝나야함
   - 웹 개발: view 함수 안에 무슨 일을 처리하도록 할건데? 
   - startapp => INSTALLED_APPS에 등록하기
   - view함수는 urlpattern과 1:1 매칭 필요함
   - (ex)
   - 1) 요청이 master urls.py로 들어옴 (ex)path app명 include(app명.urls)
   - 2) 이후 world가 맞는지 hello urls.py에서 확인
   - 3) 맞다면 views.py에서 HttpResponse return
   - 반드시 딕셔너리 값으로 변환하여 출력 가능함 (여러개의 값을 출력할 수도 있기 때문에)
   - 흐름: Root > urls.py (urlpatterns 확인) > app1 > urls.py (urlpatterns 확인) > views (함수 모음, return 확인 - render) > templates (html 확인)
  
- 프레임워크: Frame(틀)+work(일): 틀에 박힌 일, 강제되는 양식이 있음 (가장 많이 사용함)