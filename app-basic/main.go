package main

import (
	"fmt"
	"io"

	"github.com/containerd/containerd"
	"golang.org/x/crypto/md4"
	"golang.org/x/text/language"
	"golang.org/x/text/message"
)

func main() {
	message.SetString(language.Spanish, "hello world", "hola mundo")
	whatever()
	p := message.NewPrinter(language.Spanish)
	fmt.Println(p.Sprintf("hello world"))
	fmt.Println(containerd.DefaultSnapshotter)
}

func whatever() {
	h := md4.New()
	data := "These pretzels are making me thirsty."
	io.WriteString(h, data)
	fmt.Printf("MD4 is the new MD5: %x\n", h.Sum(nil))
}
