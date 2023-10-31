package handlers

import (
    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
    "net/http"
)

type Handler struct {
    DB *gorm.DB
}

type CreateExpenseInput struct {
    Description string  `json:"description" binding:"required"`
    Amount      float64 `json:"amount" binding:"required"`
}

type UpdateExpenseInput struct {
    Description string  `json:"description"`
    Amount      float64 `json:"amount"`
}

type Expense struct {
    ID          uint    `json:"id" gorm:"primary_key"`
    Description string  `json:"description"`
    Amount      float64 `json:"amount"`
    // ... other fields like timestamps, etc.
}

func (handler *Handler) CreateExpense(c *gin.Context) {
    var input CreateExpenseInput
    if err := c.ShouldBindJSON(&input); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }

    expense := Expense{Description: input.Description, Amount: input.Amount}
    handler.DB.Create(&expense)

    c.JSON(http.StatusOK, gin.H{"data": expense})
}

func (handler *Handler) GetExpenses(c *gin.Context) {
    var expenses []Expense
    result := handler.DB.Find(&expenses)
    if result.Error != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": result.Error.Error()})
        return
    }
    c.JSON(http.StatusOK, gin.H{"data": expenses})
}

func (handler *Handler) UpdateExpense(c *gin.Context) {
    var input UpdateExpenseInput
    if err := c.ShouldBindJSON(&input); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }

    var expense Expense
    if err := handler.DB.Where("id = ?", c.Param("id")).First(&expense).Error; err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Record not found!"})
        return
    }

    handler.DB.Model(&expense).Updates(input)
    c.JSON(http.StatusOK, gin.H{"data": expense})
}

func (handler *Handler) DeleteExpense(c *gin.Context) {
    var expense Expense
    if err := handler.DB.Where("id = ?", c.Param("id")).First(&expense).Error; err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Record not found!"})
        return
    }
    handler.DB.Delete(&expense)
    c.JSON(http.StatusOK, gin.H{"data": true})
}
