# Build Your Own Online Shop

An interactive, self-paced e-commerce lesson for business and information systems students. It takes about 5–6 hours: Part 1 about 1½–2 hours, Part 2 about 2–2½ hours, Part 3 about 1½ hours.

- **Part 1:** from dot-com to AI. Covers e-commerce types, business models, Web 2.0 and channels, how online payments work, AI, and a real teaching case (AMARO).
- **Part 2:** build your own shop that takes test payments, using an AI assistant, Stripe, Supabase and Vercel.
- **Part 3:** what it takes to make it real. Covers finding customers, fulfilment, the law, security and ethics, and ends with a short business case.
- **Reference:** a recap of AI tools for vibe coding, a glossary, and sources.

## Learning outcomes

By the end of the module, students can:

1. **Explain** how e-commerce has evolved from the dot-com era to AI-enabled commerce.
2. **Classify** e-commerce businesses and **compare** business models.
3. **Describe** the information systems behind an online sale and **trace** how data flows between them.
4. **Build and test** a working online shop in a test environment.
5. **Analyse** how system design controls business risks.
6. **Evaluate** what it takes to run an online shop as a real business.
7. **Justify** when and how to use AI assistants and agents safely.

## Files

- `index.html` is the whole site and the **master copy**. Edit this file.
- `shots/` holds the screenshots and logos.
- `video/` holds the module introduction video (The Hidden Labyrinth of E-commerce) and the Part 2 Stripe setup screen recording (keys blurred). The Claude version uses a smaller re-encoded copy of the introduction video, because artifacts allow files up to 15 MB.
- `guides/` holds two optional PDF guides for connecting the project's services to an AI assistant (ChatGPT Codex and Claude connectors, each covering GitHub, Supabase, Vercel and Stripe), linked from the AI tools recap and Part 2, Stage 1. `shots/disabled-by-admin.png` comes from the Codex guide. In the Claude version, these links point to the copies on GitHub Pages, because artifacts block downloads.
- Part 2 has an optional Stage 8, Improve your shop’s design (`#p2-design`). It sits outside the required stage plan (see `optionalStage` in the script), so it is never locked, has no compulsory checks and does not affect completion: Part 2 still completes at Stage 7. Its images are `shots/design-textbook-concept.webp`, `shots/design-textbook-storefront.webp` (a browser screenshot of the implemented demo page), `shots/design-comics-concept.webp` and the existing `shots/shop.webp`.
- `audio/` holds the audio introductions to Parts 1–3 (.m4a originals plus .mp3 copies for browsers without AAC support).
- `favicon.svg` is the browser-tab icon.
- Teacher preview: open the site with `#teacher-preview` at the end of the address to unlock every stage (in that browser only) and jump to the business case.
- Student answer boxes: add `data-no-paste="true"` to a textarea to block pasting and show a live word count (optionally add `data-suggested="80–120"` for a suggested length). This is a learning-design nudge, not a security control.
- Copy-restricted content: add `data-no-copy="true"` to a container holding case material or an activity prompt. Text stays selectable, but copy, cut and dragging text out are blocked (answer boxes inside are unaffected). Currently used on the AMARO case narrative and fact panel, the AMARO activity, the business case activity, the Part 1 "Discuss" reflection and the Part 3 "Try it" profit task. This is a learning-design nudge, not a security control.
- To change who receives business cases, edit the `CONVENOR_EMAIL` line in `index.html`.
- `tools/make_artifact.py` converts `index.html` into a page for a Claude artifact, swapping the embedded videos for links.

## Viewing it

The site is published with GitHub Pages. To view it locally, serve the folder (for example `python3 -m http.server`) and open it in a browser. The embedded YouTube videos only play over http(s), not when the file is opened directly.

Progress, quiz answers and the business case are saved only in each student's browser. The site collects no data.

## Sources and acknowledgements

**Acknowledgement:** the Part 1 teaching case activity is adapted (shortened, paraphrased and reorganised), for educational purposes, from Silva, W. J. da, Araújo, G. da C., Rehder, A., & Pedroso, M. C. (2024). Amaro's business model innovation: DNVB or platform? *Revista de Gestão*, 31(4), 371–382. https://doi.org/10.1108/REGE-08-2022-0115. The original is licensed under CC BY 4.0. Figures 1 and 2 are reproduced from the article. The module is not endorsed by the authors, the journal, Emerald Publishing or AMARO.

Chapter 7 material is adapted from Rainer, R. K., & Prince, B. (2021). *Introduction to information systems*. John Wiley & Sons.

All logos are trademarks of their owners, used to identify the companies discussed for teaching purposes. Icons in the business majors section are from Lucide (https://lucide.dev), ISC licence, embedded inline (no external library is loaded). The page's Sources section lists all sources and acknowledgements.

Prices, taxes and laws in the module are Australian.
