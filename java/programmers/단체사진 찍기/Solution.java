import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int n, String[] data) {
        var friends = new char[]{'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
        List<FriendConditionChecker> checkers = Arrays
                .stream(data)
                .map(it -> FriendConditionCheckerBuilder.build(it))
                .collect(Collectors.toList());

        int result = permutation(friends, checkers, 0);
        return result;
    }

    // friends 친구들 배열
    // cur 현재 다루는 인덱스
    public static int permutation(char[] friends, List<FriendConditionChecker> checkers, int cur) {
        int count = 0;
        // 문자열 하나 완성
        if (cur == friends.length - 1) {
            Map<Character, Integer> friendIdxMapper = new HashMap<>();
            for(int i = 0; i < friends.length; i++) {
                friendIdxMapper.put(friends[i], i);
            } // char 인덱스 매핑

            for(var checker: checkers) {
                if(!checker.check(friendIdxMapper)) return 0;
            }
            return 1;
        }

        for (int i = cur; i < friends.length; i++) {
            swap(friends, i, cur);
            count += permutation(friends, checkers, cur + 1);
            swap(friends, i, cur);
        }
        return count;
    }

    public static void swap(char[] arr, int idx1, int idx2) {
        char temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

    static class FriendConditionCheckerBuilder {
        public static FriendConditionChecker build(String condition) {
            char friend1 = condition.charAt(0);
            char friend2 = condition.charAt(2);
            int range = condition.charAt(4) - '0';

            char type = condition.charAt(3);

            FriendConditionChecker checker;

            switch (type) {
                case '>':
                    checker = new FriendConditionExceedChecker(friend1, friend2, range);
                    break;
                case '<':
                    checker = new FriendConditionLessThanChecker(friend1, friend2, range);
                    break;
                case '=':
                    checker = new FriendConditionEqualChecker(friend1, friend2, range);
                    break;
                default:
                    throw new IllegalStateException("no checker match");
            }
            return checker;
        }
    }

    abstract static class FriendConditionChecker {
        protected char friend1;
        protected char friend2;
        protected int range;

        public FriendConditionChecker(char friend1, char friend2, int range) {
            this.friend1 = friend1;
            this.friend2 = friend2;
            this.range = range;
        }

        protected int getFriendsCountBetween(Map<Character, Integer> friendIdxMapper) {
            int idx1 = friendIdxMapper.get(friend1);
            int idx2 = friendIdxMapper.get(friend2);

            return Math.abs(idx1 - idx2) - 1;
        }

        abstract boolean check(Map<Character, Integer> friendIdxMapper);
    }

    static class FriendConditionEqualChecker extends FriendConditionChecker {

        public FriendConditionEqualChecker(char friend1, char friend2, int range) {
            super(friend1, friend2, range);
        }

        @Override
        public boolean check(Map<Character, Integer> friendIdxMapper) {
            int idx1 = friendIdxMapper.get(friend1);
            int idx2 = friendIdxMapper.get(friend2);

            return getFriendsCountBetween(friendIdxMapper) == range;
        }
    }

    static class FriendConditionExceedChecker extends FriendConditionChecker {

        public FriendConditionExceedChecker(char friend1, char friend2, int range) {
            super(friend1, friend2, range);
        }

        @Override
        public boolean check(Map<Character, Integer> friendIdxMapper) {
            return getFriendsCountBetween(friendIdxMapper) > range;
        }
    }

    static class FriendConditionLessThanChecker extends FriendConditionChecker {

        public FriendConditionLessThanChecker(char friend1, char friend2, int range) {
            super(friend1, friend2, range);
        }

        @Override
        public boolean check(Map<Character, Integer> friendIdxMapper) {
            return getFriendsCountBetween(friendIdxMapper) < range;
        }
    }
}
// 모든 조건 만족
// 정수 n, 배열 data
// 조건은 최대 100
// data는 조건 배열
// 1 / 3글자는 {A, C, F, J, M, N, R, T}
// 2글자는 ~
// 4글자는 = < >
// 5글자는 0 ~ 6
// 모든 조건을 만족해야 함
// 배치하고, 전수조사
// 총 개수는 8!
//