import { useEffect, useRef, useState } from 'react';
import { getStoredTheme, setStoredTheme, applyTheme, type ThemeChoice } from '../../lib/theme';

const LABEL: Record<ThemeChoice, string> = { light: '☀', dark: '☾', system: '◐' };

export function ThemeToggle() {
  const [theme, setTheme] = useState<ThemeChoice>('system');
  const nextFlip = useRef<'dark' | 'light'>('dark');

  useEffect(() => {
    const t = getStoredTheme();
    setTheme(t);
    applyTheme(t);
  }, []);

  const handleClick = () => {
    let next: ThemeChoice;
    if (theme === 'system') {
      next = nextFlip.current;
      nextFlip.current = nextFlip.current === 'dark' ? 'light' : 'dark';
    } else {
      next = 'system';
    }
    setStoredTheme(next);
    applyTheme(next);
    setTheme(next);
  };

  return (
    <button
      onClick={handleClick}
      aria-label={`Theme: ${theme}, click to switch`}
      className="font-mono text-sm px-2 py-1 hover:text-accent transition-colors"
    >
      {LABEL[theme]}
    </button>
  );
}
