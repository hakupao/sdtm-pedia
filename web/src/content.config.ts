import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import path from 'node:path';

const RELEASE_DIR = path.resolve('../ai_platforms/release/v1.0');

const guide = defineCollection({
  loader: glob({ pattern: '**/*.md', base: RELEASE_DIR }),
  schema: z.object({
    lang: z.enum(['zh', 'en', 'ja']).optional(),
    slug: z.string().optional(),
    order: z.number().optional(),
    title: z.string().optional(),
  }),
});

export const collections = { guide };
