import React, { useState, useContext } from 'react';
import { GlobalContext } from '../context/GlobalState';

const AddTransaction = () => {
  const [text, setText] = useState('');
  const [amount, setAmount] = useState(0);
  const { addTransaction } = useContext(GlobalContext);

  const onSubmit = e => {
    e.preventDefault();

    const newTransaction = {
      id: Math.floor(Math.random() * 100000000),
      text,
      amount: +amount
    };

    addTransaction(newTransaction);
  };

  return (
    <form onSubmit={onSubmit}>
      <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
      <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
      <button>Add Transaction</button>
    </form>
  );
};

export default AddTransaction;
