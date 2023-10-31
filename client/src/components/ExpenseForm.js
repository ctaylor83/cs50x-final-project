import React, { useState } from 'react';
import axios from 'axios';

const ExpenseForm = () => {
    const [description, setDescription] = useState('');
    const [amount, setAmount] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8080/expenses', { description, amount: parseFloat(amount) })
            .then(response => {
                // handle success
                console.log(response.data);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" required />
            <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" required />
            <button type="submit">Add Expense</button>
        </form>
    );
};

export default ExpenseForm;
