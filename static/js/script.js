$(document).ready(function() {
  // Find the dropdown element and initialize it
  $('.dropdown-toggle').dropdown();
});

function updatePortfolio(portfolioId) {
  // Set the operation to 'update'
  document.getElementById('id_operation').value = 'update';
  // Set the portfolio_id field
  document.getElementById('id_portfolio_id').value = portfolioId;
  // Optionally, populate other fields in the form based on the selected portfolio item
}

function populateForm(portfolioId) {
  // Use AJAX to fetch the portfolio item's data
  fetch(`/portfolio/data/${portfolioId}/`)
      .then(response => response.json())
      .then(data => {
          
          document.getElementById('id_operation').value = 'update';
          document.getElementById('id_portfolio_id').value = portfolioId;
          document.getElementById('id_name').value = data.name;
          document.getElementById('id_description').value = data.description;
          document.getElementById('id_body').value = data.body;
          document.getElementById('id_url').value = data.url;
          document.getElementById('id_image').value = data.image;
          
          console.log("Portfolio ID:", portfolioId);
          // Optionally, change the form's action to point to the update URL
          document.getElementById('UpdatePortfoliosForm').action = `/portfolio/data/${portfolioId}/`;

          // Optionally, change the operation hidden field to 'update'
          document.getElementById('id_operation').value = 'update';
      })
      .catch(error => console.error('Error:', error));
    }


$('.navToggle').on('click', function (e) {
    e.preventDefault();
    $('body').toggleClass('navToggleActive');
  });
  
  
  $(window).scroll(function(){
    if ($(this).scrollTop() > 10) {
      $('body').addClass('fixedHeader');
    } else {
      $('body').removeClass('fixedHeader');
    }
  });
  
  
  var swiper = new Swiper(".testimonialSwiper", {
    navigation: {
      nextEl: ".test-swiper-button-next",
      prevEl: ".test-swiper-button-prev",
    },
  });
  
  
  var swiper = new Swiper(".certificatesSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".cert-swiper-button-next",
      prevEl: ".cert-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });