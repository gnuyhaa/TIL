# [1] git 기초
git : 소프트웨어  
저장소 : git으로 관리되고 있는 애  
로컬 저장소 : 내 컴퓨터에 있는 저장소  
원격 저장소 : github에 있는 저장소

git 설치 후 해야할 일  
git config 설정( user.name, user.email)

파일 상태 확인
- git status

저장소 선언 
- git init

1. git add . # 추가된 모든 파일이 추가됨
2. git commit -m '커밋 메시지'
3. git push origin main

파일의 4가지 상태
- Untracked : git으로 추적하지 않고 있는 상태 (새로 생성) 
- Unmodified : 추적하고 있는 상태, 변경 상태x (이전에 한번이라도 커밋한 파일)
- Modified : 추적하고 있으며, 파일이 변경된 상태 (커밋 이후 파일을 수정)
- Staged : 추적으로 시작하거나, 변경되었을 때, 이 파일을 commit하기 위해 storge에 올린 상태
  
원격저장소 설정  
git remote add origin {github repo 주소}  
참고) git remote remove origin 

원격저장소 목록 확인  
git remote -v

원격저장소에 업로드  
git push origin main  
git push {원격 저장소 주소} {브랜치 이름}

원격저장소에 있는 것 복제(최초 1회만 실행)  
git clone {원격저장소 주소}

실습 과제 내 브랜치로 받는 경로  
1. git checkout main
2. git pull origin main
3. git checkout 내브랜치
4. git merge main
5. :q enter 
6. (작업 완료 후 -> 본인 브랜치에 업로드하기) 
7. git add . 
8. git commit -m '메시지'
9. git push origin 본인 브랜치

