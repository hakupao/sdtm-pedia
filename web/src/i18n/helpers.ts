import zh from './ui.zh.json';
import en from './ui.en.json';
import ja from './ui.ja.json';

export type Lang = 'zh' | 'en' | 'ja';
export const supportedLangs: Lang[] = ['zh', 'en', 'ja'];

// Single source of truth for UI keys. zh is the seed dictionary; en/ja must
// have the same keys (enforced by helpers.test.ts key parity tests).
export type UIKey = keyof typeof zh;

const DICTS: Record<Lang, Record<UIKey, string>> = {
  zh,
  en: en as Record<UIKey, string>,
  ja: ja as Record<UIKey, string>,
};

export function getUIStrings(lang: Lang): Record<UIKey, string> {
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
