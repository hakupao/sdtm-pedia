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
    <nav aria-label="Language" className="flex items-center gap-2 font-mono tracking-wider">
      {langs.map((l) => (
        <a
          key={l}
          href={replaceLangInPath(pathname, l)}
          aria-current={l === currentLang ? 'page' : undefined}
          className={`pb-0.5 border-b ${
            l === currentLang
              ? 'text-accent border-accent'
              : 'text-ink-mute border-transparent hover:text-accent'
          }`}
        >
          {LABELS[l]}
        </a>
      ))}
    </nav>
  );
}
