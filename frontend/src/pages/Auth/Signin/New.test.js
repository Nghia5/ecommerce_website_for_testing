import { render, screen, fireEvent } from '@testing-library/react';
import SignIn from './SignIn'; // Giả sử SignIn là component cần test
import '@testing-library/jest-dom';

describe('Sign In Component', () => {
  // Test case 1: Đăng nhập với thông tin hợp lệ
  test('Sign in with valid credentials', async () => {
    render(<SignIn />);

    // Tìm các trường input và nút
    const emailInput = screen.getByLabelText(/email/i); // Tìm input theo label "Email"
    const passwordInput = screen.getByLabelText(/password/i); // Tìm input theo label "Password"
    const signInButton = screen.getByRole('button', { name: /sign in/i }); // Nút đăng nhập

    // Nhập thông tin hợp lệ
    fireEvent.change(emailInput, { target: { value: 'user@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'correctpassword' } });
    fireEvent.click(signInButton);

    // Kiểm tra xem có chuyển hướng hoặc thông báo thành công không
    const successMessage = await screen.findByText(/welcome/i); // Thông báo chào mừng
    expect(successMessage).toBeInTheDocument();
  });

  // Test case 2: Đăng nhập với mật khẩu sai
  test('Sign in with invalid password', async () => {
    render(<SignIn />);

    const emailInput = screen.getByLabelText(/email/i);
    const passwordInput = screen.getByLabelText(/password/i);
    const signInButton = screen.getByRole('button', { name: /sign in/i });

    fireEvent.change(emailInput, { target: { value: 'user@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'wrongpassword' } });
    fireEvent.click(signInButton);

    // Kiểm tra thông báo lỗi
    const errorMessage = await screen.findByText(/incorrect password/i);
    expect(errorMessage).toBeInTheDocument();
  });

  // Test case 3: Đăng nhập với email không tồn tại
  test('Sign in with non-existent email', async () => {
    render(<SignIn />);

    const emailInput = screen.getByLabelText(/email/i);
    const passwordInput = screen.getByLabelText(/password/i);
    const signInButton = screen.getByRole('button', { name: /sign in/i });

    fireEvent.change(emailInput, { target: { value: 'notexist@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'somepassword' } });
    fireEvent.click(signInButton);

    const errorMessage = await screen.findByText(/email does not exist/i);
    expect(errorMessage).toBeInTheDocument();
  });
});
