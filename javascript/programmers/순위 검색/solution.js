function solution(info, query) {
  const dict = init_dictionary();
  const answer = [];
  
  // info 기반으로 딕셔너리에 점수 인덱싱
  for(const user of info) {
      const user_info = parse_info(user);
      const conditions = user_info.info.map(it => ["-", it]);
  
      function put_userinfo_to_dict(selected) {
          const key = createKey(selected);
          dict.get(key).push(user_info.score);
      }
      
      selection(conditions, put_userinfo_to_dict);
  }
  
  // 점수 정렬
  for(const scores of dict.values()) {
      scores.sort((a,b) => a - b);
  }
  
  for(const q of query) {
      const query_info = parse_query(q);
      
      const key = createKey(query_info.info);
      // 점수를 단순히 계산하는게 아니라, 이진 탐색으로 구해야 함
      const scores = dict.get(key);
      const minright_idx = search_minright_idx(scores, query_info.score);
      // console.log(query_info.score, scores, minright_idx);
      
      const result = scores.length - minright_idx - 1;
      
      answer.push(result);
  }
  
  return answer;
}

// score보다 작은 값 중 가장 오른쪽 값 반환
function search_minright_idx(arr, score) {
  let start = 0;
  let end = arr.length - 1;
  while (start <= end) {
      const mid = Math.floor((start + end) / 2);
      
      if(arr[mid] >= score) {
          end = mid - 1;
      } else if (arr[mid] < score) {
          start = mid + 1;
      }
  }
  
  return end;
}

function init_dictionary() {
  const dict = new Map();
  
  const lang = ["-", "cpp", "java", "python"];
  const field = ["-", "backend", "frontend"];
  const carrer = ["-", "junior", "senior"];
  const soul_food = ["-", "chicken", "pizza"];
  
  function add_dict_index(selected) {
      dict.set(createKey(selected), []);
  }
  
  selection([lang, field, carrer, soul_food], add_dict_index);
  return dict;
}

function selection(conditions, callback, selected = []) {
  if(conditions.length === selected.length) {
      callback(selected);
      return;
  }
  
  for(const key of conditions[selected.length]) {
      selected.push(key);
      selection(conditions, callback, selected);
      selected.pop(key);
  }
}

function create_dict_index(dict, conditions, selected = []) {
  if(conditions.length === selected.length) {
      dict.set(createKey(selected), []);
      return;
  }
  
  for(const key of conditions[selected.length]) {
      selected.push(key);
      create_dict_index(dict, conditions, selected);
      selected.pop(key);
  }
}

function createKey(arr) {
  return arr.join(' ');
}

function parse_info(str) {
  const tokens = str.split(' ');
  
  return {
      info: tokens.slice(0,4),
      score: parseInt(tokens[4])
  };
}

function parse_query(str) {
  const tokens = str.split(' ');
  
  return {
      info: [tokens[0], tokens[2], tokens[4], tokens[6]],
      score: parseInt(tokens[7])
  };
}