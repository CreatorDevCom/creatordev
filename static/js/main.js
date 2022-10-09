const activeMenu  = () =>{
  document.getElementById('menu').classList.toggle("active-menu")
  document.getElementById('menu-btn').classList.toggle("active-menu-btn")
  document.getElementById('main-content').classList.toggle("stop-back")
}

const toggleProfilePopUp = () =>{ 
  document.getElementById('profile-pop-up-div').classList.toggle('active-profile-pop-up-div')
}

if (typeof window !=="undefined") {
  setTimeout(() => {
    document.getElementById('message-body').style.display="none"
  }, 3000);
}


const hideMessage = () =>{
  
  document.getElementById('message-body').style.display="none"
}