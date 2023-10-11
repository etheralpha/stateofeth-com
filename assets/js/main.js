---
---

{% include_relative /dataSourceSelect.js %}
{% include_relative /historicalCharts.js %}
{% include_relative /updateLinkTargets.js %}


window.onload = enableTooltips();

function enableTooltips() {
  // Enable tooltips
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
}
