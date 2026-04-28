import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { FontSizeToggle } from './FontSizeToggle';

const LABELS = { sm: 'Small', md: 'Medium', lg: 'Large', xl: 'X-Large' };

describe('<FontSizeToggle>', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-fontsize');
  });

  it('renders 4 inline buttons with i18n aria-labels', () => {
    render(<FontSizeToggle navLabel="Font size" labels={LABELS} />);
    expect(screen.getByRole('button', { name: 'Small' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Medium' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Large' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'X-Large' })).toBeInTheDocument();
  });

  it('marks "Medium" as pressed by default (no stored choice)', () => {
    render(<FontSizeToggle navLabel="Font size" labels={LABELS} />);
    expect(screen.getByRole('button', { name: 'Medium' })).toHaveAttribute('aria-pressed', 'true');
    expect(screen.getByRole('button', { name: 'Small' })).toHaveAttribute('aria-pressed', 'false');
    expect(screen.getByRole('button', { name: 'Large' })).toHaveAttribute('aria-pressed', 'false');
    expect(screen.getByRole('button', { name: 'X-Large' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('clicking Small persists "sm" + applies data-fontsize + flips aria-pressed', () => {
    render(<FontSizeToggle navLabel="Font size" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'Small' }));
    expect(localStorage.getItem('fontsize')).toBe('sm');
    expect(document.documentElement.dataset.fontsize).toBe('sm');
    expect(screen.getByRole('button', { name: 'Small' })).toHaveAttribute('aria-pressed', 'true');
    expect(screen.getByRole('button', { name: 'Medium' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('clicking X-Large persists "xl" + applies data-fontsize', () => {
    render(<FontSizeToggle navLabel="Font size" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'X-Large' }));
    expect(localStorage.getItem('fontsize')).toBe('xl');
    expect(document.documentElement.dataset.fontsize).toBe('xl');
    expect(screen.getByRole('button', { name: 'X-Large' })).toHaveAttribute('aria-pressed', 'true');
  });

  it('clicking Medium after Large removes data-fontsize + persists "md"', () => {
    render(<FontSizeToggle navLabel="Font size" labels={LABELS} />);
    fireEvent.click(screen.getByRole('button', { name: 'Large' }));
    fireEvent.click(screen.getByRole('button', { name: 'Medium' }));
    expect(localStorage.getItem('fontsize')).toBe('md');
    expect(document.documentElement.hasAttribute('data-fontsize')).toBe(false);
    expect(screen.getByRole('button', { name: 'Medium' })).toHaveAttribute('aria-pressed', 'true');
  });

  it('uses nav with passed aria-label', () => {
    render(<FontSizeToggle navLabel="字号" labels={LABELS} />);
    expect(screen.getByRole('navigation', { name: '字号' })).toBeInTheDocument();
  });
});
