import React from 'react';
import ReactDOM from 'react-dom';
import App from '../src/App';
import { GlobalProvider } from '../src/context/GlobalState';

ReactDOM.render(
  <GlobalProvider>
    <App />
  </GlobalProvider>,
  document.getElementById('root')
);
