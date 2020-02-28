var api = 'cia.atria.edu';
function createEventCard(event) {
    let parent = document.querySelector('.event-list');
    let eventcard = document.createElement('li');
    console.log(event.img);

    eventcard.innerHTML = `<div class="date">
                        <span>${event.month}</span>
                        <h1>${event.date}</h1>
                    </div>
                    <div class="event-img">
                        <img src="${event.img}"
                            alt="">
                    </div>
                    <div class="about-event-right">
                        <h1>
                            ${event.title}
                        </h1>
                        <p>${event.discription}</p>
                    </div>`;
    parent.appendChild(eventcard);
}
function createRecentEventCard(event) {
    let eventTag = document.querySelector('.event-tag');
    let monthNode = document.querySelector('.date span');
    let dateNode = document.querySelector('.date h1');
    let eventImg = document.querySelector('.left-event-child-right .event-img img');
    let eventTitle = document.querySelector('.left-event-child-right .about-event h1');
    let eventDiscription = document.querySelector('.left-event-child-right .about-event p');
    let eventRegisteration = document.querySelector('.left-event-child-right .about-event a');

    saferInnerHTML(eventTag, event.tag);
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
    json.forEach((e) => {
        let date = new Date(e.e_date);
        const months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
        /* let keys = Object.keys(json);
        let values = Object.values(json);
        let extralinks;
        keys.forEach((key)=>{
    
        }); */
        let event = {
            title: e.e_title,
            discription: e.e_description,
            date: date.getDate(),
            month: months[date.getMonth()],
            register: e.e_registration_link,
            venue: e.e_venue,
            img: e.e_image,
            
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
        document.querySelector('.right-event').style.display='none';
    } else {
        events.forEach((event, i) => {
            if (i === 0) {
                event.tag = 'Latest';
                createRecentEventCard(event);
            } else {
                createEventCard(event);
            }
        });
    }

}
function get() {
    let url = 'http://' + api + '/api/v2/events/?format=json';
    var xmlhttp = new XMLHttpRequest();


    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);
            updateUI(parseEventData(myArr));

        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();

}


get();

/* createRecntEventCard({
    month: 'Feb',
    date: '03',
    title: 'test',
    tag: 'test',
    venue: 'tets',
    additionalLinks: {
        from:'8',
        to:'9',
        medium:'link',
    },
    discription: 'test testestte stestt este sttestest testestte stesttes ttesttestt esttestte sttest test'
});
createEventCard({
    month: 'Jan',
    date: '03',
    title: 'test',
    discription: 'testtes ttesttestt esttestte sttest test'
});
 */