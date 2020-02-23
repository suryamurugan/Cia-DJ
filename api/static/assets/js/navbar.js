/* const snap = (tab, es) => {
    const t = new TimelineMax();

    if (tab == 'p') {
        t.fromTo('.events-section', .4, { x: '0', opacity: '1' }, { x: '200px', opacity: '0', ease: Expo.easeOut });
        t.fromTo('.events-section', .4, { x: '-200px', opacity: '0' }, { x: '0', opacity: '1', ease: Expo.easeOut }, '+=.5');
    } else if (tab == 'e') {
        t.fromTo('.events-section', .4, { x: '0', opacity: '1' }, { x: '-200px', opacity: '0', ease: Expo.easeOut });
        t.fromTo('.events-section', .4, { x: '200px', opacity: '0' }, { x: '0', opacity: '1', ease: Expo.easeOut }, '+=.5');
    }
}; */
const navbtns = () => {
    const homebtn = document.querySelector('.cia-tag');
    const aboutbtn = document.querySelector('.about-btn');
    const blogbtn = document.querySelector('.blog-btn');
    const projectsbtn = document.querySelector('.projects-btn');
    const eventsbtn = document.querySelector('.events-btn');
    homebtn.addEventListener('click', () => document.querySelector('header').scrollIntoView(false));
    aboutbtn.addEventListener('click', () => document.querySelector('.two').scrollIntoView(true));


    if (mobileFlag) {

        let options = {
            threshold: .7
        }
        let counter = 0;
        let navcheck = entry => {
            let target = entry[0].target;
            let nav = document.querySelector('.bottom-nav');
            tabs = nav.children;
            tabs[0].addEventListener('click', () => document.querySelector('header').scrollIntoView(false));
            tabs[1].addEventListener('click', () => document.querySelector('.two').scrollIntoView(true));

            if (counter > 1) {
                if (target.className == 'main-nav') {
                    tabs[0].className = 'selected-tab';
                    tabs[1].className = '';
                } else if (target.className == 'two') {
                    tabs[1].className = 'selected-tab';
                    tabs[0].className = '';
                }
            }
            else counter++;
        };

        let observer = new IntersectionObserver(navcheck, options);
        let sections = document.querySelectorAll('#page-section');
        sections.forEach(section => observer.observe(section));

    }

}


navbtns();

