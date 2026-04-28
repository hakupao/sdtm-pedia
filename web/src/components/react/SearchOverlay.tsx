// web/src/components/react/SearchOverlay.tsx
import { useEffect, useRef, useState } from 'react';
import { getUIStrings, type Lang } from '../../i18n/helpers';

interface Result {
  url: string;
  meta?: { title?: string };
  excerpt?: string;
}

function stripHtml(html: string): string {
  return html.replace(/<[^>]*>/g, '');
}

export function SearchOverlay({ lang = 'en' }: { lang?: Lang } = {}) {
  const t = getUIStrings(lang);
  const [open, setOpen] = useState(false);
  const [results, setResults] = useState<Result[]>([]);
  const [initFailed, setInitFailed] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const pagefindRef = useRef<any>(null);
  // C-P8-3: stash whoever had focus when overlay opens, so we can return
  // focus on close (Esc / backdrop click). Standard modal a11y pattern.
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        previousFocusRef.current = document.activeElement as HTMLElement | null;
        setOpen(true);
      }
      if (e.key === 'Escape') setOpen(false);
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  // C-P8-3: when overlay closes, restore focus to whoever opened it.
  useEffect(() => {
    if (!open && previousFocusRef.current) {
      previousFocusRef.current.focus();
      previousFocusRef.current = null;
    }
  }, [open]);

  useEffect(() => {
    if (!open) return;
    inputRef.current?.focus();
    if (!pagefindRef.current && typeof window !== 'undefined') {
      // Runtime import of static asset emitted by `pagefind --site dist`. The
      // path is computed (not literal) and wrapped in `/* @vite-ignore */` so
      // Vite skips dependency pre-analysis — the file only exists at runtime
      // after `npm run build`, never inside src/.
      const pagefindUrl = '/pagefind/pagefind.js';
      // C-P8-5: 1-retry backoff on transient init failure (CDN miss, partial
      // file). Surface initFailed state to aria live region after retry exhausts.
      const tryImport = (attempt: number) => {
        // @ts-ignore — dynamic runtime import
        import(/* @vite-ignore */ pagefindUrl)
          .then((m) => {
            pagefindRef.current = m;
          })
          .catch((err) => {
            if (attempt === 0) {
              setTimeout(() => tryImport(1), 1000);
              return;
            }
            setInitFailed(true);
            if (import.meta.env.PROD) {
              console.warn('[SearchOverlay] Pagefind init failed after retry:', err);
            }
          });
      };
      tryImport(0);
    }
  }, [open]);

  const onChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const q = e.target.value;
    if (!q || !pagefindRef.current) {
      setResults([]);
      return;
    }
    const { results: pageResults } = await pagefindRef.current.search(q);
    const data = await Promise.all(pageResults.slice(0, 10).map((r: any) => r.data()));
    setResults(data);
  };

  if (!open) return null;
  // C-P8-4: aria live region announces result count / unavailability to
  // screen readers. Empty string when no input typed yet.
  const liveMessage = initFailed
    ? t['search.unavailable']
    : results.length === 0
      ? ''
      : `${results.length} ${t['search.results.label']}`;

  return (
    <div
      className="fixed inset-0 bg-black/60 z-50 flex items-start justify-center pt-32"
      onClick={() => setOpen(false)}
    >
      <div
        className="bg-bg border border-rule w-full max-w-xl mx-4"
        onClick={(e) => e.stopPropagation()}
      >
        <input
          ref={inputRef}
          type="search"
          role="searchbox"
          placeholder={t['search.placeholder']}
          aria-label={t['search.placeholder']}
          onChange={onChange}
          className="w-full px-4 py-3 font-mono text-sm border-b border-rule bg-bg"
        />
        <div role="status" aria-live="polite" className="sr-only">
          {liveMessage}
        </div>
        <ul className="max-h-96 overflow-y-auto">
          {results.map((r, i) => (
            <li key={i} className="border-b border-rule p-3">
              <a href={r.url} className="block hover:bg-bg-alt">
                <div className="font-mono text-[10px] tracking-wider text-accent">
                  {r.meta?.title || r.url}
                </div>
                <div className="font-serif text-sm text-ink-mute mt-1">
                  {r.excerpt ? stripHtml(r.excerpt) : ''}
                </div>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default SearchOverlay;
