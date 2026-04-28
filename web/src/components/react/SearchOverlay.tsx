// web/src/components/react/SearchOverlay.tsx
import { useEffect, useRef, useState } from 'react';

interface Result {
  url: string;
  meta?: { title?: string };
  excerpt?: string;
}

function stripHtml(html: string): string {
  return html.replace(/<[^>]*>/g, '');
}

export function SearchOverlay() {
  const [open, setOpen] = useState(false);
  const [results, setResults] = useState<Result[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const pagefindRef = useRef<any>(null);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setOpen(true);
      }
      if (e.key === 'Escape') setOpen(false);
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  useEffect(() => {
    if (!open) return;
    inputRef.current?.focus();
    if (!pagefindRef.current && typeof window !== 'undefined') {
      // Runtime import of static asset emitted by `pagefind --site dist`. The
      // path is computed (not literal) and wrapped in `/* @vite-ignore */` so
      // Vite skips dependency pre-analysis — the file only exists at runtime
      // after `npm run build`, never inside src/.
      const pagefindUrl = '/pagefind/pagefind.js';
      // @ts-ignore — dynamic runtime import
      import(/* @vite-ignore */ pagefindUrl)
        .then((m) => {
          pagefindRef.current = m;
        })
        .catch(() => {
          // Pagefind index missing (e.g. dev server, jsdom test, or build skipped).
          // Search will simply return no results — no need to surface a runtime error.
        });
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
          placeholder="Search docs..."
          aria-label="Search docs"
          onChange={onChange}
          className="w-full px-4 py-3 font-mono text-sm border-b border-rule bg-bg"
        />
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
