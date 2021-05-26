"use strict"

const ratings = document.querySelectorAll('.rating')
if (ratings.length > 0){
    initRatings();
}

// Основная функция рейтинга
function initRatings(){
    let ratingActive, ratingValue;
    for (let index = 0; index < ratings.length; index++){
        const rating = ratings[index];
        initRating(rating);
    }

    // Инициализация конкретного рейтинга
    function initRating(rating){
        initRatingVars(rating);
        setRatingActiveWidth();
    }

    // Инициализация переменных
    function  initRatingVars(rating){
        ratingActive = rating.querySelector('.rating_active');
        ratingValue = rating.querySelector('.rating_value');
    }

    // Изменение визуального рейтинга
    function setRatingActiveWidth(index = ratingValue.innerHTML){
        const ratingActiveWidth = index / 0.05;
        ratingActive.style.width = `${ratingActiveWidth}%`;
    }
}