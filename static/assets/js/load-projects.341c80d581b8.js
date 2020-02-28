var api = 'test.ciadev.ninja';
function createprojectCard(project) {
    let parent = document.querySelector('.project-list');
    let projectcard = document.createElement('li');
    project.discription = project.discription.slice(0,120);
    projectcard.innerHTML = `<div class="date">
                        <span>${project.month}</span>
                        <h1>${project.date}</h1>
                    </div>
                    <div class="project-img">
                        <img src="${project.img}"
                            alt="">
                    </div>
                    <div class="about-project-right">
                        <h1>
                            ${project.title}
                        </h1>
                        <p>${project.discription}</p>
                    </div>`;
    parent.appendChild(projectcard);
}
function createRecentprojectCard(project) {

    /* let dateNode = document.querySelector('.date h1'); */
    let projectImg = document.querySelector('.left-project-child-right .project-img img');
    let projectTitle = document.querySelector('.left-project-child-right .about-project h1');
    let projectDiscription = document.querySelector('.left-project-child-right .about-project p');
    let projectRegisteration = document.querySelector('.left-project-child-right .about-project a');

    saferInnerHTML(projectTitle, project.title);
    saferInnerHTML(projectDiscription, project.discription);
    
    if (project.additionalLinks !== undefined) {
        let linksNames = Object.keys(project.additionalLinks);
        let links = Object.values(project.additionalLinks);
        linksNames.forEach((name, i) => {
            saferInnerHTML(projectDiscription, `<br>${name}: ${links[i]}`, true);
        });
    }
    /* saferInnerHTML(dateNode, project.date);
    saferInnerHTML(monthNode, project.month); */
    projectRegisteration.setAttribute('href', project.register);
    projectImg.setAttribute('src', project.img);
}
function parseprojectData(json) {
    var projects = [];
    json.forEach((p) => {
        /* let date = new Date(p.p_date);
        const months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']; */
        /* let keys = Object.keys(json);
        let values = Object.values(json);
        let extralinks;
        keys.forEach((key)=>{
    
        }); */
        let project = {
            title: p.p_title,
            discription: p.p_desc,
            register: p.p_apply_link,
            img: p.p_image,
            additionalLinks: {
                'medium': p.p_medium_link,
            }
        };
        projects.push(project)

    });

    return projects;
}
function updateUI(projects) {
    console.log(projects);
    if (projects.length === 1) {

        createRecentprojectCard(projects[0]);
        document.querySelector('.right-project').style.display = 'none';
        let left = document.querySelector('.left-project');
        let projectsBlock = document.querySelector('.projects');
        projectsBlock.style.setProperty('grid-template-columns', '1fr');
        let RightprojectsBlock = document.querySelector('.left-project-child-right');
        RightprojectsBlock.style.setProperty('display', 'flex');
        RightprojectsBlock.style.setProperty('height', '80vh');
        let aboutproject = document.querySelector('.about-project');
        aboutproject.style.setProperty('margin-left', '15px');
        aboutproject.style.setProperty('margin-top', '15px');
        left.style.width = '100%';
        document.querySelector('.project-img').style.height = '70vh';
    } else {
        projects.forEach((project, i) => {
            if (i === 0) {
                project.tag = 'Latest';
                createRecentprojectCard(project);
            } else {
                createprojectCard(project);
            }
        });
    }

}
function get() {
    let url = 'http://' + api + '/api/v2/getProjects/?format=json';
    var xmlhttp = new XMLHttpRequest();


    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);
            updateUI(parseprojectData(myArr));

        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();

}


get();

/* createRecntprojectCard({
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
createprojectCard({
    month: 'Jan',
    date: '03',
    title: 'test',
    discription: 'testtes ttesttestt esttestte sttest test'
});
 */