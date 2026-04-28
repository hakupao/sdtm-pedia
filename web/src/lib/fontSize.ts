export type FontSize = 'sm' | 'md' | 'lg' | 'xl';

const KEY = 'fontsize';
const VALID: FontSize[] = ['sm', 'md', 'lg', 'xl'];

export function getStoredFontSize(): FontSize {
  if (typeof localStorage === 'undefined') return 'md';
  const v = localStorage.getItem(KEY);
  return VALID.includes(v as FontSize) ? (v as FontSize) : 'md';
}

export function setStoredFontSize(s: FontSize): void {
  localStorage.setItem(KEY, s);
}

export function applyFontSize(s: FontSize): void {
  if (s === 'md') {
    document.documentElement.removeAttribute('data-fontsize');
  } else {
    document.documentElement.dataset.fontsize = s;
  }
}
