document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.gif-placeholder').forEach(function(img) {
        img.addEventListener('click', function() {
            // Check if the current src is already the animated GIF to prevent re-loading
            if (this.src !== this.getAttribute('data-gif')) {
                this.src = this.getAttribute('data-gif');
            }
        });
    });
});
