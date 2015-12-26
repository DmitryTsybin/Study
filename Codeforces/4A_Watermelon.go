package main

import (
    "fmt"
)

func main() {
  var n int

  fmt.Scanf("%d", &n)

  if n == 2 {
    fmt.Println("NO")
  } else if n % 2 == 0 {
    fmt.Println("YES")
  } else {
    fmt.Println("NO")
  }
}
