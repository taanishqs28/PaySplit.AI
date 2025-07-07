import React, {useState, useRef} from 'react';
import {TransactionApiService} from '../services/api';

type UploadCsvProps = {
  onUploadSuccess?: (numUploaded: number) => void;
};

export const UploadCsv: React.FC<UploadCsvProps> = ({ onUploadSuccess }) => {
    const fileInput = useRef<HTMLInputElement>(null);
    const [message, setMessage] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);
    const [canUpload, setCanUpload] = useState(true);

    const handleUpload = async(e:React.ChangeEvent<HTMLInputElement>) => {
        if(e.target.files && e.target.files[0]){
            setLoading(true);
            setMessage(null);
            setError(null);
            setCanUpload(false);
            try{
                const result = await TransactionApiService.uploadCSV(e.target.files[0]);
                if (onUploadSuccess) onUploadSuccess(result.transactions.length);
                setTimeout(() => {
                    setMessage(null);
                    setCanUpload(true);
                    if (fileInput.current) fileInput.current.value = '';
                }, 3000);
            }catch(err){
                setError('Failed to upload CSV');
                setCanUpload(true);
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
              disabled={loading || !canUpload}
              style={{ marginLeft: 10 }}
            />
          </label>
          {loading && <p>Uploading...</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
          {message && <div style={{ color: '#22c55e', fontWeight: 500 }}>{message}</div>}
        </div>
      );
}