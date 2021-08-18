$('#add-cupcake').submit(function (e) {
  e.preventDefault();
  addCupCake();
});

async function addCupCake() {
  let image;
  if ($('#image').val() === '') {
    image = 'https://tinyurl.com/demo-cupcake';
  }
  const data = {
    flavor: $('#flavor').val().toLowerCase(),
    size: $('#size').val().toLowerCase(),
    rating: $('#rating').val(),
    image: image.toLowerCase(),
  };
  await axios.post('/api/cupcakes', data);
  $('#cupcake-list').append(`<li class="cupcake-list">
                    <div class="col-sm-6 col-md-4 col-lg-3 col-xl-2"><b><span
                                class="text-success mr-2">${data.flavor.toUpperCase()}</span></b><span
                            class="mx-1">${data.size.toUpperCase()}</span><span
                            class="badge bg-secondary text-light">${parseFloat(
                              data.rating
                            )}</span>
                        <div><img src="${data.image}" alt="${
    data.flavor
  }" class="img-fluid cupcake-img"></div>
                    </div>
                </li>`);
}
