function eventAnims() {
    const event = document.querySelector('.event');
    const dis = event.querySelector('.event-discription');
    const title = event.querySelector('.event-title');
    const date = event.querySelector('.event-date');

    event.addEventListener('mouseover', () => {
        date.style.padding='5px';
        date.style.fontSize='.8rem';
        title.style.fontSize = '1.5rem';
        dis.style.opacity = 1;
        console.log('ran');
    });
    event.addEventListener('mouseleave', () => {
        date.style.padding = '10px';
        date.style.fontSize = '1rem';
        title.style.fontSize = '2rem';
        dis.style.opacity = 0;
        console.log('ran');
    });
}
//eventAnims();