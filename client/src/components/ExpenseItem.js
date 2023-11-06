import React from 'react';

const ExpenseItem = ({ expense, onDelete, onEdit }) => {
    return (
        <div>
            <p>Description: {expense.description}</p>
            <p>Amount: ${expense.amount}</p>
            <button onClick={() => onEdit(expense)}>Edit</button>
            <button onClick={() => onDelete(expense.id)}>Delete</button>
        </div>
    );
};

export default ExpenseItem;