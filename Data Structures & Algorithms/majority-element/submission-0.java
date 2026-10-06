class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap();
        for (int num : nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
       

        int answer = 0;
        int maxFrequency = 0;

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (entry.getValue() > maxFrequency) {
                maxFrequency = entry.getValue();
                answer = entry.getKey();
            }
        }
        return answer;
    }
}