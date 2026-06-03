import React, { useState } from 'react';
import { Input } from '../../../../components/ui/input';
import { Button } from '../../../../components/ui/button';
import { loginService } from '../api/service';
import type { LoginCredentials } from '../schema/login';

export const LoginForm: React.FC = () => {
  const [credentials, setCredentials] = useState<LoginCredentials>({ email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setCredentials(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess(false);

    try {
      const response = await loginService(credentials);
      console.log('Login successful:', response);
      setSuccess(true);
      // Here you would typically save the token to localStorage/context and redirect
    } catch (err: any) {
      setError(err.message || 'An error occurred during login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: '2rem', border: '1px solid #eaeaea', borderRadius: '8px', backgroundColor: '#fff' }}>
      {error && <div style={{ color: '#d32f2f', marginBottom: '1rem', padding: '0.5rem', backgroundColor: '#ffebee', borderRadius: '4px' }}>{error}</div>}
      {success && <div style={{ color: '#2e7d32', marginBottom: '1rem', padding: '0.5rem', backgroundColor: '#e8f5e9', borderRadius: '4px' }}>Login successful!</div>}
      
      <Input 
        label="Email" 
        type="email" 
        name="email" 
        id="email" 
        value={credentials.email} 
        onChange={handleChange} 
        required 
        placeholder="Enter your email"
      />
      <Input 
        label="Password" 
        type="password" 
        name="password" 
        id="password" 
        value={credentials.password} 
        onChange={handleChange} 
        required 
        placeholder="Enter your password"
      />
      
      <div style={{ marginTop: '1.5rem' }}>
        <Button type="submit" disabled={loading}>
          {loading ? 'Logging in...' : 'Login'}
        </Button>
      </div>
    </form>
  );
};
