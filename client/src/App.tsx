// This import is needed for TypeScript to understand JSX
import React, { useState } from 'react'
import Welcome from './components/Welcome'
import { TransactionApiService } from './services/api'
import { TransactionSummary } from './types'

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

  // Add this function to test the API
  const testApi = async (): Promise<void> => {
    try {
      setLoading(true);
      setError(null);
      const data = await TransactionApiService.getTransactionSummary();
      setSummary(data);
      console.log('API Response:', data);
    } catch (err) {
      setError('Failed to load data');
      console.error('API Error:', err);
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
      
      <main style={{ padding: '20px' }}>
        <Welcome 
          name={appState.userName}
          isLoggedIn={appState.isLoggedIn}
          onLogin={handleLogin}
        />
        
        {/* Add this test section */}
        <div style={{ marginTop: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
          <h3>API Test</h3>
          <button 
            onClick={testApi}
            disabled={loading}
            style={{ 
              padding: '8px 16px', 
              backgroundColor: '#22c55e', 
              color: 'white', 
              border: 'none', 
              borderRadius: '4px',
              cursor: loading ? 'not-allowed' : 'pointer'
            }}
          >
            {loading ? 'Loading...' : 'Test API Connection'}
          </button>
          
          {error && (
            <p style={{ color: 'red', marginTop: '10px' }}>Error: {error}</p>
          )}
          
          {summary && (
            <div style={{ marginTop: '10px' }}>
              <h4>Financial Summary:</h4>
              <p>Total Income: ${summary.total_income}</p>
              <p>Total Expenses: ${summary.total_expenses}</p>
              <p>Net Amount: ${summary.net_amount}</p>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App 