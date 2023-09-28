// change data timeframe
function updateData(el, chart, days) {
  // hack to remove active class from "all" option since 
  // the default checked option wasn't highlighting
  if (!el.getAttribute("for").includes("-0")) {
    let allOption = el.getAttribute("for").split("-")[0] + "-0";
    document.querySelector(`[for=${allOption}]`).classList.remove("active");
  }
  // let chart = window[el.parentElement.getAttribute('data-chart')];
  console.log(chart)
  chart.data.labels = chart.data.labels_all.slice(-days);
  chart.data.datasets.forEach((data, i) => {
    chart.data.datasets[i].data = chart.data.datasets[i].data_all.slice(-days);
  });
  chart.update();
}
