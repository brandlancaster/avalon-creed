# Avalon Creed website

Static website for the Avalon Creed: *Belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment.*
A sibling of [orderofavalon.com](https://orderofavalon.com), re-skinned in crimson and gold.

- Preview: https://creed-preview.avalon-creed.pages.dev
- Production (pages.dev, no custom domain yet): https://avalon-creed.pages.dev

## Layout

| Path | What it is |
| --- | --- |
| `generator/build.py` | Page generator (layout, nav, every page). Copies `static/` then writes HTML into the output folder. |
| `generator/content.py` | Creed copy: creed text, mission, religion section, FAQ, positions, sobriety tenet. |
| `generator/doctrine.py` | Extracts the Code, Virtues and Tenets from the saved source pages in `generator/src/`. |
| `generator/src/` | Saved copies of the original avaloncreed.com pages (doctrine source). |
| `generator/static/` | Hand-edited CSS (and, locally, the image assets). |
| `generator/deploy/` | Cloudflare Pages direct-upload helpers (`make_deploy.py`, `upload.sh`). |
| `site/` | The built site (HTML, CSS, `_redirects`, `robots.txt`). |

Image assets (seal, banner, favicon, og-image under `site/assets/`, `/favicon.ico`) are binary and are not
committed here; they live with the deploy on Cloudflare Pages.

## Pages

`/` · `/creed/` · `/way/` · `/way/code/` · `/way/virtues/` · `/way/tenets/` · `/faq/` · `/positions/` · `/order/` · `/support/` · `/contact/` · `404.html`

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
