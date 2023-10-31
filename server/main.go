package main

import (
	"github.com/ctaylor83/cs50x-final-project/server/handlers"
	"github.com/gin-gonic/gin"
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
)


func main() {
    // Connect to database
    dsn := "user=chris password=cs50 dbname=cs50tracker sslmode=disable"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        panic("Failed to connect to database")
    }
    
    handler := &handlers.Handler{DB: db}

    router := gin.Default()

    router.POST("/expenses", handler.CreateExpense)
    router.GET("/expenses", handler.GetExpenses)
    router.PUT("/expenses/:id", handler.UpdateExpense)
    router.DELETE("/expenses/:id", handler.DeleteExpense)

    router.Run()  // listen and serve on 0.0.0.0:8080 by default
}
