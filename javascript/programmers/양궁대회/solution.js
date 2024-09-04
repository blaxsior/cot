function solution(n, info) {
  return getBestHits(n, info);
}

// n: 맞춘 수
// info: 어치피의 맞춘 수 
function getBestHits(n, info) {
  const LEN = info.length;
  // 최선 점수 배열
  const best = [0,0,0,0,0,0,0,0,0,0,0];
  const hits = [0,0,0,0,0,0,0,0,0,0,0];

  // 최대 점수 차이
  let max_diff = 0;

  // cur: 현재 맞춘 수
  function dfs(cur, start) {
      if(cur === n) {
          // 총 점수 계산
          let score_apeach = 0;
          let score_lion = 0;

          for(let i = 0; i < LEN; i++) {
              // (1) 어피치 (2) 라이언
              if(info[i] === 0 && hits[i] === 0) continue;
              if(info[i] >= hits[i]) score_apeach += 10 - i;
              else score_lion += 10 - i;
          }

          const score_diff = score_lion - score_apeach;
          if(score_diff <= 0 || score_diff < max_diff) return;
          else if(score_diff === max_diff) {
              // for문 돌면서 비교, 더 낮은 점수 많은걸 선택

              for(let idx = LEN - 1; idx > -1; idx--) {
                  if(best[idx] > hits[idx]) return;
                  else if(best[idx] < hits[idx]) break;
              }    
          }

          max_diff = score_diff;
          for(let i = 0; i < LEN; i++) {
              best[i] = hits[i];
          }

          return;
      }

      for(let idx = start; idx < LEN; idx++) {
          hits[idx]++;
          dfs(cur + 1, idx);
          hits[idx]--;
      }
  }

  dfs(0,0);
  return best.every(it => it === 0) ? [-1] : best;
}

// 재귀로 순회하면서 검사.
// 인덱스 위치만큼 덧셈


// 어피치 n발, 라이언 n발
// a = b이면 a로
// 특정 점수에 더 많이 맞춘 사람이 가져감
// 동일하면 어피치

// 가장 큰 점수 차이로 이길 때, 점수 배열대로 담아 반환. 이길 수 없으면 [-1]

// 맞춘 화살의 개수 = info
// 우승 방법이 여러개면 낮은 점수 여러개 맞춘 경우
// 전부 탐색. 동점 나오면 배팅 X
// 점수는 10점 ~ 0점