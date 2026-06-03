import type { LoginCredentials, LoginResponse } from '../schema/login';

export const loginService = async (credentials: LoginCredentials): Promise<LoginResponse> => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Fake successful login
      if (credentials.email && credentials.password) {
        resolve({
          user: {
            id: '123',
            email: credentials.email,
            name: 'Test User'
          },
          token: 'fake-jwt-token-123'
        });
      } else {
        reject(new Error('Invalid credentials'));
      }
    }, 1000);
  });
};
