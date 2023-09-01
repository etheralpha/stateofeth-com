# State of Eth Website

## Local Development

1. Clone the repo
1. Install dependencies: `bundle install`
    - Ruby may need to be installed first if not already packaged with your OS
1. Create a feature branch off of the `main` branch
1. Start the local server: `bundle exec jekyll serve --config _config.yml,_config_dev.yml --incremental`
    - The `site.environment` variable can be used to only run certain operations in production vs development
        - The `--config` flag uses development variables in `_config_dev.yml` to override those in `_config.yml`
    - When running the local server, saving a file automatically triggers a build so you can see the changes
        - The `--incremental` flag speeds up the build time by caching the builds and only updating files that were edited
1. Go to <http://localhost:4400/> to view changes

To build the site, use `bundle exec jekyll build`.

Resources:

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Liquid Syntax](https://shopify.github.io/liquid/basics/introduction/)

