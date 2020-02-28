<<<<<<< HEAD
var api = 'cia.atria.edu';
function createEventCard(event) {
    let parent = document.querySelector('.event-list');
    let eventcard = document.createElement('li');
    console.log(event.img);
    event.discription = event.discription.slice(0,120) ;
    eventcard.innerHTML = `<div class="date">
=======
((api = 'test.ciadev.ninja') => {
    let allEvents;
    function createEventCard(event) {
        let parent = document.querySelector('.event-list');
        let eventcard = document.createElement('li');
        eventcard.setAttribute('data-index', event.index);
        saferInnerHTML(eventcard, `<div class="date">
>>>>>>> e392e246893767b73dcefe52174cb963ccd273a4
                        <span>${event.month}</span>
                        <h1>${event.date}</h1>
                    </div>
                    <div class="event-img-about">
                    <div class="event-img">
                        <img src="${event.img}"
                            alt="">
                    </div>
                    <div class="about-event-right">
                        <h1>
                            ${event.title}
                        </h1>
                        <p>${event.discription}</p>
                    </div></div>` );

        parent.appendChild(eventcard);
        eventcard.addEventListener('click', function () {
            console.log(Number(this.getAttribute('data-index')));
            createRecentEventCard(allEvents[Number(this.getAttribute('data-index'))])
        });

    }
    function createRecentEventCard(event) {

        let eventTag = document.querySelector('.event-tag');
        let monthNode = document.querySelector('.date span');
        let dateNode = document.querySelector('.date h1');
        let eventImg = document.querySelector('.left-event-child-right .event-img img');
        let eventTitle = document.querySelector('.left-event-child-right .about-event h1');
        let eventDiscription = document.querySelector('.left-event-child-right .about-event p');
        let eventRegisteration = document.querySelector('.left-event-child-right .about-event a');

        if (event.tag) saferInnerHTML(eventTag, event.tag);
        else saferInnerHTML(eventTag, '');
        saferInnerHTML(eventTitle, event.title);
        saferInnerHTML(eventDiscription, event.discription);
        saferInnerHTML(eventDiscription, `<br>Venue: ${event.venue}`, true);
        if (event.additionalLinks !== undefined) {
            let linksNames = Object.keys(event.additionalLinks);
            let links = Object.values(event.additionalLinks);
            linksNames.forEach((name, i) => {
                saferInnerHTML(eventDiscription, `<br>${name}: ${links[i]}`, true);
            });
        }
        saferInnerHTML(dateNode, event.date);
        saferInnerHTML(monthNode, event.month);
        eventRegisteration.setAttribute('href', event.register);
        eventImg.setAttribute('src', event.img);
    }
    function parseEventData(json) {
        var events = [];
        json.forEach((e, i) => {
            let date = new Date(e.e_date);
            const months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
            /* let keys = Object.keys(json);
            let values = Object.values(json);
            let extralinks;
            keys.forEach((key)=>{
        
            }); */
            let event = {
                index: i,
                title: e.e_title,
                discription: e.e_description,
                date: date.getDate(),
                month: months[date.getMonth()],
                register: e.e_registration_link,
                venue: e.e_venue,
                img: e.e_photos_link,
                additionalLinks: {
                    'starts at': e.e_start_time.split(':')[0] + ':' + e.e_start_time.split(':')[1],
                    'ends at': e.e_end_time.split(':')[0] + ':' + e.e_end_time.split(':')[1],
                    'medium': e.e_medium_link,
                }
            };
            events.push(event)

        });

        return events;
    }
    function updateUI(events) {
        console.log(events);
        if (events.length === 1) {
            events[0].tag = 'Latest';
            createRecentEventCard(events[0]);
            document.querySelector('.right-event').style.display = 'none';
            let left = document.querySelector('.left-event');
            let eventsBlock = document.querySelector('.events');
            eventsBlock.style.setProperty('grid-template-columns', '1fr');
            let RighteventsBlock = document.querySelector('.left-event-child-right');
            RighteventsBlock.style.setProperty('display', 'flex');
            RighteventsBlock.style.setProperty('height', '80vh');
            let aboutevent = document.querySelector('.about-event');
            aboutevent.style.setProperty('margin-left', '15px');
            aboutevent.style.setProperty('margin-top', '15px');
            left.style.width = '100%';
            document.querySelector('.event-img').style.height = '70vh';
        } else {
            events.forEach((event, i) => {
                if (i === 0) {
                    event.tag = 'Latest';
                    createRecentEventCard(event);
                    createEventCard(event);
                } else {
                    createEventCard(event);
                }
            });
        }

    }

    let url = 'http://' + api + '/api/v2/events/?format=json';
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);
            allEvents = parseEventData(myArr);
            updateUI(allEvents);

        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
    window.api = api;
})();




