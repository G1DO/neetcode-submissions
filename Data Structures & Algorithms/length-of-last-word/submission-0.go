func lengthOfLastWord(s string) int {
	parts := strings.Fields(s)
	if len(parts) == 0 {
		return 0
	}
	return len(parts[len(parts)-1])
}