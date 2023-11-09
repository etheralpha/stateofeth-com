ARG VARIANT="3.0.5"
FROM ruby:${VARIANT}

# Install dependencies for Jekyll
RUN gem install bundler jekyll

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash
