$(document).ready(function() {
  // Initialize dropdown toggles
  $('.dropdown-toggle').dropdown();

  // Function to update portfolio
  function updatePortfolio(portfolioId) {
    // Set the operation to 'update'
    $('#id_operation').val('update');
    // Set the portfolio_id field
    $('#id_portfolio_id').val(portfolioId);
    // Optionally, populate other fields in the form based on the selected portfolio item
  }

  // Function to populate form with portfolio data
  function populateForm(portfolioId) {
    // Use AJAX to fetch the portfolio item's data
    fetch(`/portfolio/data/${portfolioId}/`)
      .then(response => response.json())
      .then(data => {
        // Populate form fields
        $('#id_operation').val('update');
        $('#id_portfolio_id').val(portfolioId);
        $('#id_name').val(data.name);
        $('#id_description').val(data.description);
        $('#id_body').val(data.body);
        $('#id_url').val(data.url);
        $('#id_image').val(data.image);

        // Optionally, change the form's action to point to the update URL
        $('#UpdatePortfoliosForm').attr('action', `/portfolio/data/${portfolioId}/`);
      })
      .catch(error => console.error('Error:', error));
  }

  // Toggle navigation on small screens
  $('.navToggle').on('click', function (e) {
    e.preventDefault();
    $('body').toggleClass('navToggleActive');
    $('.navToggle').toggleClass('active');
  });

  // Handle fixed header on scroll
  $(window).scroll(function(){
    if ($(this).scrollTop() > 10) {
      $('body').addClass('fixedHeader');
    } else {
      $('body').removeClass('fixedHeader');
    }
  });

  // Initialize Swiper for testimonials
  var testimonialSwiper = new Swiper(".testimonialSwiper", {
    navigation: {
      nextEl: ".test-swiper-button-next",
      prevEl: ".test-swiper-button-prev",
    },
  });

  // Initialize Swiper for certificates
  var certificatesSwiper = new Swiper(".certificatesSlider", {
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

  // Initialize Swiper for blog slider
  var blogSwiper = new Swiper(".blogSlider", {
    slidesPerView: 2,
    spaceBetween: 30,
    navigation: {
      nextEl: ".blog-swiper-button-next",
      prevEl: ".blog-swiper-button-prev",
    },
    pagination: {
      el: ".blog-swiper-pagination",
      clickable: true,
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
});
