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



function copyText(el) {
  console.log("copying...");
  let copyIconId = el.id;
  console.log(`\tclicked: ${copyIconId}`);
  let textToCopyId = el.getAttribute("data-copy");
  console.log(`\tcopying: ${textToCopyId}`);
  const textToCopy = document.getElementById(textToCopyId).innerText;
  // const textToCopy = textToCopyId.setSelectionRange();
  console.log(`\tcopied content: ${textToCopy}`);
  navigator.clipboard.writeText(textToCopy).then(function() {
    let tooltipElement = document.getElementById(copyIconId);
    let tooltip = bootstrap.Tooltip.getInstance(tooltipElement);
    setTimeout(() => { tooltip.hide(); }, 1000);
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });

}






