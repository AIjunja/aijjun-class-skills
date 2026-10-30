# Reference Source Map

Use this list as a starting map, not as a substitute for examining the project's actual users and content. Check live sources because collections and interfaces change.

## High-Craft Component And Motion Sources

| Source | Best for | Inspect | Caution |
|---|---|---|---|
| [21st.dev](https://21st.dev/) | AI-ready React components, marketing blocks, real app screens, shaders | open the live preview and copy its prompt only after identifying anatomy and states | a copied prompt is not brand translation |
| [Magic UI](https://magicui.design/docs/components) | animated bento, number ticker, marquee, text reveal, interactive buttons, media blocks | trigger, timing, layers, mobile and reduced-motion behavior | use one coherent effect family, not a demo wall |
| [Aceternity UI](https://ui.aceternity.com/explore) | expressive hero, parallax, spotlight, text and media transitions | performance, pointer behavior, text safety and graceful fallback | default effects can overpower operational products |
| [Motion for React](https://motion.dev/docs/react) | scroll-triggered, scroll-linked, layout and gesture animation | `whileInView`, `useScroll`, `layout`, `AnimatePresence`, reduced motion | fading every section is not a motion concept |
| [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) | pinned, scrubbed, sequential storytelling | pin duration, scroll distance, cleanup and mobile behavior | use only when a timeline materially improves understanding |
| [Rive Community](https://rive.app/community/) | interactive brand mark, illustration and state machine | input/state behavior and fallback asset | check license and loading cost |

The component catalog is not the final design system. Select one component family, inspect a concrete demo, and rewrite its tokens, content, states, and responsive behavior around the project.

## Operational Products And Workflows

| Source | Best for | Search for | Caution |
|---|---|---|---|
| [Mobbin](https://mobbin.com/) | real mobile and web product screens, established flows | onboarding, tables, filters, forms, settings | adapt patterns; do not reproduce a product screen |
| [Page Flows](https://pageflows.com/web/) | end-to-end user flows and state transitions | signup, search, checkout, empty state | some content may require an account |
| [SaaSFrame](https://www.saasframe.io/) | SaaS product and marketing screen categories | dashboard, CRM, reports, forms | marketing examples may be too spacious for operational tools |
| [GOV.UK Design System Patterns](https://design-system.service.gov.uk/patterns/) | accessible task flows and forms | check answers, validation, personal details | visual branding is not a universal style template |
| [UX Patterns for Developers](https://uxpatterns.dev/) | comparing interaction patterns and tradeoffs | table, pagination, modal, validation | use it for decisions, not visual mood |

## Landing, Portfolio, Brand, And Editorial Pages

| Source | Best for | Search for | Caution |
|---|---|---|---|
| [Lapa Ninja](https://www.lapa.ninja/) | complete landing pages by industry, color, and style | SaaS, corporate, education, health and fitness | avoid importing landing-page composition into compact tools |
| [Landing.Gallery](https://www.landing.gallery/) | restrained landing-page composition | product, service, portfolio | confirm the live source before adapting details |
| [Refs.Gallery](https://refs.gallery/) | current high-craft websites by tags | corporate, product, typography, minimal | many examples optimize expression over repeated work |
| [A1 Gallery](https://www.a1.gallery/) | curated creative sites | agency, portfolio, product | check usability, not only visual novelty |
| [Awwwards Collections](https://www.awwwards.com/basic/collections/) | expressive web direction and interaction | business, apps, e-commerce, interaction | animation-heavy winners are rarely good defaults for business tools |
| [Godly](https://godly.website/) | contemporary visual and motion references | landing, product, studio | do not imitate visual effects without a product reason |

## Selection Matrix

| Project type | Start here | Typical reference roles |
|---|---|---|
| CRM, dashboard, admin, internal tool | Mobbin + Page Flows + GOV.UK | structure, interaction, accessibility |
| Data report or decision tool | SaaSFrame + UX Patterns + Mobbin | density, control choice, result hierarchy |
| Corporate or program website | Lapa Ninja + Refs.Gallery | structure, visual tone |
| Portfolio or instructor site | Refs.Gallery + A1 Gallery + Lapa Ninja | case-study flow, typography, proof |
| E-commerce or promotion page | Mobbin + Lapa Ninja + Page Flows | conversion structure, visual tone, user flow |
| Public institution service | GOV.UK + UX Patterns + one client brand source | task clarity, accessible pattern, identity |
| Cinematic brand site | Godly or A1 Gallery + one live industry site + Motion or Magic UI | composition, proof order, signature motion |
| Distinctive dashboard | Mobbin or SaaSFrame + Tremor/Recharts + Motion + one 21st.dev app screen | task flow, data story, component craft, state motion |
| AI product | The Shape of AI + Mobbin/Page Flows + assistant-ui or 21st.dev | trust flow, prompt/result states, expressive shell |

## Minimum Source Combination By Product

- **Brand or landing:** one live industry page + one high-craft composition source + one motion/component demo.
- **Dashboard or report:** one real product screen + one data-visualization pattern + one interaction/motion demo.
- **Mobile app:** one complete Mobbin/Page Flows flow + platform guideline + one transition/state reference.
- **AI interface:** one trust/AI UX pattern + one real product flow + one result-state component reference.

Inspect only sources that affect a decision, but do not begin implementation with zero live component or motion evidence.

## Search Discipline

1. Search by the user's job and page type before searching by color or style.
2. Open the live page when possible; a gallery thumbnail can hide poor states or mobile behavior.
3. Select references for specific roles: structure, interaction, visual tone.
4. Record why each reference is relevant and where it does not fit.
5. Prefer current real products over generic template screenshots.
6. Stop collecting after the design direction is supported. More references do not automatically improve the result.
7. Record the exact component demo or page section, not only the gallery home page.
8. Map every selected source to a local component and acceptance capture before coding.
