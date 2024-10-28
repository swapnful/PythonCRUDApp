import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';      // Main App component
import { GlobalProvider } from './context/GlobalState';  // Import the global state provider
import './index.css';         // Optional global styles

// Find the root element in the public/index.html
const root = ReactDOM.createRoot(document.getElementById('root'));

// Wrap the App component with the GlobalProvider to provide the state to the entire app
root.render(
  <React.StrictMode>
    <GlobalProvider>
      <App />
    </GlobalProvider>
  </React.StrictMode>
);
