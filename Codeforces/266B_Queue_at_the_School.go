package main

import (
  "fmt"
)

func main() {
  var n, t int
  fmt.Scanf("%d %d", &n, &t)

  var queue string
  fmt.Scanf("%s", &queue)

  byteQueue := []byte(queue)

  for i := 0; i < t; i++ {
    for j := 0; j < len(byteQueue) - 1; {
      if byteQueue[j] == 'B' && byteQueue[j+1] == 'G' {
        byteQueue[j] = 'G'
        byteQueue[j+1] = 'B'
        j += 2
      } else {
        j += 1
      }

    }
  }
  fmt.Println(string(byteQueue[:]))
}
