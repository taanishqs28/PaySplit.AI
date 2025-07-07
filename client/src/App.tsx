// This import is needed for TypeScript to understand JSX
import React, { useState, useEffect } from 'react'
//import Welcome from './components/Welcome'
import { TransactionApiService } from './services/api'
import { Transaction ,TransactionSummary } from './types'
import { UploadCsv } from './components/UploadCsv'
import TransactionList from './components/TransactionList'

// TypeScript interface for our app state
// interface AppState {
//   isLoggedIn: boolean;
//   userName: string;
// }

function App(): React.JSX.Element {
  // useState with TypeScript - we specify the type of our state
//   const [, setAppState] = useState<AppState>({
//     isLoggedIn: false,
//     userName: 'Freelancer'
//   });

  // Add this state for testing
  const [summary, setSummary] = useState<TransactionSummary | null>(null);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  useEffect(() => {
    refreshSummary();
    fetchTransactions();
  }, []);

  const refreshSummary = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await TransactionApiService.getTransactionSummary();
      setSummary(data);
      //setMessage('Data loaded successfully');
    } catch (err) {
      setError('Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  const fetchTransactions = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await TransactionApiService.getTransactions();
      setTransactions(data.transactions);
    } catch (err) {
      setError('Failed to load transactions');
    } finally {
      setLoading(false);
    }
  };

  const sortByAmount = () => {
    const sortedTransactions = [...transactions].sort((a, b) => {
      if (a.amount < b.amount) return -1;
      if (a.amount > b.amount) return 1;
      return 0;
    });
    if (sortOrder === 'asc') {
      setTransactions(sortedTransactions);
      setSortOrder('desc');
    } else {
      setTransactions(sortedTransactions.reverse());
      setSortOrder('asc');
    }
  };

  // Basic function to handle login will come in v2
//   const handleLogin = (): void => {
//     setAppState(prevState => ({
//       ...prevState,
//       isLoggedIn: true
//     }));
//   };

  return (
    <div style={{
      fontFamily: 'Inter, system-ui, sans-serif',
      background: '#f6f8fa',
      minHeight: '100vh',
      padding: '0',
      margin: '0'
    }}>
      <header style={{
        background: '#2563eb',
        color: 'white',
        padding: '32px 0',
        textAlign: 'center',
        borderRadius: '0 0 24px 24px',
        boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
      }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0 }}>PaySplit.AI</h1>
        <p style={{ fontSize: '1.2rem', opacity: 0.9, margin: 0 }}>Financial Tracker for Freelancers</p>
      </header>

      <main style={{
        maxWidth: 800,
        margin: '32px auto',
        padding: '0 16px'
      }}>
        {/* Upload Card */}
        <section style={{
          background: 'white',
          borderRadius: 16,
          boxShadow: '0 1px 4px rgba(0,0,0,0.06)',
          padding: 24,
          marginBottom: 24
        }}>
          <UploadCsv onUploadSuccess={(numUploaded) => {
            setMessage(`${numUploaded} transactions uploaded successfully`);
            refreshSummary();
            fetchTransactions();
            setTimeout(() => setMessage(null), 3000); // Hide message after 3 seconds
          }} />
        </section>

        {/* Summary Card */}
        <section style={{
          background: 'white',
          borderRadius: 16,
          boxShadow: '0 1px 4px rgba(0,0,0,0.06)',
          padding: 24,
          marginBottom: 24
        }}>
          <h3 style={{ fontSize: '1.3rem', fontWeight: 600, marginBottom: 16 }}>Financial Summary</h3>
          <div style={{ display: 'flex', gap: 32 }}>
            <div>
              <div style={{ fontSize: '1.1rem', color: '#2563eb', fontWeight: 500 }}>Total Income</div>
              <div style={{ fontSize: '1.5rem', fontWeight: 700 }}>
                ${summary ? summary.total_income.toFixed(2) : '0.00'}
              </div>
            </div>
            <div>
              <div style={{ fontSize: '1.1rem', color: '#ef4444', fontWeight: 500 }}>Total Expenses</div>
              <div style={{ fontSize: '1.5rem', fontWeight: 700 }}>
                ${summary ? summary.total_expenses.toFixed(2) : '0.00'}
              </div>
            </div>
            <div>
              <div style={{ fontSize: '1.1rem', color: '#22c55e', fontWeight: 500 }}>Net Amount</div>
              <div style={{ fontSize: '1.5rem', fontWeight: 700 }}>
                ${summary ? summary.net_amount.toFixed(2) : '0.00'}
              </div>
            </div>
          </div>
        </section>

        {/* Transaction List Card */}
        <section style={{
          background: 'white',
          borderRadius: 16,
          boxShadow: '0 1px 4px rgba(0,0,0,0.06)',
          padding: 24
        }}>
          {loading && <div style={{ color: '#2563eb', fontWeight: 500 }}>Loading...</div>}
          {error && <div style={{ color: '#ef4444', fontWeight: 500 }}>{error}</div>}
          {message && <div style={{ color: '#22c55e', fontWeight: 500 }}>{message}</div>}
          {transactions.length === 0 && (
            <div style={{ textAlign: 'center', color: '#888', padding: 32 }}>
              No transactions found. Upload a CSV to get started!
            </div>
          )}
          <div style={{ maxHeight: 320, overflowY: 'auto', overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '1rem' }}>
              <thead>
                <tr style={{ background: '#f3f4f6' }}>
                  <th style={{ textAlign: 'left', padding: '8px' }}>Date</th>
                  <th style={{ textAlign: 'left', padding: '8px' }}>Description</th>
                  <th style={{ textAlign: 'center', padding: '8px' }}>Type</th>
                  <th
                    style={{ cursor: 'pointer' }}
                    onClick={() => sortByAmount()}
                  >
                    Amount {sortOrder === 'asc' ? '▲' : '▼'}
                  </th>
                  {/* <th style={{ textAlign: 'left', padding: '8px' }}>Category</th> */}
                </tr>
              </thead>
              <tbody>
                {transactions.map((tx, idx) => (
                  <tr
                    key={tx.id}
                    style={{
                      background: idx % 2 === 0 ? '#fff' : '#f9fafb',
                      transition: 'background 0.2s',
                      cursor: 'pointer'
                    }}
                    onMouseOver={e => (e.currentTarget.style.background = '#e0e7ef')}
                    onMouseOut={e => (e.currentTarget.style.background = idx % 2 === 0 ? '#fff' : '#f9fafb')}
                  >
                    <td style={{ padding: '8px' }}>{new Date(tx.date).toLocaleDateString()}</td>
                    <td style={{ padding: '8px' }}>{tx.description}</td>
                    <td style={{ padding: '8px', textAlign: 'center' }}>{tx.transaction_type}</td>
                    <td style={{ padding: '8px', textAlign: 'right' }}>${tx.amount.toFixed(2)}</td>
                    {/* <td style={{ padding: '8px' }}>{tx.category || '-'}</td> */}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App 