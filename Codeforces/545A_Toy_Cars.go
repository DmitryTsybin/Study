package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scanf("%d", &n)

  var array [100][100]int
  for i := 0; i < n; i++ {
    for j := 0; j < n; j++ {
      fmt.Scan(&array[i][j])
    }
  }

  var results [100]int
  for i := 0; i < n; i++ {
    for j := 0; j < n; j++ {
      if array[i][j] != -1 && array[i][j] != 0 && array[i][j] != 2 {
        results[i] = 1
      }
    }
  }

  count := 0
  for i := 0; i < n; i++ {
    if results[i] == 0 {
      count += 1
    }
  }
  fmt.Println(count)

  for i := 0; i < n; i++ {
    if results[i] == 0 {
      fmt.Println(i+1)
    }
  }
}
