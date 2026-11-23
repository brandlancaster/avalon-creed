# Avalon · Credo Avallonis

Static website for Avalon (avaloncreed.com): *Belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment.*

Naming: **Avalon** is the belief-holding body (the religion, church, and entity). **The Way** is its creed: the Code, the Virtues, and the Tenets. "Creed" is used only as a plain description in early introductions, with pointers that the creed is called the Way.
A sibling of [orderofavalon.com](https://orderofavalon.com), re-skinned in crimson and gold.

- Preview: https://creed-preview.avalon-creed.pages.dev
- Production (pages.dev, no custom domain yet): https://avalon-creed.pages.dev

## Layout

| Path | What it is |
| --- | --- |
| `generator/build.py` | Page generator (layout, nav, every page). Copies `static/` then writes HTML into the output folder. |
| `generator/content.py` | Authored copy: opening text, naming pointers, mission, religion section, FAQ, positions, sobriety tenet, Paladinium posts (`POSTS`). |
| `generator/doctrine.py` | Extracts the Code, Virtues and Tenets from the saved source pages in `generator/src/`. |
| `generator/src/` | Saved copies of the original avaloncreed.com pages (doctrine source). |
| `generator/static/` | Hand-edited CSS (and, locally, the image assets). |
| `generator/deploy/` | Cloudflare Pages direct-upload helpers (`make_deploy.py`, `upload.sh`). |
| `site/` | The built site (HTML, CSS, `_redirects`, `robots.txt`). |

Image assets (seal, banner, favicon, og-image under `site/assets/`, `/favicon.ico`) are binary and are not
committed here; they live with the deploy on Cloudflare Pages.

## Pages

`/` · `/avalon/` · `/way/` · `/way/code/` · `/way/virtues/` · `/way/tenets/` · `/faq/` · `/positions/` · `/paladinium/` · `/support/` (includes the Order, `#order`) · `/contact/` · `404.html`

Redirects (301): `/creed/` → `/avalon/`, `/order/` → `/support/#order`.

Old avaloncreed.com paths (`/the-code`, `/the-virtues`, `/the-tenets`, `/faqs`) 301 to the new ones via `_redirects`.

## Build and deploy

```
python3 generator/build.py                      # writes the site
python3 generator/deploy/make_deploy.py <branch> /tmp/creed_deploy.js
generator/deploy/upload.sh <file-with-upload-jwt>
# then create the deployment with the generated /tmp/creed_deploy.js (manifest only)
```

Paths in the scripts are absolute to the build machine; adjust if building elsewhere.
Contact and joining go through orderofavalon.com.

## Paladinium posts

The Paladinium (`/paladinium/`) is the office of the Paladin. To publish, add a dict to `POSTS` in `generator/content.py`
(newest first): `slug`, `title`, `date` (YYYY-MM-DD), `summary`, `body` (HTML paragraphs). Rebuild and deploy; the index
and `/paladinium/<slug>/` are generated. With no posts, the index shows a "coming soon" notice.
