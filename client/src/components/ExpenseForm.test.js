import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import ExpenseForm from './ExpenseForm';

jest.mock('axios', () => ({
  get: jest.fn(),
  post: jest.fn(),
  put: jest.fn(),
  delete: jest.fn(),
}));

test('renders ExpenseForm', () => {
  render(<ExpenseForm />);
  const linkElement = screen.getByText(/Add Expense/i);
  expect(linkElement).toBeInTheDocument();
});

test('allows users to input expense data', () => {
  render(<ExpenseForm />);
  fireEvent.change(screen.getByPlaceholderText(/Description/i), {
    target: { value: 'Test Expense' },
  });
  fireEvent.change(screen.getByPlaceholderText(/Amount/i), {
    target: { value: '50' },
  });
  expect(screen.getByPlaceholderText(/Description/i).value).toBe('Test Expense');
  expect(screen.getByPlaceholderText(/Amount/i).value).toBe('50');
});
