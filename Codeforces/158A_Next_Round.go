package main

import (
  "fmt"
)

func main() {
  var n, k int
  fmt.Scanf("%d %d", &n, &k)

  var scores []int = make([]int, n, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&scores[i])
  }

  border := scores[k-1]
  m := 0
  for i := 0; i < n; i++ {
    if scores[i] > 0 && scores[i] >= border {
      m++
    }
  }
  fmt.Println(m)
}
