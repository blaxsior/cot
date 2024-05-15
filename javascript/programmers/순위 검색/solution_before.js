function Query(lang, field, career, sf) {
  this.lang = lang;
  this.field = field;
  this.career = career;
  this.sf = sf;
}

function solution(info, query) {
  var answer = [];
  info = info.map(it => {
      const arr = it.split(' ');
      arr[arr.length-1] = Number(arr[arr.length-1]);
      return arr;
  });
  info.sort((a,b) => a.at(-1) - b.at(-1));
  
  // console.log(info);
  for(let i = 0; i < query.length; i++) {
      query[i] = query[i].split(' ');
      const q = new Query(query[i][0],query[i][2],query[i][4],query[i][6]);
      const selected = info.filter(it => (
          (q.lang === '-' || q.lang === it[0])
          && (q.field === '-' || q.field === it[1])
          && (q.career === '-' || q.career === it[2])
          && (q.sf === '-' || q.sf === it[3])
      )).map(it => it[4]);
      const target = Number(query[i][7]); // 숫자 변환 필요
      let start = 0, end = selected.length - 1;
      while(start < end) {
          let mid = Math.trunc((start + end) / 2);
          if (selected[mid] >= target) {
              end = mid - 1;
          } else {
              start = mid + 1;
          }
      }
      while(selected[start] >= target && start >= 0) {
          start -= 1;
      }
      if(selected.length > 0) {
          answer.push(selected.length - start - 1);        
      } else {
          answer.push(0);
      }
      // console.log(selected);
      // console.log(target, start, selected.length - start - 1);
  }
  // console.log(answer);
  return answer;
}