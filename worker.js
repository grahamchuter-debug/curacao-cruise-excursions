/**
 * Curacao Cruise Excursions — Workers Assets entry (Phase 17B).
 * Canonical form: extensionless WITHOUT trailing slash on apex HTTPS
 * (matches live GSC preferred URLs).
 * www → apex; .html → extensionless; trailing slash → drop; query preserved.
 */
const APEX_HOST = 'curacaocruiseexcursions.com';

function toCanonicalPath(pathname) {
  let path = pathname || '/';
  if (path.toLowerCase().endsWith('.html')) {
    path = path.slice(0, -5);
    if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
    if (path === '' || path === '/index') path = '/';
  }
  if (path.length > 1 && path.endsWith('/')) {
    path = path.replace(/\/+$/, '') || '/';
  }
  return path || '/';
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isWww = host === `www.${APEX_HOST}`;
    const isHttp = url.protocol === 'http:';
    const rawPath = url.pathname || '/';
    const hasHtml = rawPath.toLowerCase().endsWith('.html');
    const hasTrail =
      rawPath.length > 1 && rawPath.endsWith('/') && !rawPath.includes('.');

    const is404Doc = rawPath.toLowerCase() === '/404.html';

    if ((isWww || isHttp || hasHtml || hasTrail) && !is404Doc) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      dest.pathname = toCanonicalPath(rawPath);
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    if (isWww || isHttp) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    const assetResponse = await env.ASSETS.fetch(request);

    if (assetResponse.status === 404) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    return assetResponse;
  },
};
