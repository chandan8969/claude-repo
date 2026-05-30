import { defineCollection, z } from 'astro:content';

export const collections = {
  projects: defineCollection({
    type: 'content',
    schema: z.object({
      title: z.string(),
      description: z.string(),
      tags: z.array(z.string()),
      githubLink: z.string().url(),
      category: z.enum(['backend-java', 'scripting-py', 'explorations']),
      date: z.date(),
    }),
  }),
};
