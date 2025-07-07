// This import is needed for TypeScript to understand JSX
import React, { useState, useEffect } from 'react'
//import Welcome from './components/Welcome'
import { TransactionApiService } from './services/api'
import { TransactionSummary } from './types'
import { UploadCsv } from './components/UploadCsv'
import TransactionList from './components/TransactionList'

// TypeScript interface for our app state
interface AppState {
  isLoggedIn: boolean;
  userName: string;
}

function App(): React.JSX.Element {
  // useState with TypeScript - we specify the type of our state
  const [appState, setAppState] = useState<AppState>({
    isLoggedIn: false,
    userName: 'Freelancer'
  });

  // Add this state for testing
  const [summary, setSummary] = useState<TransactionSummary | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    refreshSummary();
  }, []);

  const refreshSummary = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await TransactionApiService.getTransactionSummary();
      setSummary(data);
    } catch (err) {
      setError('Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  // Typed function to handle login
  const handleLogin = (): void => {
    setAppState(prevState => ({
      ...prevState,
      isLoggedIn: true
    }));
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <header style={{ 
        background: '#2563eb', 
        color: 'white', 
        padding: '20px',
        textAlign: 'center',
        borderRadius: '8px 8px 0 0'
      }}>
        <h1>PaySplit.AI</h1>
        <p>Financial Tracker for Freelancers</p>
      </header>
      
      {/* <main style={{ padding: '20px' }}>
        <Welcome 
          name={appState.userName}
          isLoggedIn={appState.isLoggedIn}
          onLogin={handleLogin}
        /> */}
        
        {/* Add this test section */}
        <main style={{ padding: '20px' }}>
          <UploadCsv onUploadSuccess={refreshSummary} />

          <div style={{ marginTop: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
            <h3>Financial Summary</h3>
            <p><strong>Total Income:</strong> ${summary ? summary.total_income : 0}</p>
            <p><strong>Total Expenses:</strong> ${summary ? summary.total_expenses : 0}</p>
            <p><strong>Net Amount:</strong> ${summary ? summary.net_amount : 0}</p>
          </div>

          <TransactionList />
        </main>
    </div>
  )
}

export default App 