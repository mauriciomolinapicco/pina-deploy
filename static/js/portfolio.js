function initCarrousel(images, currentIndex, indicatorsElement, interval) {
    function changeImage() {
      images[currentIndex].style.display = "none";
      currentIndex = (currentIndex + 1) % images.length;
      images[currentIndex].style.display = "block";
      updateIndicators();
    }
  
    function updateIndicators() {
      let indicatorsHTML = "";
      for (let i = 0; i < images.length; i++) {
        const indicatorClass = i === currentIndex ? "active" : "";
        indicatorsHTML += `<span class="indicator ${indicatorClass}"></span>`;
      }
      indicatorsElement.innerHTML = indicatorsHTML;
    }
  
    images[currentIndex].style.display = "block";
    updateIndicators();
    setInterval(changeImage, interval);
  }
  
  const carouselImagesBranding = document.querySelectorAll(".mosaico-portfolio-branding img");
  const indicatorsElementBranding = document.querySelector(".carousel-indicators-branding");
  initCarrousel(carouselImagesBranding, 0, indicatorsElementBranding, 3000);
  
  const carouselImagesPosicionamento = document.querySelectorAll(".mosaico-portfolio-posicionamento img");
  const indicatorsElementPosicionamento = document.querySelector(".carousel-indicators-posicionamento");
  initCarrousel(carouselImagesPosicionamento, 0, indicatorsElementPosicionamento, 3000);
  
  const carouselImagesAudiovisual = document.querySelectorAll(".mosaico-portfolio-audiovisual img");
  const indicatorsElementAudiovisual = document.querySelector(".carousel-indicators-audiovisual");
  initCarrousel(carouselImagesAudiovisual, 0, indicatorsElementAudiovisual, 3000);