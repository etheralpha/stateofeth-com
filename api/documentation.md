---
layout: default
title: API
permalink: /api/v1/documentation
id: apiV1Documentation
---

{% comment %}
{% include components/card-alert.html
  body="The API is still in alpha and under development so endpoints and responses may change or stop working unexpectedly."
  type="danger"
%}

{% include components/card-alert.html
  body="This API is free to use, but please do so responsibly. The data is only updated 1-2 time per day so there's no need to query every minute."
  type="info"
%}

{%- capture content -%}
  The API should only be used for testing & non-commercial hobby usage. For serious research and project development work, the data source's native API should be used.

  To use the API, expand the metric of interest and view the endpoint details.
{%- endcapture -%}
{% include components/card-text.html
	title="Introduction"
  body=content
%}
{% endcomment %}



{%- capture details -%}

Consensus Client Diversity

{% include components/details-api.html
  id="consensusclientdiversityvalidators"
  title="<code>/metrics/consensus-client-diversity-validators</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
  open="true"
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators1"
  title="<code>/metrics/consensus-client-diversity-nodes</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators2"
  title="<code>/metrics/consensus-client-count</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators3"
  title="<code>/metrics/consensus-client-languages</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

---

Execution Client Diversity

{% include components/details-api.html
  id="consensusclientdiversityvalidators4"
  title="<code>/metrics/execution-client-diversity-validators</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators5"
  title="<code>/metrics/execution-client-diversity-nodes</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators6"
  title="<code>/metrics/execution-client-count</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{% include components/details-api.html
  id="consensusclientdiversityvalidators7"
  title="<code>/metrics/execution-client-languages</code>"
  data=site.data.metrics.consensus-client-diversity-validators.content
%}

{%- endcapture -%}


{% include components/card-text.html
	title="Documentation"
  body=details
%}

