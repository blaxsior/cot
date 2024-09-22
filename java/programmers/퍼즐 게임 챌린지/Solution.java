class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int min_level = diffs[0];
        int max_level = diffs[0];
        
        // 레벨 설정
        for(int i = 1; i < diffs.length; i++) {
            if(min_level > diffs[i]) min_level = diffs[i];
            if(max_level < diffs[i]) max_level = diffs[i];
        }        
        // limit보다 작아지는 가장 작은 값을 얻어야 함
        // limit > => min 이동
        // limit < => max 이동
        
        while(min_level <= max_level) {
            int level = (int) ((min_level + max_level) / 2);
            long levelScore = calculateScore(diffs, times, level);
            
            // level을 더 높여야 한다.
            if(levelScore > limit) {
                min_level = level + 1;
            } else {
                max_level = level - 1;
            }
        }
        
        return min_level;
    }
    
    public static long calculateScore(int[] diffs, int[] times, int level) {
        long result = 0;
        
        for(int i = 0; i < diffs.length; i++) {
            int time_cur = times[i];
            int time_prev = i > 0 ? times[i-1] : 1;
            
            result += time_cur;
            if(diffs[i] > level) {
                result += (diffs[i] - level) * (time_cur + time_prev);
            }
        }
        
        return result;
    }
}

//diff 난이도
//퍼즐 시간 time_cur
//이전 퍼즐 시간 time_prev

// diff <= level: time_cur 소모
// diff > level: diff_level만큼 틀림 =>  (diff - level) * (time_cur + time_prev) + time_cur만큼 시간 소모

// 제한 시간 내 모두 해결하기 위한 숙련도 최소값
// 해결 가능한 최소값인지 알아내야 함.