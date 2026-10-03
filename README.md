# Build Your Own Online Shop

An interactive, self-paced e-commerce lesson for business and information systems students. It takes about 5–6 hours: Part 1 about 1½–2 hours, Part 2 about 2–2½ hours, Part 3 about 1½ hours.

- **Part 1:** from dot-com to AI. Covers e-commerce types, business models, Web 2.0 and channels, how online payments work, AI, and a real teaching case (Afterpay).
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
- `favicon.svg` is the browser-tab icon.
- Teacher preview: open the site with `#teacher-preview` at the end of the address to unlock every stage (in that browser only) and jump to the business case.
- To change who receives business cases, edit the `CONVENOR_EMAIL` line in `index.html`.
- `tools/make_artifact.py` converts `index.html` into a page for a Claude artifact, swapping the embedded videos for links.

## Viewing it

The site is published with GitHub Pages. To view it locally, serve the folder (for example `python3 -m http.server`) and open it in a browser. The embedded YouTube videos only play over http(s), not when the file is opened directly.

Progress, quiz answers and the business case are saved only in each student's browser. The site collects no data.

## Sources and acknowledgements

**Teaching case:** the Part 1 Afterpay case was written for this module from widely reported public information. It is not endorsed by Afterpay or Block, Inc.

Chapter 7 material is adapted from Rainer, R. K., & Prince, B. (2021). *Introduction to information systems*. John Wiley & Sons.

All logos are trademarks of their owners, used to identify the companies discussed for teaching purposes. The page's Sources section lists all sources and acknowledgements.

Prices, taxes and laws in the module are Australian.
