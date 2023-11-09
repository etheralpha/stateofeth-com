ARG VARIANT="2.7.8"
FROM ruby:${VARIANT}

# Install dependencies for Jekyll
RUN gem install bundler jekyll
RUN bundle install

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash
