package main

import (
  "fmt"
  "strconv"
)

func main() {
  var n int
  fmt.Scanf("%d", &n)

  var words []string = make([]string, n, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&words[i])
  }

  var shortWords []string = make([]string, n, n)
  for i := 0; i < n; i++ {
    if len(words[i]) <= 10 {
      shortWords[i] = words[i]
    } else {
      shortWords[i] = string(words[i][0]) + strconv.Itoa(len(words[i]) - 2) + string(words[i][len(words[i])-1])
    }
  }

  for i := 0; i < n; i++ {
    fmt.Println(shortWords[i])
  }
}
