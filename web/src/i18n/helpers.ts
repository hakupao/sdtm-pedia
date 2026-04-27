import zh from './ui.zh.json';
import en from './ui.en.json';
import ja from './ui.ja.json';

export type Lang = 'zh' | 'en' | 'ja';
export const supportedLangs: Lang[] = ['zh', 'en', 'ja'];

const DICTS: Record<Lang, Record<string, string>> = { zh, en, ja };

export function getUIStrings(lang: Lang): Record<string, string> {
  if (!supportedLangs.includes(lang)) throw new Error(`Unsupported lang: ${lang}`);
  return DICTS[lang];
}

export function replaceLangInPath(pathname: string, target: Lang): string {
  const m = pathname.match(/^\/(zh|en|ja)(\/|$)(.*)$/);
  if (m) {
    const rest = m[2] + m[3];
    return `/${target}${rest}`;
  }
  return `/${target}/${pathname.slice(1)}`;
}
