// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');
const math = require('remark-math');
const katex = require('rehype-katex');

const organizationName = 'rmnicola'; // Usually your GitHub org/user name.
const projectName = 'm8-ec-encontros'; // Usually your repo name.

/** @type {import('@docusaurus/types').Config} */
const config = {
  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.

  title: 'Módulo 8 - EC',
  tagline: 'Robótica móvel e deep learning',
  favicon: 'img/inteli.svg',
  url: `https://${organizationName}.github.io`,
  baseUrl: `/${projectName}/`,

  organizationName: 'rmnicola', // Usually your GitHub org/user name.
  projectName: 'm8-ec-encontros', // Usually your repo name.



  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/${organizationName}/${projectName}/tree/main/docs',
          remarkPlugins: [math],
          rehypePlugins: [katex],
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Módulo 8 - EC',
        logo: {
          alt: 'Logo Inteli',
          src: 'img/inteli.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Material de Computação',
          },
          {
            href: 'https://github.com/rmnicola/m8-ec-encontros',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Módulo 8. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        magicComments: [
        // Remember to extend the default highlight class name as well!
        {
          className: 'theme-code-block-highlighted-line',
          line: 'highlight-next-line',
          block: {start: 'highlight-start', end: 'highlight-end'},
        },
        {
          className: 'code-block-red',
          line: 'red',
        },
        {
          className: 'code-block-green',
          line: 'green',
        },
        {
          className: 'code-block-blue',
          line: 'blue',
        },
        {
          className: 'code-block-purple',
          line: 'purple',
        },
      ],
      },
    }),
  stylesheets: [
      {
        href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
        type: 'text/css',
        integrity:
          'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
        crossorigin: 'anonymous',
      },
    ],
};

module.exports = config;
