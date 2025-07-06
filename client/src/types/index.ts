// Transaction model matching the backend Transaction class
export interface Transaction {
  id: number;
  date: string; // ISO date string
  description: string;
  amount: number;
  transaction_type: 'Income' | 'Expense';
  category?: string;
  is_business: boolean;
  business_percentage: number;
  created_at: string; // ISO date string
  updated_at: string; // ISO date string
}

// Financial summary response from the backend
export interface TransactionSummary {
  total_transactions: number;
  total_income: number;
  total_expenses: number;
  net_amount: number;
  income_count: number;
  expense_count: number;
}

// API response for transaction list
export interface TransactionListResponse {
  transactions: Transaction[];
  count: number;
}

// API response for CSV upload
export interface UploadResponse {
  message: string;
  transactions: Transaction[];
} 