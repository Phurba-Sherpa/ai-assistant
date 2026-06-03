import React from 'react';
import { LoginForm } from '../features/auth/login/components/LoginForm';

export const LoginPage: React.FC = () => {
  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      minHeight: '100vh', 
      padding: '20px',
      backgroundColor: '#f5f5f5'
    }}>
      <div style={{ width: '100%', maxWidth: '400px' }}>
        <h1 style={{ textAlign: 'center', marginBottom: '2rem', color: '#333' }}>Sign In</h1>
        <LoginForm />
      </div>
    </div>
  );
};

export default LoginPage;
