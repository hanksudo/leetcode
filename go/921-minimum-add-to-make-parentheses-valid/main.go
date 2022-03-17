package main

func minAddToMakeValid(s string) int {
	var stack []rune
	for _, c := range s {
		if len(stack) == 0 || c == '(' {
			stack = append(stack, c)
		} else if stack[len(stack)-1] == '(' {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, c)
		}
	}
	return len(stack)
}
