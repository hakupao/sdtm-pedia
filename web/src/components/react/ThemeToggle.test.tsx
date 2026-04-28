import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeToggle } from './ThemeToggle';

const LABELS = { light: 'Light', dark: 'Dark', system: 'System' };

describe('<ThemeToggle>', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  it('renders 3 inline buttons with i18n aria-labels', () => {
    render(<ThemeToggle navLabel="Theme" labels={LABELS} />);
    expect(screen.getByRole('button', { name: 'Light' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Dark' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'System' })).toBeInTheDocument();
  });

  it('marks "System" as pressed by default (no stored choice)', () => {
    render(<ThemeToggle navLabel="Theme" labels={LABELS} />);
    expect(screen.getByRole('button', { name: 'System' })).toHaveAttribute('aria-pressed', 'true');
    expect(screen.getByRole('button', { name: 'Light' })).toHaveAttribute('aria-pressed', 'false');
    expect(screen.getByRole('button', { name: 'Dark' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('clicking Light persists "light" + applies data-theme + flips aria-pressed', () => {
    render(<ThemeToggle navLabel="Theme" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'Light' }));
    expect(localStorage.getItem('theme')).toBe('light');
    expect(document.documentElement.dataset.theme).toBe('light');
    expect(screen.getByRole('button', { name: 'Light' })).toHaveAttribute('aria-pressed', 'true');
    expect(screen.getByRole('button', { name: 'System' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('clicking Dark persists "dark" + applies data-theme', () => {
    render(<ThemeToggle navLabel="Theme" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'Dark' }));
    expect(localStorage.getItem('theme')).toBe('dark');
    expect(document.documentElement.dataset.theme).toBe('dark');
    expect(screen.getByRole('button', { name: 'Dark' })).toHaveAttribute('aria-pressed', 'true');
  });

  it('clicking System after Dark removes data-theme + persists "system"', () => {
    render(<ThemeToggle navLabel="Theme" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'Dark' }));
    fireEvent.click(screen.getByRole('button', { name: 'System' }));
    expect(localStorage.getItem('theme')).toBe('system');
    expect(document.documentElement.hasAttribute('data-theme')).toBe(false);
    expect(screen.getByRole('button', { name: 'System' })).toHaveAttribute('aria-pressed', 'true');
  });

  it('uses nav with passed aria-label', () => {
    render(<ThemeToggle navLabel="主题" labels={LABELS} />);
    expect(screen.getByRole('navigation', { name: '主题' })).toBeInTheDocument();
  });
});
