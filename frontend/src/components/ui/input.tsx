import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
}

export const Input: React.FC<InputProps> = ({ label, id, ...props }) => {
  return (
    <div style={{ marginBottom: '1rem' }}>
      {label && <label htmlFor={id} style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>{label}</label>}
      <input 
        id={id} 
        style={{ 
          padding: '0.5rem', 
          width: '100%', 
          boxSizing: 'border-box',
          border: '1px solid #ccc',
          borderRadius: '4px'
        }} 
        {...props} 
      />
    </div>
  );
};
