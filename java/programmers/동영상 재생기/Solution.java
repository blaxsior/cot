import java.util.*;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int TIME_STEP = 10;
        int sec_len = timeStrToSec(video_len);
        int sec_pos = timeStrToSec(pos);
        int sec_op_start = timeStrToSec(op_start);
        int sec_op_end = timeStrToSec(op_end);
        
        sec_pos = skipOpening(sec_pos, sec_op_start, sec_op_end);
        for(var command: commands) {
            switch(command) {
                case "prev":
                    sec_pos -= TIME_STEP;
                    if(sec_pos < 0) sec_pos = 0;
                    break;
                case "next":
                    sec_pos += TIME_STEP;
                    if(sec_pos > sec_len) sec_pos = sec_len;
                    break;
            }
            sec_pos = skipOpening(sec_pos, sec_op_start, sec_op_end);
        }
        
        return secToTimeStr(sec_pos);
    }
    
    public static int timeStrToSec(String timeStr) {
        String[] times = timeStr.split(":");
        int secFromMin = Integer.parseInt(times[0]) * 60;
        int sec = Integer.parseInt(times[1]);
        
        return secFromMin + sec;
    }
    
    public static String secToTimeStr(int sec) {
        int minute = (int)(sec / 60);
        int second = sec % 60;
        
        return String.format("%02d:%02d", minute, second);
    }
    
    public static int skipOpening(int sec_pos, int sec_op_start, int sec_op_end) {
        if(sec_op_start <= sec_pos  && sec_pos <= sec_op_end) {
            return sec_op_end;
        }
        return sec_pos;
    }
}
// 10초 전 이동, 10초 후 이동, 오프닝 건너뛰기
// prev: 10초 전으로. 0분 0초가 가장 전
// next: 10초 후로. 짧으면 마지막으로
// 오프닝: op_start <= 구간 <= op_end면 op_end로

// 입력 종료 시간 반환