// web/src/components/react/LangSwitcher.tsx
import { replaceLangInPath, type Lang } from '../../i18n/helpers';

const LABELS: Record<Lang, string> = { zh: '中', en: 'EN', ja: '日' };

interface Props {
  currentLang: Lang;
  pathname: string;
}

export function LangSwitcher({ currentLang, pathname }: Props) {
  const langs: Lang[] = ['en', 'zh', 'ja'];
  return (
    <nav className="flex gap-2 font-mono text-[10px] tracking-wider">
      {langs.map((l) => (
        <a
          key={l}
          href={replaceLangInPath(pathname, l)}
          aria-current={l === currentLang ? 'page' : undefined}
          className={l === currentLang ? 'text-ink font-bold' : 'text-ink-mute hover:text-accent'}
        >
          {LABELS[l]}
        </a>
      ))}
    </nav>
  );
}
