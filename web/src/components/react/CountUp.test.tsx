import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { CountUp } from './CountUp';

describe('<CountUp>', () => {
  it('renders 0 initially', () => {
    render(<CountUp end={17} />);
    expect(screen.getByText('0')).toBeInTheDocument();
  });
  it('renders end value when reduced motion preferred', () => {
    vi.spyOn(window, 'matchMedia').mockReturnValue({
      matches: true, addEventListener: vi.fn(), removeEventListener: vi.fn(),
    } as unknown as MediaQueryList);
    render(<CountUp end={16.5} decimals={1} />);
    expect(screen.getByText('16.5')).toBeInTheDocument();
  });
});
