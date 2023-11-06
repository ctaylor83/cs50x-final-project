import React, { useState } from 'react';
import ExpenseForm from './components/ExpenseForm';
import ExpenseList from './components/ExpenseList';

const App = () => {
    const [expenses, setExpenses] = useState([]);
    const [expenseToEdit, setExpenseToEdit] = useState(null);
    const [isEditing, setIsEditing] = useState(false);

    // This function will be called when we want to edit an expense
    const handleEditInitiation = (expense) => {
        setExpenseToEdit(expense);
        setIsEditing(true); // We set isEditing to true to indicate we're in edit mode
    };

    return (
        <div>
            {isEditing ? (
                <div>
                    <h2>Edit Expense</h2>
                    <ExpenseForm
                        expenseToEdit={expenseToEdit}
                        setExpenses={setExpenses}
                        setIsEditing={setIsEditing}
                    />
                </div>
            ) : (
                <div>
                    <h2>Add Expense</h2>
                    <ExpenseForm setExpenses={setExpenses} />
                </div>
            )}
            <ExpenseList expenses={expenses} setExpenses={setExpenses} setExpenseToEdit={handleEditInitiation} />
        </div>
    );
};

export default App;