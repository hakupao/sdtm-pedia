import { useEffect, useState } from 'react';
import { getStoredTheme, setStoredTheme, applyTheme, type ThemeChoice } from '../../lib/theme';

const CHOICES: ThemeChoice[] = ['light', 'dark', 'system'];

const ICON: Record<ThemeChoice, JSX.Element> = {
  light: (
    <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" aria-hidden="true">
      <circle cx="8" cy="8" r="3" />
      <path d="M8 1.5v1.6M8 12.9v1.6M1.5 8h1.6M12.9 8h1.6M3.4 3.4l1.1 1.1M11.5 11.5l1.1 1.1M3.4 12.6l1.1-1.1M11.5 4.5l1.1-1.1" />
    </svg>
  ),
  dark: (
    <svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
      <path d="M6.2 2.2a6 6 0 1 0 7.6 7.6A5 5 0 0 1 6.2 2.2Z" />
    </svg>
  ),
  system: (
    <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="1.4" aria-hidden="true">
      <rect x="2" y="3" width="12" height="8.5" rx="1" />
      <path d="M5.5 14h5M8 11.5V14" strokeLinecap="round" />
    </svg>
  ),
};

interface Props {
  navLabel: string;
  labels: Record<ThemeChoice, string>;
}

export function ThemeToggle({ navLabel, labels }: Props) {
  const [theme, setTheme] = useState<ThemeChoice>('system');

  useEffect(() => {
    const t = getStoredTheme();
    setTheme(t);
    applyTheme(t);
  }, []);

  const switchTo = (t: ThemeChoice) => {
    setStoredTheme(t);
    applyTheme(t);
    setTheme(t);
  };

  return (
    <nav aria-label={navLabel} className="flex items-center gap-2">
      {CHOICES.map((t) => (
        <button
          key={t}
          type="button"
          onClick={() => switchTo(t)}
          aria-pressed={t === theme}
          aria-label={labels[t]}
          title={labels[t]}
          className={`inline-flex items-center justify-center min-w-8 min-h-8 pb-0.5 border-b ${
            t === theme
              ? 'text-accent border-accent'
              : 'text-ink-mute border-transparent hover:text-accent'
          }`}
        >
          {ICON[t]}
        </button>
      ))}
    </nav>
  );
}
