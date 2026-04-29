import { useEffect, useState } from 'react';
import { getStoredFontSize, setStoredFontSize, applyFontSize, type FontSize } from '../../lib/fontSize';

const TIERS: FontSize[] = ['sm', 'md', 'lg', 'xl'];
const TIER_PX: Record<FontSize, string> = { sm: '10px', md: '12px', lg: '14px', xl: '16px' };

interface Props {
  navLabel: string;
  labels: Record<FontSize, string>;
}

export function FontSizeToggle({ navLabel, labels }: Props) {
  const [size, setSize] = useState<FontSize>('md');

  useEffect(() => {
    const s = getStoredFontSize();
    setSize(s);
    applyFontSize(s);
  }, []);

  const switchTo = (s: FontSize) => {
    setStoredFontSize(s);
    applyFontSize(s);
    setSize(s);
  };

  return (
    <nav aria-label={navLabel} className="flex items-baseline gap-2 font-mono">
      {TIERS.map((t) => (
        <button
          key={t}
          type="button"
          onClick={() => switchTo(t)}
          aria-pressed={t === size}
          aria-label={labels[t]}
          title={labels[t]}
          style={{ fontSize: TIER_PX[t] }}
          className={`inline-flex min-h-8 min-w-8 items-center justify-center ${
            t === size ? 'text-accent' : 'text-ink-mute hover:text-accent'
          }`}
        >
          A
        </button>
      ))}
    </nav>
  );
}
