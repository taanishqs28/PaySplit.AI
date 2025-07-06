import React from 'react'

// TypeScript interface - defines the shape of our props
interface WelcomeProps {
  name: string;           // Required string prop
  isLoggedIn?: boolean;   // Optional boolean prop (note the ?)
  onLogin?: () => void;   // Optional function prop
}

// Function component with typed props
function Welcome({ name, isLoggedIn = false, onLogin }: WelcomeProps): React.JSX.Element {
  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Welcome, {name}!</h2>
      
      {/* Conditional rendering based on boolean prop */}
      {isLoggedIn ? (
        <p>You are logged in. Ready to track your finances!</p>
      ) : (
        <div>
          <p>Please log in to access your financial data.</p>
          {/* Only show button if onLogin function is provided */}
          {onLogin && (
            <button 
              onClick={onLogin}
              style={{ 
                padding: '8px 16px', 
                backgroundColor: '#2563eb', 
                color: 'white', 
                border: 'none', 
                borderRadius: '4px',
                cursor: 'pointer'
              }}
            >
              Login
            </button>
          )}
        </div>
      )}
    </div>
  )
}

export default Welcome 