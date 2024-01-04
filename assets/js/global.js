'use strict';

/**
 * Add events on elements
 */

const addEventOnElements = function (elements, eventType, callback) {
    for (const elem of elements) elem.addEventListener(eventType, callback);
}


/**
 * Toggle search box in mobile device || mall creen
 */

const searchBox = document.querySelector("[search-box]");
const searchTogglers = document.querySelectorAll("[search-toggler]");

addEventOnElements(searchTogglers, "click", function() { 
    searchBox.classList.toggle("active");
 });



/*const exploreBtn = document.querySelector('.explore-btn');
const exploreMenu = document.querySelector('.explore-menu');

exploreBtn.addEventListener('click', () => {
  exploreMenu.classList.toggle('show'); 
})*/

