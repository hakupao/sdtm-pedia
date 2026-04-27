import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { LangSwitcher } from './LangSwitcher';

describe('<LangSwitcher>', () => {
  it('renders 3 lang links', () => {
    render(<LangSwitcher currentLang="zh" pathname="/zh/guide" />);
    expect(screen.getAllByRole('link')).toHaveLength(3);
  });
  it('marks current lang as aria-current', () => {
    render(<LangSwitcher currentLang="en" pathname="/en/" />);
    const current = screen.getByText('EN');
    expect(current).toHaveAttribute('aria-current', 'page');
  });
  it('builds correct hrefs', () => {
    render(<LangSwitcher currentLang="zh" pathname="/zh/guide/demo" />);
    expect(screen.getByText('EN').closest('a')).toHaveAttribute('href', '/en/guide/demo');
    expect(screen.getByText('日').closest('a')).toHaveAttribute('href', '/ja/guide/demo');
  });
});
