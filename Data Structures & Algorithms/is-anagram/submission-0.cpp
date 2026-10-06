class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        // If the lengths are different, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }

        // Sort both strings
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());

        // Compare sorted strings
        return s == t;
    }
};
