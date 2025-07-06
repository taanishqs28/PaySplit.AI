import axios from 'axios' //this is HTTP client to make requests to the backend
import { Transaction, TransactionListResponse, UploadResponse, TransactionSummary } from '../types'

const api = axios.create({
    baseURL: '/api',
});

export class TransactionApiService {
    static async getTransactionSummary(): Promise<TransactionSummary>{
        const response = await api.get('/transactions/summary');
        return response.data;
    }
    static async getTransactions(limit: number = 100): Promise<TransactionListResponse>{
        const response = await api.get('/transactions', {params: {limit}});
        return response.data;
    }
    static async getTransactionById(id: number): Promise<Transaction>{
        const response = await api.get(`/transactions/${id}`);
        return response.data;
    }
    static async uploadCSV(file: File): Promise<UploadResponse>{
        const formData = new FormData();
        formData.append('file', file);
        const response = await api.post('/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    }
}
    