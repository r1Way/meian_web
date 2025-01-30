//used to change image slider
let currentIndex = 0;
const images = document.querySelectorAll('.slider img');
const thumbnails = document.querySelectorAll('.thumbnail');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

function showImage(index) {
    images.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
    thumbnails.forEach((thumb, i) => {
        thumb.classList.toggle('active', i === index);
    });
    currentIndex = index;
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
}

 console.log(images);
 console.log(thumbnails);
 console.log(prevBtn);
 console.log(nextBtn);

prevBtn.addEventListener('click', prevImage);
nextBtn.addEventListener('click', nextImage);

thumbnails.forEach(thumb => {
    thumb.addEventListener('click', () => {
        showImage(parseInt(thumb.getAttribute('data-index')));
    });
});

// Auto slide every 3 seconds
setInterval(nextImage, 3000);




//lxc 图片浮现
document.addEventListener('DOMContentLoaded', function() {
    // 获取图片元素
    var img = document.querySelector('.fade-in-image');

    // 创建一个IntersectionObserver实例
    var observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                // 当图片进入视口时，添加'visible'类
                img.classList.add('visible');
            } else {
                // 当图片离开视口时，移除'visible'类
                img.classList.remove('visible');
            }
        });
    }, {
        rootMargin: '0px', // 可以设置一个边距，提前触发
        threshold: 0.6 // 当图片的60%进入视口时触发
    });

    // 开始观察图片元素
    observer.observe(img);
});