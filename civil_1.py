class Participant:
    def __init__(self, name, tier, main_line, sub_line):
        self.name = name
        self.tier = tier
        self.main_line = main_line
        self.sub_line = sub_line
        self.main_line_score, self.sub_line_score = self.calculate_scores()
        self.assigned_team = None
        self.assigned_position = None

    def calculate_scores(self):
        tier_scores = {"브론즈": 13, "실버": 19, "골드": 38, "플래티넘": 47, "에메랄드": 56, "다이아": 62}
        line_scores = {"탑": 2, "정글": 1, "미드": 0, "원딜": 1, "서풋": 5}
        sub_line_penalties = {"탑": -3, "정글": 0, "미드": -3, "원딜": -1, "서풋": 0, "올라인": 1, None: -6}

        tier_score = tier_scores.get(self.tier, 0)
        main_line_score = tier_score + line_scores.get(self.main_line, 0)
        sub_line_score = main_line_score + sub_line_penalties.get(self.sub_line, 0)

        return main_line_score, sub_line_score

    def __repr__(self):
        return (f"점수(이름={self.name}, 티어={self.tier}, 주라인={self.main_line}, "
                f"보조라인={self.sub_line}, 메인점수={self.main_line_score}, 보조라인 점수={self.sub_line_score}, "
                f"팀={self.assigned_team}, 포지션={self.assigned_position})")


class ParticipantsManager:
    def __init__(self):
        self.participants_data = []

    def add_player(self, player):
        self.participants_data.append(player)

    def assign_teams(self):
        # 점수 정렬
        self.participants_data.sort(key=lambda x: x.main_line_score, reverse=True)

        team1 = []
        team2 = []

        positions = ["탑", "정글", "미드", "원딜", "서풋"]

        # 포지션별로 플레이어를 팀에 배정
        for pos in positions:
            players_for_pos = [p for p in self.participants_data if p.main_line == pos]
            for i, player in enumerate(players_for_pos):
                if i % 2 == 0:
                    team1.append(player)
                    player.assigned_team = 1
                else:
                    team2.append(player)
                    player.assigned_team = 2
                player.assigned_position = pos
                self.participants_data.remove(player)

        # 남은 플레이어를 팀에 배정
        remaining_players = self.participants_data[:]
        for player in remaining_players:
            if len(team1) <= len(team2):
                team1.append(player)
                player.assigned_team = 1
            else:
                team2.append(player)
                player.assigned_team = 2
            self.participants_data.remove(player)

        # 팀 균형 맞추기
        self.balance_teams(team1, team2)

        # 팀 스코어 계산
        team1_score = sum(p.main_line_score for p in team1)
        team2_score = sum(p.main_line_score for p in team2)

        return team1, team2, team1_score, team2_score

    def balance_teams(self, team1, team2):
        team1_score = sum(p.main_line_score for p in team1)
        team2_score = sum(p.main_line_score for p in team2)
        
        while abs(team1_score - team2_score) > 5:
            combined_teams = team1 + team2
            combined_teams.sort(key=lambda x: x.sub_line_score, reverse=True)

            # 팀 균형을 맞추기 위해 플레이어를 교환
            swapped = False
            for player in combined_teams:
                if player.assigned_team == 1 and len(team2) < 5:
                    team1.remove(player)
                    team2.append(player)
                    player.assigned_team = 2
                    swapped = True
                    break
                elif player.assigned_team == 2 and len(team1) < 5:
                    team2.remove(player)
                    team1.append(player)
                    player.assigned_team = 1
                    swapped = True
                    break

            if not swapped:
                break

            team1_score = sum(p.main_line_score for p in team1)
            team2_score = sum(p.main_line_score for p in team2)

        return team1, team2

# 예시 사용법
participants_manager = ParticipantsManager()
participants_manager.add_player(Participant("황현성", "실버", "탑", None))
participants_manager.add_player(Participant("선현태", "실버", "정글", "원딜"))
participants_manager.add_player(Participant("김준영", "에메랄드", "미드", None))
participants_manager.add_player(Participant("김영두", "골드", "원딜", "정글"))
participants_manager.add_player(Participant("강수정", "실버", "서풋", "미드"))
participants_manager.add_player(Participant("유호제", "플래티넘", "정글", None))
participants_manager.add_player(Participant("이승현", "에메랄드", "미드", "원딜"))
participants_manager.add_player(Participant("고은성", "플래티넘", "미드", "원딜"))
participants_manager.add_player(Participant("권성배", "플래티넘", "서풋", "원딜"))
participants_manager.add_player(Participant("정지영", "실버", "서풋", None))

team1, team2, team1_score, team2_score = participants_manager.assign_teams()

print("Team 1:")
for player in team1:
    print(player)
print("Team 1 Score:", team1_score)

print("Team 2:")
for player in team2:
    print(player)
print("Team 2 Score:", team2_score)
