package main

import (
    "fmt"
    "math"
)

func main() {
  var n, m , a float64

  fmt.Scanf("%f %f %f", &n, &m, &a)
  fmt.Println(int64(math.Ceil(n / a) * math.Ceil(m / a)))
}
