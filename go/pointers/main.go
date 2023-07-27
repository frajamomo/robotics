package main

import (
    "fmt"
)

type Person struct {
    Name string
    Age int
}

func (p *Person) Birthday(){
    p.Age++
}

func main(){
    timmy := Person{ Age: 11, Name: "Timmy" }
    timmy.Birthday()
    fmt.Printf("Happy Birthday %s! You are now %d\n", timmy.Name, timmy.Age)
}
