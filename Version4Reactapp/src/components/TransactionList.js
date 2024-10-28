import React, { useContext } from 'react';
import { GlobalContext } from '../context/GlobalState';

const TransactionList = () => {
  const { transactions } = useContext(GlobalContext);

  return (
    <ul className="list">
      {transactions.map(transaction => (
        <li key={transaction.id}>
          {transaction.text} <span>{transaction.amount}</span>
        </li>
      ))}
    </ul>
  );
};

export default TransactionList;
