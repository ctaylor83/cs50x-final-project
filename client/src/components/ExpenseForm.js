import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExpenseForm = ({ expenseToEdit, setExpenses, setIsEditing }) => {
    const [description, setDescription] = useState('');
    const [amount, setAmount] = useState('');

    // When expenseToEdit changes, update form fields
    useEffect(() => {
        if (expenseToEdit) {
            setDescription(expenseToEdit.description);
            setAmount(expenseToEdit.amount);
        }
    }, [expenseToEdit]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const expenseData = { description, amount: parseFloat(amount) };

        if (expenseToEdit) {
            // Update existing expense
            axios.put(`http://localhost:8080/expenses/${expenseToEdit.id}`, expenseData)
                .then(response => {
                    // handle success - update expenses list
                    setExpenses((prevExpenses) => prevExpenses.map((exp) => exp.id === expenseToEdit.id ? response.data : exp));
                    setIsEditing(false); // Exit editing mode
                })
                .catch(error => {
                    // handle error
                    console.error('Update failed:', error);
                });
        } else {
            // Create new expense
            axios.post('http://localhost:8080/expenses', expenseData)
                .then(response => {
                    // handle success - add to expenses list
                    setExpenses((prevExpenses) => [...prevExpenses, response.data]);
                })
                .catch(error => {
                    // handle error
                    console.error('Creation failed:', error);
                });
        }

        // Clear form
        setDescription('');
        setAmount('');
    };

    // Clear form if we exit editing mode
    const handleCancel = () => {
        setDescription('');
        setAmount('');
        setIsEditing(false); // Exit editing mode
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" required />
            <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" required />
            <button type="submit">{expenseToEdit ? 'Update Expense' : 'Add Expense'}</button>
            {expenseToEdit && <button type="button" onClick={handleCancel}>Cancel</button>}
        </form>
    );
};

export default ExpenseForm;
