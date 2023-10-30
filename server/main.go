package main

import (
	"github.com/ctaylor83/cs50x-final-project/server/handlers"
	"github.com/gin-gonic/gin"
)

func main() {
	db := connectDB()

	r := gin.Default()
	r.POST("/expenses", handlers.CreateExpense(db))

	r.Run() // listen and serve on 0.0.0.0:8080
}
