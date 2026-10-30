# Gmarket Sans Setup

The bundled assets include Light 300, Medium 500, and Bold 700 from the official Gmarket Sans TTF package. `assets/fonts/OFL.txt` contains the official SIL Open Font License 1.1 text distributed with this skill.

Official source and terms: [Gmarket Sans](https://corp.gmarket.com/fonts/). The official page states that the font uses the SIL Open Font License and is available for personal or corporate, commercial or non-commercial use. Recheck the official page when redistributing outside the project.

After running `scripts/install-gmarket-sans.ps1`, add this to the global stylesheet:

```css
@font-face {
  font-family: "Gmarket Sans";
  src: url("/fonts/GmarketSans-Light.ttf") format("truetype");
  font-style: normal;
  font-weight: 300;
  font-display: swap;
}

@font-face {
  font-family: "Gmarket Sans";
  src: url("/fonts/GmarketSans-Medium.ttf") format("truetype");
  font-style: normal;
  font-weight: 500;
  font-display: swap;
}

@font-face {
  font-family: "Gmarket Sans";
  src: url("/fonts/GmarketSans-Bold.ttf") format("truetype");
  font-style: normal;
  font-weight: 700;
  font-display: swap;
}

:root {
  font-family: "Gmarket Sans", "Noto Sans KR", "Malgun Gothic", sans-serif;
  font-synthesis: none;
}
```

Use 500 for ordinary Korean interface text and 700 for deliberate emphasis. Light 300 is suitable for large display text, not dense form labels or small body copy. Keep `letter-spacing: 0` unless a client brand guide explicitly says otherwise.
