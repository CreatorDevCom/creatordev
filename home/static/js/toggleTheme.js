

// Get Current theme
var curTheme = localStorage.getItem("theme");  
var themeBtn =  document.getElementById("toggleTheme-btn");

// Check theme (light ofr dark )
const checkTheme = () =>{  
  if (curTheme == 'dark') { 
    document.body.classList.add('light')    
    document.body.classList.remove('dark') 
  }else{ 
    document.body.classList.add('dark')    
    document.body.classList.remove('light')  
  }
}

//  Toggle Theme
const toggleThemeBtn = ()=>{  
  if (curTheme == 'dark'){
    document.body.classList.toggle('dark')    
    localStorage.setItem("theme",'light') 
  } else{
    localStorage.setItem("theme",'dark')
    document.body.classList.toggle('dark')  
  }
}  
checkTheme()
