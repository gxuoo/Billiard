# Billiard Game

Billiard Game은 3D 당구 시뮬레이션 게임입니다. 이 게임은 Python과 VPython 라이브러리를 이용해 만들어졌습니다. 이 README에서는 게임의 설치 및 실행 방법과 함께 협업 가이드라인에 대해 설명합니다.

## 설치 및 실행 방법

### 1. 필수 요구사항
이 게임을 실행하기 위해서는 Python 환경이 설치되어 있어야 합니다.
- Python 3.6 이상이 필요합니다. Python을 아직 설치하지 않았다면 [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하실 수 있습니다.
- 이 게임은 Web VPython 3.2을 이용해 만들어졌습니다.

### 2. 필요한 Python 라이브러리 설치하기
이 게임을 실행하기 위해서는 VPython 라이브러리가 필요합니다.
- VPython: 3D 모델링 및 시뮬레이션 라이브러리입니다. 이 라이브러리를 설치하기 위해선 Python을 설치한 후 터미널이나 명령 프롬프트에서 다음 명령을 실행하세요:

```sh
pip install vpython
```

### 3. 코드 다운로드 및 실행
게임을 실행하려면 이 README 파일이 있는 곳에서 Python 파일을 다운로드하세요. 그 다음 Python 파일을 실행하면 게임이 시작됩니다. 파일 이름은 `billiard.py`, 다음 명령을 사용해 프로그램을 실행할 수 있습니다:

```sh
python billiard.py
```

### 4. 게임 방법
게임 화면에서 마우스를 클릭하여 수구를 움직일 수 있습니다. 원하는 방향으로 수구를 치면 수구는 1번과 2번 목적구를 향해 움직입니다. 목표는 벽에 세 번 부딪히고 수구가 1번과 2번 목적구를 모두 맞추는 것입니다. 이것이 성공하면 점수가 올라갑니다.

## 협업 가이드라인

프로젝트의 성공을 위해서는 협업과 코드 리뷰가 필요합니다. 이 프로젝트는 GitHub Flow를 사용하여 협업을 진행합니다.

### GitHub Flow

1. 'master' 브랜치에서 새로운 브랜치를 만듭니다. 이 브랜치의 이름은 수정하려는 내용을 잘 설명하도록 합니다. 예를 들어, "fix-collision-bug"나 "add-new-score-system" 같이 명확한 이름을 사용합니다.
2. 새로운 기능을 개

발하거나 버그를 수정합니다. 이때는 주요 변경 사항을 잘 설명하는 commit 메시지를 사용합니다.
3. 변경 사항이 완료되면 GitHub에 브랜치를 push하고 Pull Request(PR)를 생성합니다. PR의 내용은 다른 개발자들이 이해할 수 있도록 충분한 설명을 포함해야 합니다.
4. 다른 팀원들이 PR을 리뷰하고 피드백을 제공합니다. 필요한 경우 코드를 수정하고 다시 리뷰를 요청합니다.
5. 모든 피드백이 해결되고 리뷰가 완료되면 'master' 브랜치로 PR을 병합(merge)합니다.

이 방식을 통해 개발 프로세스가 이루어집니다. 이 가이드라인을 따라주세요. 함께 성공적인 프로젝트를 만들어봅시다!
