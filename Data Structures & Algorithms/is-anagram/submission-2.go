func isAnagram(s string, t string) bool {
    // Early exit: different lengths can't be anagrams
    // This is a necessary condition (same multiset → same cardinality)
    if len(s) != len(t) {
        return false
    }
    
    // Fixed-size array for 26 lowercase letters
    // Index mapping: 'a'→0, 'b'→1, ..., 'z'→25
    var count [26]int
    
    // Single pass: increment for s, decrement for t
    // If anagram, all counts end at zero
    for i := 0; i < len(s); i++ {
        count[s[i]-'a']++
        count[t[i]-'a']--
    }
    
    // Verify all buckets are zero
    for _, c := range count {
        if c != 0 {
            return false
        }
    }
    
    return true
}