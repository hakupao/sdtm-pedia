// web/src/components/react/CompareFilter.tsx
import { useState } from 'react';
import platforms from '../../data/platforms.json';
import { getUIStrings, type Lang } from '../../i18n/helpers';

interface Dim {
  key: string;
  label: Record<Lang, string>;
  values: Record<string, string>;
  winners: string[];
}

interface Props { dims: Dim[]; lang: Lang; }

export function CompareFilter({ dims, lang }: Props) {
  const [q, setQ] = useState('');
  const t = getUIStrings(lang);
  const lower = q.toLowerCase().trim();
  const filtered = lower
    ? dims.filter((d) => d.label[lang].toLowerCase().includes(lower))
    : dims;

  return (
    <>
      <input
        type="search"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder={t['compare.filter.placeholder']}
        aria-label={t['compare.filter.label']}
        className="font-mono text-sm px-3 py-2 border border-rule bg-bg w-64 mb-6"
      />
      <div className="overflow-x-auto">
        <table className="w-full font-serif text-sm border-collapse min-w-[600px]">
          <thead>
            <tr className="border-b border-rule">
              <th className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">DIMENSION</th>
              {platforms.map((p) => (
                <th key={p.key} className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">
                  {p.name}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filtered.map((d) => (
              <tr key={d.key} className="border-b border-rule">
                <td className="py-2 px-2 font-mono text-[10px] tracking-wider">
                  {d.label[lang]}
                </td>
                {platforms.map((p) => (
                  <td
                    key={p.key}
                    className={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}
                  >
                    {d.values[p.key]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
