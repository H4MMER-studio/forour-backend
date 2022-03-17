# :rose: 꽃 추천 서비스, ForOur

<div id="top"></div>

## :books: Table Of Contents

- [:tada: Introduce](#tada-introduce)
  - [:raising_hand: ForOur](#raising_hand-forour)
  - [:arrows_counterclockwise: Service Proces](#arrows_counterclockwise-service-process)
  - [:fire: Motivation](#fire-motivation)
  - [:information_desk_person: Features](#information_desk_person-features)
  - [:rocket: Build Process](#rocket-build-process)
  - [:no_entry_sign: Limitation](#no_entry_sign-limitation)
- [:recycle: Refactor](#recycle-refactor)
  - [:pushpin: API Communication](#pushpin-api-communication)
  - [:pushpin: API Document](#pushpin-api-document)
  - [:pushpin: CI/CD](#pushpin-cicd)
  - [:pushpin: Database](#pushpin-database)
  - [:pushpin: Formatting and Linting](#pushpin-formatting-and-linting)
  - [:pushpin: Package Manager](#pushpin-package-manager)
  - [:pushpin: Unittest](#pushpin-unittest)

### :tada: Introduce

#### :raising_hand: ForOur

[ForOur](https://forour.space)는 12가지 상황에 대한 사용자의 답변을 토대로 성향을 분석하여 어울리는 꽃을 알려주는 서비스입니다.

#### :arrows_counterclockwise: Service Process

![Service Process]()

#### :fire: Motivation

해당 프로젝트의 차별점 및 의의를 서비스와 애플리케이션 측면으로 나누어 생각하면 다음과 같습니다.

##### For Service

서비스 측면에서 해당 프로젝트는 기존 성향 분석 서비스가 참여하는 **사용자 본인**에 국한되어 본인의 성향을 파악하던 것과 달리 **타인**에 초점을 맞춰 타인의 성향을 분석한다는 점에 있어 차별성이 존재합니다. 그리고 이것은 장기적으로 **사용자 유입**의 차이가 발생함을 의미합니다.

기존 본인의 성향만 분석하던 서비스의 경우 본인의 결과를 공유하여 타인의 참여를 유도하지만 타인의 성향을 분석할 경우 이후 본인이 분석한 타인에게 본인의 성향을 대신 분석해줄 것을 요구하기 때문에 훨씬 강력한 **유입 동기**로 작용합니다.

##### For Application

애플리케이션 측면에서 부흥하고 있는 파이썬 웹 프레임워크 **FastAPI**와 함께 NoSQL 데이터베이스 종류 중 하나인 **MongoDB**를 활용하여 **비동기적 통신**을 구축했다는 의의가 있습니다.

현재 국내 프로젝트 중 FastAPI를 사용하여 구현된 서비스 예시가 오픈소스로 많이 존재하지 않습니다. 더욱이 해외의 경우에도 제작자인 Sebastian Ramirez가 공식적으로 제공 중인 보일러 플레이트는 [VueJS, FastAPI, PostgreSQL를 활용한 동기적 통신 풀스택](https://github.com/tiangolo/full-stack-fastapi-postgresql) 및 [VueJS, FastAPI, Couchbase를 활용한 동기적 통신 풀스택](https://github.com/tiangolo/full-stack-fastapi-couchbase)만 존재하기 때문에 MongoDB를 활용한 비동기적 통신 풀스택에 대한 예시는 많이 존재하지 않은 상황입니다.

이러한 맥락에서 본 프로젝트는 FastAPI 및 MongoDB를 활용한 비동기적 통신의 좋은 예시가 될 수 있습니다. 구체적으로 구현된 기능에 관련해서는 바로 다음에 이어지는 [:information_desk_person: Features](#information-desk-person-features) 항목과 [:recycle: Refactor](recycle-refactor) 항목을 통해 확인하실 수 있습니다.

#### :information_desk_person: Features

#### :rocket: Build Process

애플리케이션의 배포 과정은 아래 이미지와 같습니다.

![Build Process]()

#### :no_entry_sign: Limitation

해당 프로젝트의 한계점을 서비스와 애플리케이션 측면으로 나누어 생각하면 다음과 같습니다. 해당 한계점은 바꾸어 이야기하면 보완하고 구현해야 할 사항입니다.

##### For Service

서비스 측면에서 결국 해당 프로젝트는 장기적인 유입을 촉구하지 못하는 한계점이 존재합니다.

##### For Application

<p align="right">⬆️ <a href="#top">Back to Top</a></p>

### :recycle: Refactor

#### :pushpin: API Communication

##### Before

기존에는 동기적(Synchrnous) 통신을 구현했습니다.

##### After

비동기적(Aysnchronous) 통신으로 변경했습니다.

#### :pushpin: API Document

##### Before

##### After

#### :pushpin: CI/CD

##### Before

기존에는 [GitHub Actions]()를 활용하여 CI/CD를 구축했고 관련 알림을 이메일을 통해서 받았습니다.

##### After

[CircleCI](.circleci/workflow.yml)를 활용하여 CI/CD를 구축하고 관련 알림을 Slack을 통해 수신하게 변경했습니다. GitHub Actions를 사용해도 Slack을 통해 알림을 받을 수 있었으나 CircleCI로 변경한 가장 큰 이유는 관리 측면에 있습니다.

[H4MMER.studio]()라는 공용 저장소를 만들고 팀원들과 ForOur 이외에도 다양한 작업을 함께 진행하기 시작했습니다. 이때 CI/CD 작업 진행 및 결과를 확인하려면 GitHub의 경우 개별 저장소에 들어가 Actions 탭에서 확인해야 하지만 CircleCI의 경우 아래 이미지와 같이 간단하게 대시보드를 통해 여러 작업을 한 번에 확인할 수 있습니다.

![CircleCI Dashboard]()

#### :pushpin: Database

##### Before

기존에는 [PostgreSQL]() 및 [SQLModel]()를 활용하여 SQL를 사용한 데이터베이스를 구축했습니다. ERD는 아래와 같습니다.

![ERD](/images/ERD.png)

##### After

[MongoDB]() 및 [Motor]()를 활용하여 NoSQL를 사용한 데이터베이스로 변경했습니다.

#### :pushpin: Formatting and Linting

##### Before

기존에는 별다른 포맷팅이나 린팅을 설정하지 않았습니다.

##### After

[pre-commit](.pre-commit-config.yaml) 및 [flake8](), [isort](), [black]()을 활용하여 포맷 및 린팅을 구성했습니다.

#### :pushpin: Pacakge Manager

##### Before

기존에는 [requiremets.txt]() 파일을 사용해서 필요한 패키지를 관리했습니다.

##### After

[Poetry]()를 사용하여 패키지를 관리하는 것으로 변경했습니다.

#### :pushpin: Unittest

##### Before

##### After

<p align="right">⬆️ <a href="#top">Back to Top</a></p>
