// web/src/components/react/CompareFilter.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { CompareFilter } from './CompareFilter';

const dims = [
  {
    key: 'best-at',
    label: { zh: '最强场景', en: 'Best at', ja: '最も得意' },
    values: { claude: 'A', chatgpt: 'B', gemini: 'C', notebooklm: 'D' },
    winners: ['claude'],
  },
  {
    key: 'capacity',
    label: { zh: '容量上限', en: 'Capacity', ja: '容量上限' },
    values: { claude: '1.29M', chatgpt: '20', gemini: '1M', notebooklm: '50' },
    winners: ['claude'],
  },
];

describe('<CompareFilter>', () => {
  it('renders all rows by default', () => {
    render(<CompareFilter dims={dims} lang="zh" />);
    expect(screen.getByText('最强场景')).toBeInTheDocument();
    expect(screen.getByText('容量上限')).toBeInTheDocument();
  });
  it('filters rows by search input', () => {
    render(<CompareFilter dims={dims} lang="zh" />);
    const input = screen.getByRole('searchbox');
    fireEvent.change(input, { target: { value: '容量' } });
    expect(screen.queryByText('最强场景')).not.toBeInTheDocument();
    expect(screen.getByText('容量上限')).toBeInTheDocument();
  });
});
