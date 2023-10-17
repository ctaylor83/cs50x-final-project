package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/", func(c *gin.Context) {
		c.String(200, "Hello, World!")
	})

	r.GET("/design", func(c *gin.Context) {
		c.String(200, "Design Page")
	})	

	r.Run() // listens and serves on 0.0.0.0:8080 by default
}