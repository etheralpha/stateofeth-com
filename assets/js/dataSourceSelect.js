// change dataset to alternative source
function updateDataSource(select) {
  let datasets = document.querySelectorAll(`.dataset`)
  datasets.forEach(item => {
    item.classList.add("d-none");
  });
  let selectedSource = select.value;
  let activeDataset = document.querySelector(`.${selectedSource}`);
  activeDataset.classList.remove("d-none");
}
