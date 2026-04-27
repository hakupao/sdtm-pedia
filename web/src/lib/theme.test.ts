import { describe, it, expect, beforeEach, vi } from 'vitest';
import { getStoredTheme, setStoredTheme, applyTheme, resolveEffectiveTheme } from './theme';

describe('theme', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  it('getStoredTheme returns "system" by default', () => {
    expect(getStoredTheme()).toBe('system');
  });

  it('setStoredTheme persists choice to localStorage', () => {
    setStoredTheme('dark');
    expect(localStorage.getItem('theme')).toBe('dark');
    expect(getStoredTheme()).toBe('dark');
  });

  it('applyTheme sets data-theme attribute on root', () => {
    applyTheme('light');
    expect(document.documentElement.dataset.theme).toBe('light');
  });

  it('applyTheme with "system" removes the attribute', () => {
    document.documentElement.dataset.theme = 'dark';
    applyTheme('system');
    expect(document.documentElement.hasAttribute('data-theme')).toBe(false);
  });

  it('resolveEffectiveTheme returns "dark" when stored=system + media query dark', () => {
    setStoredTheme('system');
    vi.spyOn(window, 'matchMedia').mockReturnValue({ matches: true } as MediaQueryList);
    expect(resolveEffectiveTheme()).toBe('dark');
  });
});
