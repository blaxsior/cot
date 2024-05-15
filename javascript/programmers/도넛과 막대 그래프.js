function solution(edges) {
  // 생성 도넛 막대 8자
  const answer = [0,0,0,0];
  let graph_count = 0;
  // node에 대한 inout 횟수 저장
  const nodes_inout = new Map();
  
  for(const [from, to] of edges) {
    if(!nodes_inout.has(from)) nodes_inout.set(from, [0,0]);
    if(!nodes_inout.has(to)) nodes_inout.set(to, [0,0]);
    // from은 out / to는 in 추가
    nodes_inout.get(from)[1]++;
    nodes_inout.get(to)[0]++;
  }

  for(const [node, [node_in, node_out]] of nodes_inout) {
    // 가운데 연결점
    if(node_in === 0) {
      // out 개수 = 총 그래프 개수
      answer[0] = node;
      graph_count = node_out;
    }
    // 막대
    else if(node_in === 1 && node_out === 0) {
      answer[2] += 1;
    }
    // 8자
    else if(node_in === 2 && node_out === 2) {
      answer[3] += 1;
    }
  }
  answer[1] = graph_count - answer[2] - answer[3];

  return answer;
}

// 초기점 => in 0 out N

// 막대 => in 1 out 0 인 끝 점 존재
// 8자 => in 2 out 2인 중간 점 존재
// 도넛 => 전체 - 막대 - 8자
