export const REPO = 'hakupao/sdtm-pedia';

export function buildReleaseAssetURL(tag: string, filename: string): string {
  return `https://github.com/${REPO}/releases/download/${tag}/${filename}`;
}
