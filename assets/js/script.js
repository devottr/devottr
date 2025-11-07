document.addEventListener('DOMContentLoaded', function() {
            const links = document.querySelectorAll('.contact-links a');
            links.forEach(link => {
                const img = new Image();
                img.src = link.getAttribute('href');
            });
        });