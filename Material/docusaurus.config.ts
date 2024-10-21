import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';


const config: Config = {
  title: 'M8 (EC)',
  tagline: 'Robótica de serviço',
  favicon: 'icons/hh_icon.png',

  url: 'https://rmnicola.github.io',
  baseUrl: '/m8-ec-encontros',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'pt-br'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Módulo 8 (EC)',
      logo: {
        alt: 'Inteli Logo',
        src: 'icons/jjk_icon.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Material de computação',
        },
        {
          href: 'https://github.com/rmnicola/m8-ec-encontros',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    prism: {
      theme: prismThemes.oneLight,
      darkTheme: prismThemes.oneDark,
    },
  stylesheets: [
      {
      href: '/katex/katex.min.css',
      type: 'text/css',
      },
  ],
  } satisfies Preset.ThemeConfig,
};

export default config;
