source 'https://rubygems.org'

# Jekyll 4 is used directly rather than through the github-pages gem: the site
# is built by .github/workflows/pages.yml, not by the legacy GitHub Pages
# builder, so there is no reason to be bound to that gem's pinned Jekyll 3.10.
gem 'jekyll', '~> 4.3'

# The AcademicPages / Minimal Mistakes stylesheets predate Dart Sass and rely on
# @import and on the vendored susy and breakpoint libraries. jekyll-sass-converter
# 3.x switches to sass-embedded, which rejects part of that syntax. Pinning to
# 2.x keeps the theme compiling; revisit when the stylesheets are modernised.
gem 'jekyll-sass-converter', '~> 2.2'

# Must mirror the "plugins:" list in _config.yml. A plugin declared there but
# absent here makes the build fail with "Dependency Error" at startup.
group :jekyll_plugins do
  gem 'jekyll-feed'
  gem 'jekyll-gist'
  gem 'jekyll-paginate'
  gem 'jekyll-sitemap'
  gem 'jemoji'
end

# Local preview server (no longer bundled with Ruby 3.x).
gem 'webrick', '~> 1.8'

# Link and markup checking, run in CI. Keep in a group so it is not required at
# build time.
group :test do
  gem 'html-proofer', '~> 5.0'
end
