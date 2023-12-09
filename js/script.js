let profile = document.querySelector('.header .flex .profile');

document.querySelector('#user-btn').onclick = () => {
  profile.classList.toggle('active');
  searchForm.classList.remove('active');
};

let searchForm = document.querySelector('.header .flex .search-form');

document.querySelector('#search-btn').onclick = () => {
  searchForm.classList.toggle('active');
  profile.classList.remove('active');
};

window.onscroll = () => {
  profile.classList.remove('active');
  searchForm.classList.remove('active');
};


/*dark mode */

let toggleBtn = document.querySelector('#toggle-btn');
let body = document.body; // Assuming you have a variable named 'body' defined somewhere in your code
let darkMode = localStorage.getItem('dark-mode');

const enableDarkMode = () => {
  toggleBtn.classList.replace('fa-sun', 'fa-moon');
  body.classList.add("dark");
  localStorage.setItem('dark-mode', 'enabled');
}

const disableDarkMode = () => {
  toggleBtn.classList.replace('fa-moon', 'fa-sun');
  body.classList.remove("dark"); // Change add to remove
  localStorage.setItem('dark-mode', 'disabled');
}

if (darkMode === 'enabled') {
  enableDarkMode();
}

toggleBtn.onclick = () => {
  let darkMode = localStorage.getItem('dark-mode');
  if (darkMode === 'disabled') {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
}
