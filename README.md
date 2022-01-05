# This-is-the-coding-test

✅그리디

- 현재 상황에서 지금 가장 좋은 것만 고르는 방법
- 주로 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제

✅구현

- 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
- 구현하기 어려운 문제 : 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제, 특정 소수점 자리까지 출력해야하는 문제, 문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트에 넣어야 하는 (파싱을 해야 하는) 문제 등이 까다로운 구현 유형의 문제
- 프로그래밍 문법을 정확하게 숙지하지 못했거나, 라이브러리 사용 경험이 부족하면 구현 유형의 문제를 풀 때 불리하다  

❗ 이 책에서는 🙆‍완전 탐색, 🙆‍시뮬레이션 유형을 모두 '구현' 유형으로 묶어서 다루고 있다.  
🙆‍♀️ 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법  
🙆‍ 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행  

❌ 구현 시 고려해야 할 메모리 제약 사항
- 파이썬 리스트 크기
- C / C++ 에서 변수의 표현 범위

✔ 파이썬이 C/C++보다 구현 난이도가 쉬운 편

✅DFS/BFS

- 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘
- DFS: 깊이 우선 탐색: 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘  
  1️⃣ 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다  
  2️⃣ 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 수택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스태에서 최상단 노드를 꺼냄  
  3️⃣ 2️⃣의 과정을 더 이상 수행할 수 없을 때까지 반복  
- BFS: 너비 우선 탐색: 가까운 노드부터 탐색하는 알고리즘  
  1️⃣ 탐색 시작 노드를 큐에 삽입하고 방문처리  
  2️⃣ 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.  
  3️⃣ 2️⃣의 과정을 더 이상 수행할 수 없을 때까지 반복  

❗꼭 필요한 자료구조 기초
- 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정  
  ➡ 그래프, 트리 등의 자료구조 안에서 탐색하는 문제를 주로 다룸  
  ➡ 대표적인 탐색 알고리즘으로 DFS와 BFS  
- 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조  
  ➡ 스택과 큐는 자료구조의 기초 개념으로 삽입(Push), 삭제(Pop)의 함수로 구성된다  
- 스택 : '섭입후출'구조 또는 '후입선출'구조
- 큐 : '선입선출'구조 * 흔히 공정한 자료구조라고 불린다

✅정렬 (면접 단골 문제)
- 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것  
  ✔ 선택 정렬 : 데이터가 무작위로 여러 개 있을 때, 가장 작은 데이터를 선택해 맨 앞에 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복  
                매번 가장 작은 것을 택한다는 의미  
                🕐시간 복잡도 : O(n^2)  
  
  ✔ 삽입 정렬 : 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입  
                특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어있다고 가정  
                🕐시간 복잡도 : O(n^2) , 최선의 경우(거의 정렬되어있는 경우)는 O(n)  
  ✔ 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까 : 기준을 pivot이라고 함  
              🕐시간 복잡도 : O(NlogN)  
  ✔ 계수 정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘  
              🕐시간 복잡도 : O(N + K)  

✅이진 탐색
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
