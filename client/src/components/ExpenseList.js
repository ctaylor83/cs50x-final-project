import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ExpenseItem from './ExpenseItem';

const ExpenseList = () => {
    const [expenses, setExpenses] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8080/expenses')
            .then(response => {
                setExpenses(response.data.data);
            });
    }, []);

    return (
        <div>
            {expenses.map(expense => (
                <ExpenseItem key={expense.id} expense={expense} />
            ))}
        </div>
    );
};

export default ExpenseList;
