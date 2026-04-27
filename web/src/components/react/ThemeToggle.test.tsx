import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeToggle } from './ThemeToggle';

describe('<ThemeToggle>', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  it('renders an accessible button', () => {
    render(<ThemeToggle />);
    expect(screen.getByRole('button', { name: /theme/i })).toBeInTheDocument();
  });

  it('cycles system → dark → system on click', () => {
    render(<ThemeToggle />);
    const btn = screen.getByRole('button');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('dark');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('system');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('light');
  });
});
