import type { CollectionEntry } from 'astro:content';
import { supportedLangs, type Lang } from '../i18n/helpers';

export type GuideEntry = CollectionEntry<'guide'>;

export interface SelectedGuideEntry {
  entry: GuideEntry;
  fallback: boolean;
}

export interface GuidePath extends SelectedGuideEntry {
  lang: Lang;
  slug: string;
}

function byOrder(a: SelectedGuideEntry, b: SelectedGuideEntry): number {
  return (a.entry.data.order ?? 99) - (b.entry.data.order ?? 99);
}

export function selectGuideEntry(all: GuideEntry[], slug: string, lang: Lang): SelectedGuideEntry | null {
  const exact = all.find((entry) => entry.data.slug === slug && entry.data.lang === lang);
  if (exact) return { entry: exact, fallback: false };

  const neutral = all.find((entry) => entry.data.slug === slug && entry.data.lang === undefined);
  if (neutral) return { entry: neutral, fallback: false };

  const english = all.find((entry) => entry.data.slug === slug && entry.data.lang === 'en');
  if (english) return { entry: english, fallback: lang !== 'en' };

  return null;
}

export function selectGuideEntries(all: GuideEntry[], lang: Lang, includeChangelog = false): SelectedGuideEntry[] {
  const slugs = [...new Set(all.map((entry) => entry.data.slug))];
  const selected = slugs
    .filter((slug) => includeChangelog || slug !== 'changelog')
    .map((slug) => selectGuideEntry(all, slug, lang))
    .filter((entry): entry is SelectedGuideEntry => entry !== null);

  return selected.sort(byOrder);
}

export function buildGuidePaths(all: GuideEntry[]): GuidePath[] {
  const slugs = [...new Set(all.map((entry) => entry.data.slug))].filter((slug) => slug !== 'changelog');
  const paths: GuidePath[] = [];

  for (const slug of slugs) {
    for (const lang of supportedLangs) {
      const selected = selectGuideEntry(all, slug, lang);
      if (selected) paths.push({ ...selected, lang, slug });
    }
  }

  return paths;
}
