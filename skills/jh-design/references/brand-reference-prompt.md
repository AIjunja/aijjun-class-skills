# Brand Reference Prompt Protocol

Use this protocol for landing pages, corporate sites, portfolios, campaigns, and cinematic redesigns. It turns references into an implementation prompt without copying a source brand.

## 1. Build an evidence pack

Collect only what can change a design decision:

- live URLs and checked date
- desktop and mobile captures of relevant states
- official logo, colors, type, architecture, materials, and owned media
- current copy, actions, routes, and functional states
- media provenance: owner or channel, original URL, subject, crop suitability, and usage risk

Mark each item as `confirmed`, `inferred`, or `missing`. Do not fill missing evidence with stock claims.

## 2. Assign reference roles

Use this matrix. Leave a role empty when it adds no value.

| Role | Question | Output |
|---|---|---|
| Structure | What order moves the visitor from attention to action? | section sequence and density |
| Interaction | How do navigation, filters, selection, and feedback behave? | state and control rules |
| Visual | What creates the perceived tone? | type, palette, grid, imagery, spacing |
| Hook/copy | What earns the first three seconds and sustains attention? | tension, promise, proof, CTA ladder |
| Motion/media | What moves, why, and with what fallback? | sequence, trigger, duration, mobile crop, reduced motion |

For every role, write both `adapt` and `do not copy`. Never use the source's proprietary wording, brand marks, people, statistics, or complete layout.

## 3. Read the project's identity

Extract a reusable grammar rather than decorating with the logo:

- immutable: mark geometry, name, approved colors, factual positioning
- repeatable: modules, lines, materials, image crops, light, rhythm
- removable: inconsistent colors, generic template devices, unsupported claims
- typographic personality: friendly vs sharp, wide vs condensed, quiet vs forceful

Reject a requested font when the live composition proves it conflicts with the desired personality. Explain the evidence and select a licensed alternative.

## 4. Write the copy ladder

Create copy in this order:

1. **Tension:** a true friction or category belief the visitor recognizes
2. **Promise:** what changes because this brand exists
3. **Proof:** owned space, process, people, product, or verified facts
4. **Choice:** programs, services, cases, or locations in visitor language
5. **Action:** one concrete next step and one lower-commitment alternative

Avoid empty claims such as `premium experience`, `best solution`, or `new standard`. Prefer specific conditions, actions, and outcomes that the available evidence supports.

## 5. Produce the implementation prompt

Fill this template before editing code:

```text
PROJECT JOB
[visitor] should [action] after understanding [promise/proof].

BRAND GRAMMAR
- Preserve: [identity elements]
- Repeat: [shape/material/grid rules]
- Remove: [inconsistent or generic patterns]
- Typography: [family, weights, why it fits]

REFERENCE SYNTHESIS
- Structure from [source]: adapt [principle], do not copy [trade dress/content]
- Interaction from [source]: adapt [principle], do not copy [specific UI]
- Visual tone from [source]: adapt [principle], do not copy [identity/layout]
- Hook/copy from [source]: adapt [rhythm], write original evidence-based copy
- Motion/media from [source]: adapt [behavior], use only verified project media

FIRST 3 SECONDS
- Opening frame: [owned media or identity motion]
- Tension: [short line]
- Promise: [short line]
- Primary action: [label]

PAGE SEQUENCE
1. [hook and promise]
2. [real proof]
3. [choice/comparison]
4. [location/case/decision support]
5. [conversion]

MOTION CONTRACT
- Intro job and duration:
- Scroll reveal grammar:
- Staggered elements:
- Hover/focus feedback:
- Reduced-motion state:

RESPONSIVE MEDIA CONTRACT
- Desktop crop or focal point:
- Mobile asset or crop or focal point:
- Poster or failure fallback:
- Text-safe zones:

NON-NEGOTIABLE QA
- Preserve [routes/actions/results]
- Confirm computed font
- Verify media source and currentSrc
- Check 320/360/390/430px overflow and copy-safe elements
- Human-check Korean line breaks, crop, overlap, empty rhythm, and CTA visibility
- Run lint, tests, and production build
```

## 6. Evidence gate

Do not call the pass complete unless the final report distinguishes:

- what was confirmed from official or supplied sources
- what was inferred from repeated brand patterns
- what remains unavailable
- what was verified automatically
- what was inspected visually by a human
