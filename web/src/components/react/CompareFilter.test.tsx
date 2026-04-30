// web/src/components/react/CompareFilter.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { CompareFilter } from './CompareFilter';

const dims = [
  {
    key: 'best-at',
    label: { zh: '最强场景', en: 'Best at', ja: '最も得意' },
    values: {
      claude: { zh: 'A zh', en: 'A en', ja: 'A ja' },
      chatgpt: { zh: 'B zh', en: 'B en', ja: 'B ja' },
      gemini: { zh: 'C zh', en: 'C en', ja: 'C ja' },
      notebooklm: { zh: 'D zh', en: 'D en', ja: 'D ja' },
    },
    winners: ['claude'],
  },
  {
    key: 'capacity',
    label: { zh: '容量上限', en: 'Capacity', ja: '容量制限' },
    values: {
      claude: { zh: '1.29M zh', en: '1.29M en', ja: '1.29M ja' },
      chatgpt: { zh: '20 zh', en: '20 en', ja: '20 ja' },
      gemini: { zh: '1M zh', en: '1M en', ja: '1M ja' },
      notebooklm: { zh: '50 zh', en: '50 en', ja: '50 ja' },
    },
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
  it('localizes filter input placeholder + aria-label per lang', () => {
    const { rerender } = render(<CompareFilter dims={dims} lang="zh" />);
    expect(screen.getByPlaceholderText('按维度筛选...')).toBeInTheDocument();
    expect(screen.getByLabelText('按维度筛选')).toBeInTheDocument();
    expect(screen.getByText('A zh')).toBeInTheDocument();
    rerender(<CompareFilter dims={dims} lang="ja" />);
    expect(screen.getByPlaceholderText('次元で絞り込み...')).toBeInTheDocument();
    expect(screen.getByLabelText('次元で絞り込み')).toBeInTheDocument();
    expect(screen.getByText('A ja')).toBeInTheDocument();
    expect(screen.queryByText('A zh')).not.toBeInTheDocument();
    rerender(<CompareFilter dims={dims} lang="en" />);
    expect(screen.getByPlaceholderText('Filter by dimension...')).toBeInTheDocument();
    expect(screen.getByLabelText('Filter by dimension')).toBeInTheDocument();
    expect(screen.getByText('A en')).toBeInTheDocument();
  });
});
