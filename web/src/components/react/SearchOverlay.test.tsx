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

  // C-P8-3: focus must return to the element that triggered the overlay.
  it('returns focus to the previously focused element on close', () => {
    render(
      <>
        <button data-testid="trigger">Trigger</button>
        <SearchOverlay lang="en" />
      </>
    );
    const trigger = screen.getByTestId('trigger');
    trigger.focus();
    expect(document.activeElement).toBe(trigger);
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    expect(screen.getByRole('searchbox')).toBeInTheDocument();
    fireEvent.keyDown(document, { key: 'Escape' });
    expect(screen.queryByRole('searchbox')).not.toBeInTheDocument();
    expect(document.activeElement).toBe(trigger);
  });

  // C-P8-4: aria live region present (a11y plumbing wired). Live-region
  // *content* depends on Pagefind module which jsdom can't dynamic-import,
  // so we only assert structural presence + role/aria-live attributes here.
  it('renders an aria-live status region when open', () => {
    render(<SearchOverlay lang="en" />);
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    const liveRegion = document.querySelector('[role="status"][aria-live="polite"]');
    expect(liveRegion).not.toBeNull();
  });
});
