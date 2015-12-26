package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scanf("%s", &s)

  var t string
  fmt.Scanf("%s", &t)

  m := make([]byte, len(s))

  count := 0
  for i := 0; i < len(s); i++ {
    if s[i] != t[i] {
      count += 1
    }
  }

  if count % 2 != 0 {
    fmt.Println("impossible")
  } else {
    count = count / 2
    for i := 0; i < len(s); i++ {
      if s[i] != t[i] && count > 0 {
        m[i] = s[i]
        count -=1
      } else {
        m[i] = t[i]
      }
    }
    fmt.Println(string(m))
  }
}
