const APIURL = 'https://api.github.com/users/'

const main = document.getElementById('main');
const form = document.getElementById('form');
const search = document.getElementById('search');

getUser('cokemania2')

async function getUser(user) {
	const resp = await fetch(APIURL + user);
	const respData = await resp.json();
	createUserCard(respData);
	getRepos(user);
}

async function getRepos(user) {
	const resp = await fetch(APIURL + user + '/repos');
	const respData = await resp.json();

	addReposToCard(respData);
}


//getUser('cokemania2');

function createUserCard(user) {
	const card = document.createElement('div');
	card.classList.add('card');

	const cardHTML =  `
		<div class="card">
			<div class="image_container">
				<img class="avatar" src="${user.avatar_url}" alt="${user.name}"/>
			</div>
			<div class="user_info">
				<h2>${user.name}</h2>
				<p>${user.bio}</p>	
				<ul class="info">
					<li>
						
						${user.followers}</li>
						<strong>Followers</strong>
					<li>
						
						${user.following}</li>
						<strong>Following</strong>
					<li>
						
						${user.public_repos}</li>
						<strong>Repos</strong>
				</ul>
				<h4>Repos:</h4>
				<div id="repos"></div>

				</div>
			</div>
		</div>
	`;

	main.innerHTML = cardHTML;
}

form.addEventListener('submit', e=> {
	e.preventDefault();

	const user = search.value;
	if (user) {
		getUser(user);
		search.value = '';
	}
})

function addReposToCard(repos) {
	const reposEl = document.getElementById('repos');

	repos.slice(0, 9).forEach(repo => {
		const repoEl = document.createElement('a');
		repoEl.classList.add('repo');
		repoEl.href = repo.html_url;
		repoEl.target = "_blank"
		repoEl.innerText = repo.name;
		reposEl.appendChild(repoEl);
	})
}