from sys import stdin

input = stdin.readline

# N명 참가
# 지민이는 모든 파티에 참가
# 진실을 아는 사람 수 + 번호
# 진실 아는 사람 포함되어 있으면 진실 말 못함.

# N명 참가 / M개 파티
N, M = map(int, input().split(" "))

# 특정 사람이 참가한 파티 목록
man_party: list[list[int]] = [[] for _ in range(N)]
can_bluff_man = [True for _ in range(N)]
# 특정 파티에 참가한 사람 목록 
party_man: list[list[int]] = []
can_bluff_party = [True for _ in range(M)]

# n 번이 참가한 파티 순회, 함께 참가한 사람들에 대해 마킹?
# 거짓말쟁이와 함께 파티에 참가한 모든 사람에게 마킹, 해당 인원 참가한 파티도 모두 마킹

know_truth = [*map(lambda x: int(x) - 1, input().split(" "))][1:]
for man in know_truth:
  can_bluff_man[man] = False

i = 0
# man_party / party_man 비교하기
for _ in range(M):
  participants = [*map(lambda x: int(x) - 1, input().split(" "))][1:]
  party_man.append(participants)
  for p in participants:
    man_party[p].append(i)
  i += 1

for man in know_truth:
  for party in man_party[man]:
    # 이미 거짓말 못하는 파티라는 것을 알고 있으면 무시
    if can_bluff_party[party] == False: continue

    can_bluff_party[party] = False
    for participant in party_man[party]:
      if can_bluff_man[participant]:
        can_bluff_man[participant] = False
        know_truth.append(participant)

print(can_bluff_party.count(True))
