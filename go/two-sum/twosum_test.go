package main

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	checkAns := func(t *testing.T, got, want []int) {
		t.Helper()
		if !reflect.DeepEqual(got, want) {
			t.Errorf("got %v want %v", got, want)
		}
	}

	t.Run("sample 1", func(t *testing.T) {
		numbers := []int{2, 7, 11, 15}
		target := 9

		got := twoSum(numbers, target)
		want := []int{0, 1}

		checkAns(t, got, want)
	})

	t.Run("sample 2", func(t *testing.T) {
		numbers := []int{3, 2, 4}
		target := 6

		got := twoSum(numbers, target)
		want := []int{1, 2}

		checkAns(t, got, want)
	})

	t.Run("sample 3", func(t *testing.T) {
		numbers := []int{3, 3}
		target := 6

		got := twoSum(numbers, target)
		want := []int{0, 1}

		checkAns(t, got, want)
	})
}
