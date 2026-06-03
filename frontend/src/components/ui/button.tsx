import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {}

export const Button: React.FC<ButtonProps> = ({ children, ...props }) => {
  return (
    <button 
      style={{ 
        padding: '0.5rem 1rem', 
        cursor: 'pointer', 
        backgroundColor: '#007bff', 
        color: 'white', 
        border: 'none', 
        borderRadius: '4px',
        width: '100%',
        fontWeight: 'bold'
      }} 
      {...props}
    >
      {children}
    </button>
  );
};
