import { describe, it, expect } from 'vitest';
import { getUIStrings, replaceLangInPath, supportedLangs, type Lang } from './helpers';

describe('i18n.getUIStrings', () => {
  it('returns zh dictionary', () => {
    expect(getUIStrings('zh')['nav.guide']).toBe('文档');
  });
  it('returns en dictionary', () => {
    expect(getUIStrings('en')['nav.guide']).toBeTruthy();
  });
  it('throws on invalid lang', () => {
    expect(() => getUIStrings('fr' as Lang)).toThrow();
  });
});

describe('i18n.replaceLangInPath', () => {
  it('swaps zh→en at prefix', () => {
    expect(replaceLangInPath('/zh/guide/demo', 'en')).toBe('/en/guide/demo');
  });
  it('inserts lang prefix on root', () => {
    expect(replaceLangInPath('/', 'ja')).toBe('/ja/');
  });
  it('preserves trailing slash and query', () => {
    expect(replaceLangInPath('/zh/changelog?v=1', 'en')).toBe('/en/changelog?v=1');
  });
});

describe('supportedLangs', () => {
  it('lists exactly zh/en/ja', () => {
    expect(supportedLangs).toEqual(['zh', 'en', 'ja']);
  });
});
