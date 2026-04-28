import { useEffect, useState } from 'react';
import { getStoredTheme, setStoredTheme, applyTheme, type ThemeChoice } from '../../lib/theme';

const ICON: Record<ThemeChoice, string> = { light: '☀', dark: '☾', system: '◐' };
const CHOICES: ThemeChoice[] = ['light', 'dark', 'system'];

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
    <nav aria-label={navLabel} className="flex gap-2 font-mono text-[10px] tracking-wider">
      {CHOICES.map((t) => (
        <button
          key={t}
          type="button"
          onClick={() => switchTo(t)}
          aria-pressed={t === theme}
          aria-label={labels[t]}
          title={labels[t]}
          className={t === theme ? 'text-ink font-bold' : 'text-ink-mute hover:text-accent'}
        >
          {ICON[t]}
        </button>
      ))}
    </nav>
  );
}
