# Validation plan — Blog posts

## Data model
Post, excerpt, featured image, category, author, date, draft or published status.

## Expected implementation
Create the posts as drafts through the admin or the MCP connector, check title, excerpt, image and category, then let a person publish.

## Tests to plan
1. Nominal: Create a complete draft, have it published, then check its rendering, the RSS feed and the sitemap.
2. Refusal check: A draft appears neither on the public site, nor in the sitemap, nor in the feed.
3. Invariant: Never publish or delete content in place of the authorised person.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
