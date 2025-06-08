document.addEventListener('DOMContentLoaded', function() {
    // Image Gallery Functionality for Property Detail Page
    const mainImage = document.getElementById('main-property-image');
    const thumbnailsContainer = document.querySelector('.image-gallery .thumbnails');

    if (mainImage && thumbnailsContainer) {
        const thumbnails = thumbnailsContainer.querySelectorAll('.thumbnail');

        // Function to set a thumbnail as active
        function setActiveThumbnail(selectedThumbnail) {
            // Remove 'active' class from all thumbnails
            thumbnails.forEach(t => t.classList.remove('active'));
            // Add 'active' class to the selected thumbnail
            selectedThumbnail.classList.add('active');
            // Update main image src and alt
            mainImage.src = selectedThumbnail.src;
            mainImage.alt = selectedThumbnail.alt; // Update alt text for accessibility
        }

        thumbnails.forEach(thumbnail => {
            // Set initial active state: if a thumbnail's src matches the main image's src, mark it active.
            // This is useful if the page is loaded with a specific image already displayed in mainImage.
            if (mainImage.src === thumbnail.src) {
                thumbnail.classList.add('active');
            }

            thumbnail.addEventListener('click', function() {
                setActiveThumbnail(this);
            });

            // Keyboard accessibility for thumbnails
            thumbnail.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault(); // Prevent default space scroll or Enter key form submission
                    setActiveThumbnail(this);
                }
            });
        });

        // If no thumbnail is 'active' (e.g. mainImage.src didn't match any thumbnail's src),
        // and there are thumbnails present, set the first one as active by default.
        const currentActive = thumbnailsContainer.querySelector('.thumbnail.active');
        if (!currentActive && thumbnails.length > 0) {
            // setActiveThumbnail(thumbnails[0]); // This line makes the first thumbnail active by default
                                              // The CSS already styles the first thumbnail as active by default if JS is disabled
                                              // or before JS runs. However, explicitly setting it here ensures JS state matches.
                                              // The prompt says "Optional: Set the first thumbnail as active by default if needed"
                                              // and "thumbnails[0].classList.add('active'); // This was styled in CSS"
                                              // The CSS for `.thumbnail.active` handles the visual.
                                              // Let's ensure the main image also reflects this first active thumbnail if no other is active.
            if (thumbnails[0].src !== mainImage.src) { // Only if main image isn't already showing the first thumb
                 // mainImage.src = thumbnails[0].src; // Let's rely on CSS or initial HTML for the very first load
                 // mainImage.alt = thumbnails[0].alt;
            }
            // The CSS might already highlight the first one, or an `.active` class might be on the first thumbnail in HTML.
            // The current logic correctly sets the active class if mainImage.src matches a thumbnail.
            // If not, no thumbnail gets the .active class from JS initially unless explicitly done here.
            // The task's CSS for .thumbnail.active suggests it's JS-driven.
            // Let's ensure if mainImage.src is NOT among thumbnails, the first thumbnail becomes active and updates mainImage.
            let foundActive = false;
            thumbnails.forEach(thumb => {
                if(thumb.src === mainImage.src) foundActive = true;
            });

            if(!foundActive && thumbnails.length > 0){
                 setActiveThumbnail(thumbnails[0]);
            }

        }
    }

    // Add other global JavaScript functionalities below if needed
    // e.g., mobile navigation toggle, form validation helpers, etc.
});
