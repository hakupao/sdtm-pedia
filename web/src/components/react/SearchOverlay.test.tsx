// web/src/components/react/SearchOverlay.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { SearchOverlay } from './SearchOverlay';

describe('<SearchOverlay>', () => {
  it('opens on Cmd+K', () => {
    render(<SearchOverlay lang="en" />);
    expect(screen.queryByRole('searchbox')).not.toBeInTheDocument();
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    expect(screen.getByRole('searchbox')).toBeInTheDocument();
  });

  it('closes on Escape', () => {
    render(<SearchOverlay lang="en" />);
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    expect(screen.getByRole('searchbox')).toBeInTheDocument();
    fireEvent.keyDown(document, { key: 'Escape' });
    expect(screen.queryByRole('searchbox')).not.toBeInTheDocument();
  });
});
