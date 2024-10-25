# 팀 배정 프로그램

이 프로그램은 참가자 정보를 기반으로 팀을 자동으로 배정하는 기능을 제공합니다. 각 참가자는 티어, 주라인, 보조라인에 따라 점수를 계산하고, 해당 점수에 따라 두 팀으로 나누어집니다. 팀의 균형을 맞추기 위해 추가적인 로직도 포함되어 있습니다.

## 기능

- 참가자 점수 계산
- 주라인과 보조라인에 따라 팀 배정
- 팀 간의 점수를 균형 있게 유지

## DFD

![DFD](https://github.com/user-attachments/assets/8fa36ea9-bc09-4365-8edf-15c2bbeb6ff7)

## 순서도

![Flowchart (1)](https://github.com/user-attachments/assets/48fdf429-eb62-4fd6-999e-fad4334db8e6) 
## 코드 설명

### `Participant` 클래스

`Participant` 클래스는 각 참가자의 정보를 저장하고 점수를 계산하는 기능을 제공합니다.

- **속성**:
  - `name`: 참가자의 이름
  - `tier`: 참가자의 티어
  - `main_line`: 주라인
  - `sub_line`: 보조라인
  - `main_line_score`: 주라인 점수
  - `sub_line_score`: 보조라인 점수
  - `assigned_team`: 배정된 팀
  - `assigned_position`: 배정된 포지션

- **메서드**:
  - `calculate_scores()`: 참가자의 점수를 계산합니다.
  - `__repr__()`: 참가자 정보를 문자열로 반환합니다.

### `ParticipantsManager` 클래스

`ParticipantsManager` 클래스는 참가자 목록을 관리하고 팀을 배정하는 기능을 제공합니다.

- **속성**:
  - `participants_data`: 참가자 정보를 저장하는 리스트

- **메서드**:
  - `add_player(player)`: 참가자를 추가합니다.
  - `assign_teams()`: 참가자를 팀에 배정합니다.
  - `balance_teams(team1, team2)`: 팀 간의 균형을 맞춥니다.

### 사용 예시

아래는 프로그램을 사용하는 예시입니다.

```python
# ParticipantsManager 인스턴스 생성
participants_manager = ParticipantsManager()

# 참가자 추가
participants_manager.add_player(Participant("이름", "티어", "라인", "부포지션)) // 부 포지션은 None 처리해도 가능함.

# 팀 배정 및 점수 계산
team1, team2, team1_score, team2_score = participants_manager.assign_teams()

# 팀 정보 출력
print("Team 1:")
for player in team1:
    print(player)
print("Team 1 Score:", team1_score)

print("Team 2:")
for player in team2:
    print(player)
print("Team 2 Score:", team2_score)
