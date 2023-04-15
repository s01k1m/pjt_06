# PJT_06

<br>

## 20230414 with Seoyoung❤️ with Sol❤️

이는 6번 싸.피 1학기 관통프로젝트의 READ.me 입니다. 서영과 솔이 같은 팀으로 `Djano` &`github`를 이용해 서버를 구축하며 협업을 하는 방법을 공부했습니다.

<br>

## 📓 Order of task

1. 가상환경을 설정하고 `pip freeze > requirements.txt` `pip install -r requirements.txt`
2. `.gitignore` 파일을 생성함
3. account 앱이 모든 어플리케이션에 쓰이므로 `accounts/model` 같이 작성함
4. `createsuperuser` 만들고 아래의 데이터가 담긴 sqlite 파일을 `dumpdata accounts.json` 함

id   :  admin
pw :  1234

5. 솔이 조장을 맡아 master repository를 만들고
서영이 조원으로서 이 repository를 fork해서
각자의 컴퓨터에서 branch를 만들고
아래의 업무 분배표에 따른 기능구현을 하기로 했다.

## 👥 Task allocation table

| task order | app name | views | 이름 | 체크 |
| --- | --- | --- | --- | --- |
| 1 | accounts | login | 솔 | ✅ |
|  |  | logout | 솔 | ✅ |
|  |  | signup | 솔 | ✅ |
|  |  | update | 솔 | ✅ |
|  |  | delete | 서영 | ✅ |
|  |  | change_password | 서영 | ✅ |
|  |  | profile | 서영 | ✅ |
|  |  | follow | 서영 | ✅ |
| 2 | movie | index |  | ✅ |
|  |  | create |  | ✅ |
|  |  | detail |  | ✅ |
|  |  | update |  | ✅ |
|  |  | delete |  | ✅ |
|  |  | comments_create | 솔 | ✅ |
|  |  | commets_delete | 솔 | ✅ |
|  |  | likes | 서영 | ✅ |


---
<br>

## 🙂 What We Learned

- 배포 코드인 master에 영향을 주지 않으면서 branch를 통해 독립하여 기능을 구현하고 conflict된 상황을 반복적으로 해결하는 과정을 통해 git branch를 이용하는 이유와 방법을 학습하였다.
    
    ```bash
    # 새로운 기능을 구현할때는 배포 코드에 영향을 주지 않기 위해 새로운 branch에서 한다
    $ git branch {branch name}
    # merge가 끝나면 branch 삭제
    $ git branch -d {branch name}
    ```
    
- 조원은 다른 사람의 Repo를 fork를 하고나서, 자신의 local에서 작업을 완료 후, 이를 pull request 하였다. 조장은 이 코드를 merge하는 방법을 하루 동안 반복하였다. 이를 통해 다른 사람과 협업하는 방식을 학습하였다.
- 처음에는  다른 조처럼 어플리케이션을 기준으로 업무를 분배하려고 했다. 그렇게 한다면 conflict도 안나고 편하게 작성할 수는 있겠지만, 그러나 git pull request $ merge & coflict 해결을 공부하는 의미가 옅어질 것이라 생각이 들었다. 그래서 같은 어플리케이션 내에서 함께 코드를 작성하는 평행적 업무 수행을 해보았다. 이것이 pull request와 merge를 공부하는데 많은 공부가 되었던 것 같다. 같은 어플리케이션 vies.py에서 평행적으로 코드를 짜다보니 서로 소통을 많이 했고 또 작성하는 코드에서 모르는 부분이 있다면 편하게 물어보고 답변을 받아서 많이 배울 수 있어서 좋았다.

## 😭 Need to improve more

- branch는 가지치기가 아니다. 나뭇가지가 나뉘는 걸로 생각하기보다는 바라보고 있는 HEAD가 달라지는 것으로 이해하자
- ⭐명세서를 먼저 읽어보자. 무작정 코드를 짜러가지 말자.
- pull request에서 요청 내용 작성과 리뷰자도 이를 코멘트로 남기는 연습을 하자
- 시간에 쫓겨 추가기능을 구현하지 못하여 아쉽다
