// Vergaderingen waarvan de indiendatum voorbij is, worden doorgestreept.
(function () {
  var today = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('.dates tr[data-date]').forEach(function (row) {
    if (row.dataset.date < today) row.classList.add('is-past');
  });
})();
