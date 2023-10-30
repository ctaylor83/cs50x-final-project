package handlers

import (
	"net/http"

	"github.com/ctaylor83/cs50x-final-project/server/models"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func CreateExpense(db *gorm.DB) gin.HandlerFunc {
	return func(c *gin.Context) {
		var expense models.Expense
		if err := c.ShouldBindJSON(&expense); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		db.Create(&expense)
		c.JSON(http.StatusOK, gin.H{"data": expense})
	}
}
