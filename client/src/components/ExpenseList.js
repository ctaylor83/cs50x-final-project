import React from 'react';
import axios from 'axios';
import ExpenseItem from './ExpenseItem';

const ExpenseList = ({ setExpenseToEdit }) => {
    const [expenses, setExpenses] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8080/expenses')
            .then(response => {
                setExpenses(response.data.data);
            });
    }, []);

    const handleDelete = (id) => {
        axios.delete(`http://localhost:8080/expenses/${id}`)
            .then(() => {
                setExpenses(expenses.filter((expense) => expense.id !== id));
            })
            .catch(error => console.error('There was an error!', error));
    };

    const handleEdit = (expense) => {
        // Instead of alert, you set the expense to edit in the parent state
        setExpenseToEdit(expense);
    };

    return (
        <div>
            {expenses.map(expense => (
                <ExpenseItem key={expense.id} expense={expense} onDelete={handleDelete} onEdit={handleEdit} />
            ))}
        </div>
    );
};

export default ExpenseList;
