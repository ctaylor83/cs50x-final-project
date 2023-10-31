import React from 'react';

const ExpenseItem = ({ expense }) => {
    return (
        <div>
            <p>Description: {expense.description}</p>
            <p>Amount: ${expense.amount}</p>
        </div>
    );
};

export default ExpenseItem;
