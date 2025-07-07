import React, {useState, useRef} from 'react';
import {TransactionApiService} from '../services/api';

type UploadCsvProps = {
  onUploadSuccess?: () => void;
};

export const UploadCsv: React.FC<UploadCsvProps> = ({ onUploadSuccess }) => {
    const fileInput = useRef<HTMLInputElement>(null);
    const [message, setMessage] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleUpload = async(e:React.ChangeEvent<HTMLInputElement>) => {
        if(e.target.files && e.target.files[0]){
            setLoading(true);
            setMessage(null);
            setError(null);
            try{
                const result = await TransactionApiService.uploadCSV(e.target.files[0]);
                setMessage(`${result.transactions.length} transactions uploaded successfully`);
                if (onUploadSuccess) onUploadSuccess();
            }catch(err){
                setError('Failed to upload CSV');
            }finally{
                setLoading(false);
            }
        }
    };

    return (
        <div style={{ marginTop: 20 }}>
          <label>
            <strong>Upload Transactions CSV:</strong>
            <input
              type="file"
              accept=".csv"
              ref={fileInput}
              onChange={handleUpload}
              disabled={loading}
              style={{ marginLeft: 10 }}
            />
          </label>
          {loading && <p>Uploading...</p>}
          {message && <p style={{ color: 'green' }}>{message}</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
      );
}