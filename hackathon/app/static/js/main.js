document.addEventListener('DOMContentLoaded', function() {
  // Lazy load images with Intersection Observer
  const lazyImages = document.querySelectorAll('.responsive-image[data-src]');
  
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
  } else {
    // Fallback for older browsers
    lazyImages.forEach(img => {
      img.src = img.dataset.src;
    });
  }

  // Add loading states for charts
  document.querySelectorAll('.chart-container').forEach(container => {
    const img = container.querySelector('img');
    if (img) {
      img.onload = () => {
        container.classList.remove('loading');
      };
      img.onerror = () => {
        container.innerHTML = '<div class="no-data">Failed to load visualization</div>';
      };
      if (!img.complete) {
        container.classList.add('loading');
      }
    }
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
});