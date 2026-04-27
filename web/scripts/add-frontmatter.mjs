// web/scripts/add-frontmatter.mjs
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const __dirname = path.dirname(url.fileURLToPath(import.meta.url));
const DIR = path.resolve(__dirname, '../../ai_platforms/release/v1.0');
const ORDER = { 'README': 0, 'USER_GUIDE': 10, 'PLATFORM_COMPARISON': 20, 'DEMO_QUESTIONS': 30, 'GLOSSARY': 40, 'KNOWN_LIMITATIONS': 50, 'CHANGELOG': 60 };
const TITLES = {
  'user-guide':         { zh: '用户手册',       en: 'User Guide',           ja: 'ユーザーガイド' },
  'demo-questions':     { zh: '演示题',         en: 'Demo Questions',       ja: 'デモクエスチョン' },
  'glossary':           { zh: '术语表',         en: 'Glossary',             ja: '用語集' },
  'known-limitations':  { zh: '已知限制',       en: 'Known Limitations',    ja: '既知の制限' },
  'readme':             { zh: 'README',         en: 'README',               ja: 'README' },
  'compare':            { zh: '4 平台对比',     en: 'Platform Comparison',  ja: 'プラットフォーム比較' },
  'changelog':          { zh: '变更日志',       en: 'Changelog',            ja: '変更履歴' },
};

for (const file of fs.readdirSync(DIR)) {
  if (!file.endsWith('.md')) continue;
  const m = file.match(/^([A-Z_]+)(?:\.(zh|en|ja))?\.md$/);
  if (!m) continue;
  const slug = m[1].toLowerCase().replace(/_/g, '-');
  const lang = m[2] || 'en';
  const order = ORDER[m[1]] ?? 99;
  const title = TITLES[slug]?.[lang] ?? m[1];
  const fp = path.join(DIR, file);
  const body = fs.readFileSync(fp, 'utf8');
  if (body.startsWith('---')) continue;  // already has frontmatter
  const fm = `---\nlang: ${lang}\nslug: ${slug}\norder: ${order}\ntitle: "${title}"\n---\n\n`;
  fs.writeFileSync(fp, fm + body);
  console.log(`+ ${file} (lang=${lang}, slug=${slug}, order=${order}, title="${title}")`);
}
