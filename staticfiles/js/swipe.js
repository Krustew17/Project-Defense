document.addEventListener('DOMContentLoaded', function() {
  let currentIndex = 0;
  const images = document.querySelectorAll('.image');
  const nextButton = document.querySelector('.next');
  const prevButton = document.querySelector('.prev');

  function showImage(index) {
    images.forEach((image) => {
      image.style.display = 'none';
    });
    images[index].style.display = 'block';
  }

  function showNextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }

  function showPrevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
  }

  nextButton.addEventListener('click', showNextImage);
  prevButton.addEventListener('click', showPrevImage);

  showImage(currentIndex);
});