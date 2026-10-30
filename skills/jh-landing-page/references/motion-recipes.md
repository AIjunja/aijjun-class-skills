# Purposeful landing motion

Inspected sources include Motion's scroll-animation documentation, Magic UI's
Blur Fade reference, Codrops, HOVERSTAT.ES and the supplied AI쭌 motion/UX pack.
Use the catalog for dated access limitations. These recipes describe behavior;
they do not grant permission to copy a showcased site or paid component.

## Choose by purpose

| Purpose | Good motion | Avoid |
|---|---|---|
| Establish the offer | Short staggered reveal of one headline, then readable hold | Repeated word scrambling, essential copy behind a long intro |
| Express real context | Small pointer/scroll displacement of actual media on fine pointers | Fake cursor, heavy blur, making the subject unrecognizable |
| Explain the mechanism | Stable source object moves through identifiable processing stages and produces a changed result | Random particles between boxes with no matching data |
| Compare plans or course days | A deliberate user switch, preserved position, restrained content transition | Auto-swapping while the reader is reading |
| Demonstrate a result | Actual local sample calculation with synthetic-data label and optional export | Canned AI success or fabricated loading time |
| Clarify action | Button's icon/underline responds, focus state equivalent | Magnets that move the button away, hover-only functionality |

## Three practical recipes

### A. Short entrance with readable hold

Use IntersectionObserver to trigger transform/opacity once. Keep initial content
visible when JavaScript fails. Only hide it after animation capability is active,
and make all content immediately visible in reduced-motion mode. Avoid cropping
descenders in reveal masks. Never tween the full paragraph for several seconds.

### B. Light media depth

For a fine pointer and no reduced-motion preference, normalize pointer position
within the hero and change a CSS transform by a small distance, e.g. 3–8px.
Use a pre-scaled image so edges do not reveal gaps. Update at most once per frame,
reset on pointer leave, and do not change body layout or the cursor. This is a
candidate amount, not a requirement for every visual style.

### C. Input to result, with meaningful states

Keep one identifiable source row/file through these states:
read input -> check actual criteria -> calculate -> present result and exceptions.
Link highlights and progress to the current stage, not decorative timers. An
illustrative sequence may run locally, but must be labelled and must not claim a
model or external system was called. Let a visitor change an input and see the
consequence. If offering a download, generate the real current sample result.

## Tool choice

CSS/WAAPI and IntersectionObserver fit small static sites. Existing Motion/GSAP
can handle cross-section or scroll-linked sequences. Use a library where its
actual complexity benefit justifies the payload. The public Motion and Magic UI
documentation does not make all premium examples free. Check the exact source
license before copying code, and do not run arbitrary gallery code.

## Motion review

Check beginning, mid-animation and settled frames; verify that transforms change
and the final state is readable. Test reduced motion, keyboard, touch and fast
scrolling away/back. The system must remain correct after replay or an input
change mid-playback. Cancel old timers/animation frames before starting new work.
Do not use an animation count as a quality score or require MP4 for a webpage.
